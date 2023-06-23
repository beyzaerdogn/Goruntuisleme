import cv2
import numpy as np

video =cv2.VideoCapture("yangin.mp4")

while True:
    (grabbed,frame) = video.read()
    if not grabbed:
        break
   
    frame=  cv2.resize(frame,(255,255))

    blur = cv2.GaussianBlur(frame,(21,21),0)#bulanıklaştırdık
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)#renk algılaması için

    lower =[10,50,50]
    upper =[35,255,255]
    lower =np.array(lower,dtype="uint8")
    upper =np.array(upper,dytpe="uint8")
    mask =cv2.inRange(hsv,lower,upper)#sadece alevi odaklar yukardaki kodlar,alev rengi için
    output = cv2.bitwise_and(frame,hsv,mask=mask) # sadece ateşi gösteren resim output
    
    cv2.imshow("output",output)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.destroyAllWindows()
    video.release()
    cv2.waitKey(0)