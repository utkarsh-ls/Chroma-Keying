
import cv2
import numpy as np
import os
from os.path import exists

# Opens the inbuilt camera
cam = cv2.VideoCapture(0)
# Count number of frames captured
frame_ct = 0

folderOut = './2/'
if not exists(folderOut):
    os.makedirs(folderOut)

while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == False:
        break
    frame_ct += 1

    # saving the captured frames to disk
    img_name = 'Frame'+str(frame_ct)+'.jpg'
    cv2.imwrite(folderOut+img_name, frame)

    # display the saved image in cv-window
    image = cv2.imread(folderOut+img_name)
    cv2.imshow('Frames', image)
    cv2.waitKey(1)
    
    # Break if user closes cv-window
    if cv2.getWindowProperty('Frames', cv2.WND_PROP_VISIBLE)<1:
        break

cam.release()
cv2.destroyAllWindows()
