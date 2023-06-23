import cv2
import numpy as np

video =cv2.VideoCapture("yangin.mp4")

while True:
    (grabbed,frame) = video.read()
    if not grabbed:
        break
   
    frame=  cv2.resize(frame,(960,540))

    cv2.imshow("output",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.destroyAllWindows()
    video.release()
    cv2.waitKey(0)