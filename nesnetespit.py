import cv2
kamera =cv2.VideoCapture('yangin.mp4')

trackers=cv2.legacy.MultiTracker_create()
while True:
    ret,kare = kamera.read()
    success,boxes = trackers.update(kare)

    for box in boxes :
        
        x,y,w,h = int(box[0]),int(box[1]),int(box[2]),int(box[3])
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,255),3,1)
    key = cv2.waitKey(1)
    if key==ord("a"):
        bbox=cv2.selectROI("kamera",kare)
        trackers=cv2.legacy.TrackerKCF_create()
        trackers.add(trackers,kare,bbox)

    elif  key == ord ("q"):
        break
    cv2.imshow("kamera",kare)
kamera.release()
cv2.destroyAllWindows()