import numpy as np
import cv2

fire_cascade = cv2.CascadeClassifier("fire_detection.xml")

cap = cv2.VideoCapture("yangin.mp4")

while(True):
    ret, frame = cap.read()
    gray   = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('frame', frame)
    key = cv2.waitKey(0) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
    cv2.destroyAllWindows()
    cap.release()
    
 
   
