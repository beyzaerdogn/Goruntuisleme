import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


img = cv2.imread("byz.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    
cv2.imshow('img',img)
cv2.waitKey(0)

