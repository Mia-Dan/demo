a = 2
for i in range(5):
    if i==4:
        a=3
        break
    if a==3:
        print("a")
    print(i)




# # both are global, yep
# str1 = "asdhd"
# int1 = 182
# def print1():
#     print(str1)
#     print(int1)

# print1()









# BUG1
# import time

# def displayLineByChar(strLine, period=0.1):
#     '''display line by character 将一行文字逐字符显示
#     para: 
#     strLine[str] 要打印的一行文字
#     period[float] 每两个字符打印的时间间隔
#     '''
#     for ch in strLine:
#         print(ch, end='')
#         time.sleep(period)
#     print('') # 换行

# print("*Sigh* ",end='')
# time.sleep(1)
# displayLineByChar("Alright, dude, type whatever you want.",0.05)
# time.sleep(0.3)
# displayLineByChar("I won't say anything from now on.",0.05)
