from cmdUI import formatDraggedpath, dragFileHere, inputChoice
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
import typing
from typing import List, Callable
'''
method PdfFileReader.getPage(i): i begins at zero
'''

# Haven't tested. Just ran through the "select" op.

# Deals with input pages like "2,3,6-10,99,1". 
# Shan't break input order.

def input2Pages(inputStr: str) -> List[int]: # x -> add pages in order

    '''* Translates input str like (select)"2,3, 6-10,99,1" 
    into a list [2,3,6,7,8,9,10,99,1]
    '''
    inputStr = inputStr.replace(' ','')
    inputs = inputStr.split(',')
    pages = []
    for inStr in inputs:
        if '->' in inStr:
            pass
            # ??? no idea for now
        elif '-' in inStr:
            [startP, endP] = inStr.split('-')
            startP, endP = int(startP), int(endP)
            appendPRange(startP, endP, pages)
        elif 1: 
            appendP(int(inStr), pages)
    return pages

def movePages(inputStr: str) -> List[int]:
    '''
    * Translates (move)"23-50 -> 100, 325->0",
    which is 23-50 after page 100, 325(say, last page) to front, 
        assume no cross move like "23-50 -> 100, 325->33"
    into a list [325,1,...,22,51,...100,23,...,50,101,...,324]
    '''
    # TODO
    return pages


def appendP(page, pages) -> List[int]:
    pages.append(page)

def appendPRange(startP, endP, pages):
    morePages = list(range(startP, endP+1))
    pages.extend(morePages)

# operations: 
# return page maps: new -> raw, under each operations 
def getOp(op: str) -> Callable[[List[int]], List[int]]: # return a function obj
    opDict = {
        "select": selectP,
        "delete": deleteP,
        "move": moveP,
        "impose": imposeP
    }
    return opDict[op]

def selectP(pages: List[int]) -> List[int]:
    return pages

def deleteP(pages: List[int]) -> List[int]:
    return [p for p in range(nPages+1) if p not in pages] 

def imposeP(imposePattern: List[int]) -> List[int]:
    '''Given order pattern (imposePattern): 8 1 2 7 6 3 4 5, 
    (8 p/fold, print A5 pages with A4 paper)
    this would compute automatically also - 
    16 9 10 15 14 11 12 13
    24 17 18 23 22 19 20 21
    32 25 26 31 30 27 28 29
    https://lifehacker.com/how-to-make-print-and-bind-your-own-books-30796479
    https://superuser.com/questions/690065/how-to-print-pdf-for-book-like-binding
    '''
    # TODO: +1, -1 stuff
    nFold = len(nPages) // len(imposePattern)
    if len(nPages) % len(imposePattern) != 0: 
        print(f"Not all pages included. Pages left: {list(range(len(nPages)*nFold , nPages))}")
        pages = []
    for i in nFold:
        '''generate sequence'''
        tmpFold = [i * len(nPages) + pBase for pBase in imposePattern]
        pages.extend(tmpFold)
    return pages

def moveP(pages: List[int]) -> List[int]:
    return pages



# add to writer
def page2index(page) -> int:
    return page - 1

def addToWriter(reader, writer, pages):
    for p in pages:
        writer.addPage(reader.getPage(page2index(p)))




def movePages(reader, writer, pagesSrcs, pagesDest):
    # 一般来说，移动目的地不会同时有多处（对用户来说，移动导致的页码变更难以计算）。
    # 故假设，pagesSrcs:list，pagesDest:int。
    '''Tests: pagesSrcs = [90,91,92], pagesDest = 12, Move pp.90-92 to before original pp.12.
    pagesSrcs = [4,5,6], pagesDest = 1, Move pp.4-6 to front'''

    iSrcs, iDest = [page-1 for page in pagesSrcs], pagesDest-1
    iNews = [i for i in list(range(nPages)) if i not in iSrcs]
    iNews[iDest:iDest] = iSrcs
    for i in iNews:
        writer.addPage(reader.getPage(i))


# showHelp() # there should be a better way to call, feels like help(pdfUtilities)?
print()
inputFilePath = dragFileHere()
reader = PdfFileReader(open(inputFilePath, "rb"))
nPages = reader.getNumPages()
print()
op = inputChoice(choices=['select','delete','move','impose'])
inputP = input2Pages(input("Then args: "))
pages = getOp(op)(inputP)
print()
outputFilePath = '/Users/admin/Downloads/auto.pdf'
writer = PdfFileWriter()
addToWriter(reader, writer, pages)
with open(outputFilePath,"wb") as outputFile: writer.write(outputFile)
print("Finish! 🍺")

# # EDIT
# inputFilePath = r'''
# /Users/admin/computer/其他\ \:\ to\ read/Spark\ in\ Action\,\ Second\ Edition\ -\ Jean-Georges\ Perrin.pdf 
# '''
# # /Users/admin/Documents/GitHub/demo/PythonWheels/tmp/A4黑白双面\ 散打2.pdf
# outputFilePath = "tmp/auto.pdf" # 默认在代码所在文件夹

'''
# # A. selectPages ----------------------------------------
# startP = 1 # 开始页，第一页
# endP = 245 # 截止页，最后一页

# # B. movePages ------------------------------------------
# pagesSrcs = [4,5,6]
# pagesDest = 1

# C. deletePages ------------------------------------------
pagesToDelete2 = [377,562]
# pagesToDelete = [2,3,6,7]

# don't edit these
inputFilePath = formatDraggedpath(inputFilePath)
writer = PdfFileWriter()
reader = PdfFileReader(open(inputFilePath, "rb"))
nPages = reader.getNumPages()

# EDIT
# selectPages(reader, writer, startP, endP)
# movePages(reader, writer, pagesSrcs, pagesDest)
deletePages2(reader, writer, pagesToDelete2)

# don't edit these
with open(outputFilePath,"wb") as outputFile: writer.write(outputFile)
'''

