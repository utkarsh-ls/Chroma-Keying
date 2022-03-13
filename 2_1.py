import cv2
import os
from os.path import isfile, join, exists

FPS = 10
video = 'vid.mp4'

# Converting Video to Image

folderOut = './1/images/'
fps_im = 4
fr_dur = 1/fps_im

def video_to_image(video, folderOut, fr_dur):
    
    if not exists(folderOut):
        os.makedirs(folderOut)
    
    vid = cv2.VideoCapture(video)
    sec = 0
    frame_ct = 0

    while(1):
        vid.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        ret, frame = vid.read()
        if ret == False:
            break
        sec += fr_dur
        sec = round(sec, 2)

        frame_ct += 1

        # saving the captured frames to disk
        img_name = 'image'+f'{frame_ct:05d}'+'.jpg'
        cv2.imwrite(folderOut+img_name, frame)


video_to_image(video, folderOut, fr_dur)

# Converting Image to Video

pathIn = './1/images/'
pathOut = './1/video.avi'
fps = FPS*fps_im


def image_to_video(pathIn, pathOut, fps):
    
    if not exists(pathIn):
        os.makedirs(pathIn)
    
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: x[5:10])

    frames = []
    for i in range(len(files)):
        filename = pathIn + files[i]
        frame = cv2.imread(filename)
        height, width, layers = frame.shape
        size = (width, height)
        frames.append(frame)

    # MPEG-4 codec (DIVX)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frames)):
        out.write(frames[i])
    out.release()


image_to_video(pathIn, pathOut, fps)
