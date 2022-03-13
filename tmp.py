import cv2
import os
from os.path import isfile, join, exists

pathIn= './1/images/'
pathOut = './1/video.avi'
# fps = FPS/fps_im

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
print(files)
files.sort(key = lambda x: x[5:-4])

print(files)