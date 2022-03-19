from cmdUI import formatDraggedpath
from PyPDF2 import PdfFileWriter, PdfFileReader
import typing
from typing import List
'''method PdfFileReader.getPage(i): i begins at zero
'''

def selectPages(reader, writer, startPage, endPage):
    startPage -= 1
    for i in range(startPage, endPage):
        writer.addPage(reader.getPage(i))

def deletePages(reader, writer, pagesToDelete):
    '''Tests: pagesToDelete = [1,2,3,90,91]'''
    pagesToDelete = [page-1 for page in pagesToDelete]
    for i in range(nPages):
        if i not in pagesToDelete:
            writer.addPage(reader.getPage(i))

def deletePages2(reader, writer, pagesToDelete):
    '''Tests: pagesToDelete = [1,2,3,90,91]'''
    pagesToDelete = [page-1 for page in pagesToDelete]
    for i in range(nPages):
        if i not in range(pagesToDelete[0],pagesToDelete[1]+1):
            writer.addPage(reader.getPage(i))

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


# EDIT
inputFilePath = r'''
/Users/admin/computer/其他\ \:\ to\ read/Spark\ in\ Action\,\ Second\ Edition\ -\ Jean-Georges\ Perrin.pdf '''
# /Users/admin/Documents/GitHub/demo/PythonWheels/tmp/A4黑白双面\ 散打2.pdf
outputFilePath = "tmp/auto.pdf" # 默认在代码所在文件夹

# # A. selectPages ----------------------------------------
# startPage = 1 # 开始页，第一页
# endPage = 245 # 截止页，最后一页

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
# selectPages(reader, writer, startPage, endPage)
# movePages(reader, writer, pagesSrcs, pagesDest)
deletePages2(reader, writer, pagesToDelete2)

# don't edit these
with open(outputFilePath,"wb") as outputFile: writer.write(outputFile)


