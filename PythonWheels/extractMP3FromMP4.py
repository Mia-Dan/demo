from pydub import AudioSegment
from cmdUI import dragFileHere # get filename by dragging file into Terminal
import os
import time

print("\nInput mp4 file,")
mp4Filename = dragFileHere()
if not mp4Filename: time.sleep(1); quit() # in case dragFileHere() failed
dirName = os.path.dirname(mp4Filename)

# [a] useless one
# mp3Filename = input("\nOutput MP3 as: (if you don't enter anything, same_name.mp3 in same_dir)\n") 
# if not mp3Filename: 
#     mp3Filename = os.path.splitext(os.path.basename(mp4Filename))[0] + '.mp3'
#     mp3Filename = os.path.join(dirName, mp3Filename)
# [b] save as same_name.mp3 in same_dir
mp3Filename = os.path.splitext(os.path.basename(mp4Filename))[0] + '.mp3'
mp3Filename = os.path.join(dirName, mp3Filename)

AudioSegment.from_file(mp4Filename).export(mp3Filename, format='mp3')
print("\nFinished🍺\n")








