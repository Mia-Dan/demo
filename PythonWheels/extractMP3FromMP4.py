from pydub import AudioSegment
from cmdUI import dragFileHere # get filename by dragging file into Terminal

print("Input mp4 file - ")
mp4Filename = dragFileHere()
print(mp4Filename) #T

mp3Filename = input("Output MP3 as: (by default, same_name.mp3 in same_dir)\n")
#isNoEnter = (mp3Filename == b"") 
#isNoEnter = (mp3Filename == "") #AttributeError: 'bytes' object has no attribute 'seek' 
# no, that's because "mp3Filename = input("...").encode('unicode-escape')"
isNoEnter = (mp3Filename == "")
if isNoEnter: 
    mp3Filename = "/Users/admin/Desktop/1.mp3"
print(mp3Filename) #T
AudioSegment.from_file(mp4Filename).export(mp3Filename, format='mp3')








