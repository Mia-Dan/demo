
# Python在terminal运行时的输出样式，一些常用的小函数

import time

def displayLineByChar(strLine, period=0.1):
    '''display line by character 将一行文字逐字符显示
    TODO:?BUG only work in sublime console, but fail in Terminal.
    para: 
    strLine[str] 要打印的一行文字
    period[float] 每两个字符打印的时间间隔
    '''
    for ch in strLine:
        print(ch, end='')
        time.sleep(period)
    print('') # 换行

def displayLinesByChar(strLines, periodCh=0.1, periodLine=0.3):
    '''display lines by character 将一段或多段文字逐字符显示, 文字可含换行符
    para: 
    strLines[str] 要打印的一段或多段文字
    period[float] 每两个字符打印的时间间隔
    '''
    strLineList = strLines.split('\n')
    for strLine in strLineList:
        displayLineByChar(strLine, periodCh)
        time.sleep(periodLine)


# displayLineByChar() - Test Cases
displayLineByChar("")
displayLineByChar("Hello World!")
displayLineByChar("Loading...", period=0.2)

# displayLinesByChar() - Test Cases
displayLinesByChar("Hello World!")
displayLinesByChar("1st line... \n2nd line...\n3rd line.")
