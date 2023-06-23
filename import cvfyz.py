import cv2
#from playsound import playsound
 
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

cap = cv2.VideoCapture(0)
front1 = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 3)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame, (x-20,y-20),(x+w+20,y+w+20),(255,0,0))
        cv2.putText(frame,"YANGIN",(x,y),front1,1,(255,0,0), cv2.LINE_4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("ateş tespit edildi")
        #playsound ('audio.mp3')

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    # Mesafe tahmini yapma
   

cap.release()
cv2.destroyAllWindows()