import cv2
import numpy as np

# Kameradan görüntü akışını almak için kullanılacak capture objesi oluşturma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare okuma
    ret, frame = cap.read()
    
    # Kameradan alınan karenin boyutlarını alarak dikdörtgen koordinatları hesaplama
    height, width, _ = frame.shape
    rect_height, rect_width = int(height/2), int(width/2)
    x1, y1 = int(width/2 - rect_width/2), int(height/2 - rect_height/2)
    x2, y2 = int(width/2 + rect_width/2), int(height/2 + rect_height/2)
    
    # Kareyi yeniden boyutlandırma ve grayscale yapma
    resized_frame = cv2.resize(frame, (640, 480))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Görüntüyü histogram eşitleme ile iyileştirme
    equalized_frame = cv2.equalizeHist(gray_frame)

    # Ateş için eşik değeri belirleme
    thresh_value = 200

    # Eşikleme işlemi uygulama
    ret, thresh_image = cv2.threshold(equalized_frame, thresh_value, 255, cv2.THRESH_BINARY)

    # Ateşin alanını bulma
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ateşin orta noktasını bulma
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # Mesafe tahmini yapma
        distance = (thresh_value - equalized_frame[cy][cx]) / 10
        cv2.putText(resized_frame, "Ateşe olan mesafe: {} metre".format(distance), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Ateş noktasını kırmızı bir dikdörtgen içine alma
        cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            cv2.circle(resized_frame, (cx, cy), 5, (0, 0, 255), -1)
        else:
            cv2.circle(resized_frame, (cx, cy), 5, (255, 0,0))
