import os
import glob
from pydub import AudioSegment
 
wenjianjia = []
#path = input('请输入要转码的父文件夹路径：')
path = "/Users/admin/Downloads"
for root, dirs, files in os.walk(path):
    wenjianjia.append(root)
wjj = wenjianjia
# print(wjj)#T # lots of dirs

for dir in wjj:
    video_dir = dir
    extension_list = ('*.mp4', '*.flv')
    i=1
 
    os.chdir(video_dir)
    for extension in extension_list:
        #print(extension)#T # *.mp4, *.flv repeating
        for video in glob.glob(extension):
            print(type(video)) #T #<class 'str'>
            # print(video)#T #video in folder: "storyshift - Frisk.mp4"
            mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
            # print(mp3_filename)#T # #"storyshift - Frisk.mp3"
            AudioSegment.from_file(video).export(mp3_filename, format='mp3')
            # print('已转码', str(i) ,'个视频！')
            # i += 1
             
    # for infile in glob.glob(os.path.join(video_dir, '*.mp4')):
    #     os.remove(infile)

# 请输入要转码的父文件夹路径：/Users/admin/Downloads            
# 已转码 1 个视频！
# 已转码 2 个视频！
# 已转码 1 个视频！