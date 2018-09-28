
import cv2
import os
import numpy as np

# Arguments

output = "C:\\Users\\ashanbhag\\Desktop\\Momento\\Chinmay\\Chinmay.avi"
video_path="C:\\Users\\ashanbhag\\Desktop\\Momento\\Chinmay\\Chinmay.mp4"
vidcap = cv2.VideoCapture(video_path)

# Define the codec and create VideoWriter object
# Be sure to use lower case
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(output,fourcc, 24, (1920,1080))


success,image = vidcap.read()
count = 0
success = True

while success:

    img1 = cv2.resize (image, (1920, 1080), interpolation=cv2.INTER_CUBIC)

    out.write(img1) # Write out frame to video
    cv2.imshow('video',img1)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

    success,image = vidcap.read()
    print('Read a new frame: '+str(count))
    count += 1



# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

