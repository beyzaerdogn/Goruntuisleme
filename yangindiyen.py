import cv2


mycascade = cv2.CascadeClassifier("fire_detection.xml")
cap = cv2.VideoCapture("yangin.mp4")
front1 = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,frame = cap.read()
    
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   

    fire = mycascade.detectMultiScale(gray,1.3,7)
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x,y),[x+w,y+h],(255,0,0),2)
        cv2.putText(frame,"YANGIN",(x,y),front1,1,(255,0,0), cv2.LINE_4)

        cv2.imshow("yangin var",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
