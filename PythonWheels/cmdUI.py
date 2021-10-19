
# Python在terminal运行时的输出样式，一些常用的小函数

import time

def displayByChar(strToDisplay, period=0.1):
    '''将一行文字逐字符显示
    para: 
    strToDisplay[str] 要打印的一行文字
    period[float] 每两个字符打印的时间间隔
    '''
    for ch in strToDisplay:
        print(ch, end='')
        time.sleep(period)
    print('') # 换行



# displayByChar() - Test Cases
displayByChar("Hello World!")
displayByChar("Loading...", period=0.2)
