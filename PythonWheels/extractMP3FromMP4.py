from pydub import AudioSegment

mp4Filename = b''
while mp4Filename == b'':
    mp4Filename = input("Drag MP4 below:\n").strip() # Draging are likely to leave a whitespace 
# at the end of string, which then causes #FileNotFoundError: [Errno 2] No such file or directory
mp3Filename = input("Output MP3 as: (by default, name as 1.mp3 on desktop)\n").encode('unicode-escape')
isNoEnter = (mp3Filename == b"") 
#isNoEnter = (mp3Filename == "") #AttributeError: 'bytes' object has no attribute 'seek'
#print(mp3Filename) 
if isNoEnter: 
    mp3Filename = "/Users/admin/Desktop/1.mp3"
AudioSegment.from_file(mp4Filename).export(mp3Filename, format='mp3')