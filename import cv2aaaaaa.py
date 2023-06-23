import cv2
import numpy as np

# Kamera yakalama cihazını belirleme
capture = cv2.VideoCapture(0)

while True:
    # Kameradan görüntü yakalama
    ret, frame = capture.read()

    # Görüntüyü yeniden boyutlandırma
    frame = cv2.resize(frame, (640, 480))

    # Gri tonlamalı görüntüye dönüştürme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüyü histogram eşitleme ile iyileştirme
    gray = cv2.equalizeHist(gray)

    # Ateş için eşik değeri belirleme
    thresh_value = 200

    # Eşikleme işlemi uygulama
    ret, thresh_image = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)

    # Ateşin alanını bulma
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ateşin orta noktasını bulma
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Mesafe tahmini yapma
        distance = (thresh_value - gray[cy][cx]) / 10
        print("Ateş noktası: ({}, {})".format(cx, cy))
        print("Ateşe olan mesafe: {} metre".format(distance))

    # Görüntüyü gösterme
    cv2.imshow("Kamera Görüntüsü", frame)

    # Çıkış için bekleyin
    key = cv2.waitKey(1)

    # Eğer 'q' tuşuna basılırsa döngüden çıkın
    if key == ord("q"):
        break

# Kamera yakalama cihazını serbest bırakma
capture.release()

# Pencereleri kapatma
cv2.destroyAllWindows()

cv2.imshow('Kamera görüntü',frame)