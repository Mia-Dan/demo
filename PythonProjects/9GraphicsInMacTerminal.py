import time
import os
import random

def initRain(numRainDrops, rowWidth, picHeight):
    # Constraints: picWidth > numRainDrops
    initPosiRainDrops = random.sample(range(1,picWidth+1), numRainDrops) # sampling without replacement
    initIndexRainDrops = [initPosiRainDrop - random.choice(range(picHeight)) * rowWidth for initPosiRainDrop in initPosiRainDrops]
    return initIndexRainDrops

def addRain(initIndexRainDrops, rowWidth, picHeight, tmpListFrame, i):
    level = i % picHeight
    for initIndexRainDrop in initIndexRainDrops:
        objIndex = initIndexRainDrop + level * (rowWidth - 1) # Raining in the wind
        isObjAtLR = ((objIndex % (picWidth + 1)) == picWidth)  
        isObjWaitting = (objIndex < 0)
        if isObjAtLR or isObjWaitting: 
            pass
        else: 
            tmpListFrame[objIndex] = charFG

# TODO: 雨滴函数化。对每个雨滴，输入初始位置，当前时刻；输出图案。
picWidth, picHeight = 50, 10
mode = "rain"
numRainDrops = 27
# char example: '■',' ','❄️'
charBG = ' ' # background char
charFG = '💧' # foreground char
numFrames = 30 # 30 frames in total
timeEachFrame = 0.3 # each frame last xx s
pic = (charBG * picWidth + "\n") * picHeight 
rowWidth = picWidth + 1 # (picWidth+1) characters per row

if mode == "rain": 
    initIndexRainDrops = initRain(numRainDrops, rowWidth, picHeight)

for i in range(numFrames):
    os.system('clear')
    tmpListFrame = list(pic)

    if mode == "rain": 
        addRain(initIndexRainDrops, rowWidth, picHeight, tmpListFrame, i)

    frame = ''.join(tmpListFrame)
    print(frame)
    time.sleep(timeEachFrame)



# TODO: 做一个图像转点阵。
# 用处：在terminal中图像显示。


# TODO: 图片转点阵。下采样。
#improve：颜色方面用Matlab的公式吧。
#链接：https://www.zhihu.com/question/33646570/answer/102046631

# import Image
 
# color = 'MNHQ$OC?7>!:-;.' #zifu
 
# def to_html(func):
#     html_head = '''
#             <html>
#               <head>
#                 <style type="text/css">
#                   body {font-family:Monospace; font-size:5px;}
#                 </style>
#               </head>
#             <body> '''
#     html_tail = '</body></html>'
#  # ding yi HTML
#     def wrapper(img):
#         pic_str = func(img)
#         pic_str = ''.join(l + ' <br/>' for l in pic_str.splitlines())
#         return html_head + pic_str + html_tail
 
#     return wrapper
#  # fan hui zhi
# @to_html
# def make_char_img(img):
#     pix = img.load()
#     pic_str = ''
#     width, height = img.size
#     for h in xrange(height):
#         for w in xrange(width):
#             pic_str += color[int(pix[w, h]) * 14 / 255]
#         pic_str += '\n'
#     return pic_str
 
# def preprocess(img_name):
#     img = Image.open(img_name)
 
#     w, h = img.size
#     m = max(img.size)
#     delta = m / 200.0
#     w, h = int(w / delta), int(h / delta)
#     img = img.resize((w, h))
#     img = img.convert('L')
 
#     return img
 
# def save_to_file(filename, pic_str):
#     outfile = open(filename, 'w')
#     outfile.write(pic_str)
#     outfile.close()
 
# def main():
#     img = preprocess(raw_input('input your filename:'))
#     pic_str = make_char_img(img)
#     save_to_file('char.html', pic_str)
 
# if __name__ == '__main__':
#     main()

# # TODO: 做一个滚动文字显示


# # optTODO: 点阵汉字
# # https://blog.csdn.net/weixin_40796925/article/details/86491343
