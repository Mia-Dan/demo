# Python在terminal运行时的输出样式，一些常用的小函数
import time

# ------ input ------

# TODO: allow whitespace in filepath.
# TODO: debug - what is it when nothing entered? '' or b''?

def dragFileHere():
    ''' Ask user to drag a file into Terminal.
        * Currently, NO whitespace is allowed in filepath.
    Returns:
        If a file is dragged in, return its filepath(str).
        If nothing is dragged in, return None.
    '''
    filepath = input("Drag your file below:\n").strip() # Dragings are likely to leave a whitespace at end
    print(filepath)

    # This works today. 20211129
    if not filepath:  # Python takes empty str as False
        print("Nothing Entered. [1]")
        return

    # #BUG?? It worked yesterday, but failed today? 20211129
    # if filepath == b'': # NOTE: not '', but b''. 
    #     print("Nothing Entered.")
    #     return

    # This works today. 20211129
    # if filepath == '':  
    #     print("Nothing Entered. [2]")
    #     return

    return filepath


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

# dragFileHere() - Test Cases
dragFileHere()
# drag nothing
# drag file without whitespaces 
# drag file with whitespaces ❌

# # displayLineByChar() - Test Cases
# displayLineByChar("")
# displayLineByChar("Hello World!")
# displayLineByChar("Loading...", period=0.2)

# # displayLinesByChar() - Test Cases
# displayLinesByChar("Hello World!")
# displayLinesByChar("1st line... \n2nd line...\n3rd line.")
