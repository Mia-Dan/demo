# Python在terminal运行时的输出样式，一些常用的小函数
import time
import os
# ------ input ------

# TODO: support Chinese. 
# UnicodeDecodeError: 'utf-8' codec can't decode ...
# TODO: debug - what is it when nothing entered? '' or b''?

# failed
def dragFileHere(filepath=''): #T: filepath accepts value only when tesing.
    ''' Ask user to drag a file into Terminal, and return its formatted filepath, 
    which can be directly used in futher code, like open(filepath).

    Returns:
        Return its formatted filepath(str), to be directly used in open(filepath).
        If nothing is dragged in, return None.

    # usage note
    1. May use with
        if not mp4Filename: time.sleep(1); quit() # in case dragFileHere() failed
    '''
    while (not filepath):
        filepath = input("Enter/Drag your filepath here 📁:\n")
        if not filepath:  # Python takes empty str as False
            print("\nERROR: No Input.\nTry Again:\n")

    filepath = formatDraggedpath(filepath)

    if not os.path.isfile(filepath) and not filepath: # TODO: can this code ever be reached? as we already have formatDraggedpath()
        raise Exception(f"\nNOT a path, please re-check. \nYour entering = {filepath} \n")


    return filepath

def formatDraggedpath(path=''):
    '''Formatting dragged-into-shell filepath; 
        if path is already in good format, do nothing.'''
    path = path.strip() # Dragged-ins are likely to leave a whitespace at end
    path = path.replace('\\', '') # For filepath containing whitespace, single-quote, etc
    if not os.path.isfile(path):
        raise Exception(f"\nformatDraggedpath() can't deal with it. \n  The exception raising filepath = {path} \n"); return
    return path

def inputChoice(choices=[], prompt='') -> str:
    if not prompt: 
        prompt = f"Choose from {choices}:\n" 

    while True:
        choice = input(prompt)
        if choice in choices: break
        print(f"\nERROR: Invalid Choice.\nChoose Again:\n")
    return choice


# ------ output ------

# TODO: [BUG?] only work in sublime console, but fail in Terminal.
def displayLineByChar(strLine, period=0.1):
    ''' Display line by character 将一行文字逐字符显示
    Parameters:  
        strLine[str] 要打印的一行文字
        period[float] 每两个字符打印的时间间隔
    Returns: 
        None
    '''
    for ch in strLine:
        print(ch, end='')
        time.sleep(period)
    print('') # 换行

def displayLinesByChar(strLines, periodCh=0.1, periodLine=0.3):
    ''' Display lines by character 将一段或多段文字逐字符显示, 文字可含换行符
    Parameters:  
        strLines[str] 要打印的一段或多段文字
        period[float] 每两个字符打印的时间间隔
    Returns: 
        None
    '''
    strLineList = strLines.split('\n')
    for strLine in strLineList:
        displayLineByChar(strLine, periodCh)
        time.sleep(periodLine)

if __name__ == "__main__":
    # dragFileHere() - Test Cases
    # drag nothing
    # drag file without whitespaces 
    # drag file with whitespaces 
    #   e.g. "/Users/admin/Downloads/how\ to\ learn.rtf"
    # drag file with Chinese  ❌
    #   e.g. "/Users/admin/Downloads/喀秋莎的故事\ -\ Planya.mp4 "
    #   # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8a in position 34: invalid start byte
    # ------
    filepath = dragFileHere()
    print(filepath) 
    if filepath: print(os.path.isfile(filepath))


    # # displayLineByChar() - Test Cases
    # displayLineByChar("")
    # displayLineByChar("Hello World!")
    # displayLineByChar("Loading...", period=0.2)

    # # displayLinesByChar() - Test Cases
    # displayLinesByChar("Hello World!")
    # displayLinesByChar("1st line... \n2nd line...\n3rd line.")
