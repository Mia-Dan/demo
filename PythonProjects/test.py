import time

def displayLineByChar(strLine, period=0.1):
    '''display line by character 将一行文字逐字符显示
    para: 
    strLine[str] 要打印的一行文字
    period[float] 每两个字符打印的时间间隔
    '''
    for ch in strLine:
        print(ch, end='')
        time.sleep(period)
    print('') # 换行

print("*Sigh* ",end='')
time.sleep(1)
displayLineByChar("Alright, dude, type whatever you want.",0.05)
time.sleep(0.3)
displayLineByChar("I won't say anything from now on.",0.05)

# a = 5
# if a == 1:
#     print("1")
# elif a == 2:
#     print("2")
# # else:
# #     pass

# print("fin")

# help(str.strip)

# a = "  asd asds  "
# b = a.strip()
# print(a, "- the original string is unchanged")
# print(b, "- should record its value to some place, like this")