import cv2
import numpy as np

# video_bg->with green screen
# video_fg->without green screen
video_gr = cv2.VideoCapture("green.mp4")
video_ngr = cv2.VideoCapture("video.webm")
fps = video_gr.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('./3.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (640,480))

while True:

    ret, frame = video_gr.read()
    if ret==False:
        break
    gr_video = cv2.resize(frame, (640, 480))
    
    ## [B value, G value, R value]
    lower_green = np.array([0, 150, 0])
    upper_green = np.array([100, 255, 100])

    # Creates a binary mask and filters the bg_frame
    # (white(255)->within range, black(0)->out of range)
    mask = cv2.inRange(gr_video, lower_green, upper_green)
    res = cv2.bitwise_and(gr_video, gr_video, mask=mask)

    f = gr_video - res
    
    ret, frame = video_ngr.read()
    if ret==False:
        break
    ngr_video = cv2.resize(frame, (640, 480))
    f = np.where(f == 0, ngr_video, f)

    cv2.imshow("video", ngr_video)
    cv2.imshow("mask", f)
    out.write(f)
    if cv2.waitKey(25) == 27:
        break

video_gr.release()
video_ngr.release()
out.release()
cv2.destroyAllWindows()

# Check range (problem for different shades of green)



import cv2
import numpy as np

# video_bg->with green screen
# video_fg->without green screen
# video_gr = cv2.VideoCapture("green.mp4")
# video_ngr = cv2.VideoCapture("video.webm")
# fps = video_gr.get(cv2.CAP_PROP_FPS)
# out = cv2.VideoWriter('./3.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (640,480))

# while True:

frame = cv2.imread('/home/sthawk/Pictures/r1.jpeg')
# if ret==False:
#     break
height, width, layers = frame.shape
gr_video = cv2.resize(frame, (width, height))

## [B value, G value, R value]
lower_green = np.array([0, 150, 0])
upper_green = np.array([100, 255, 100])

# Creates a binary mask and filters the bg_frame
# (white(255)->within range, black(0)->out of range)
mask = cv2.inRange(gr_video, lower_green, upper_green)
res = cv2.bitwise_and(gr_video, gr_video, mask=mask)

f = gr_video - res

frame = cv2.imread('/home/sthawk/Pictures/Webcam/wallpaperarchives18141space ultra hd 4k wallpaper planet satellites.jpg')
# if ret==False:
#     break
# height, width, layers = frame.shape
ngr_video = cv2.resize(frame, (width, height))
f = np.where(f == 0, ngr_video, f)

cv2.imshow("video", ngr_video)
cv2.imshow("mask", f)
cv2.imwrite('/home/sthawk/Pictures/Webcam/rashis.jpeg',f)
cv2.waitKey(10000)

# out.write(f)
# if cv2.waitKey(25) == 27:
#     break

# video_gr.release()
# video_ngr.release()
# out.release()
cv2.destroyAllWindows()

# Check range (problem for different shades of green)