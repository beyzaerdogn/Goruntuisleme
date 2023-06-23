import cv2
import numpy as np

# Kamera ayarlarını yapma
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Kameradan görüntüyü alma
    ret, frame = cap.read()

    # Görüntüyü Griye çevirme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüyü histogram eşitleme ile iyileştirme
    gray = cv2.equalizeHist(gray)

    # Ateş için eşik değeri belirleme
    thresh_value = 200

    # Eşikleme işlemi uygulama
    ret, thresh_image = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)

    # Ateşin alanını bulma
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ateşin orta noktasını bulma ve mesafe hesaplama
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Kare oluşturma
        square_size = 100
        x1 = cx - square_size // 2
        y1 = cy - square_size // 2
        x2 = cx + square_size // 2
        y2 = cy + square_size // 2
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Mesafe tahmini yapma
        distance = (thresh_value - gray[cy][cx]) / 10
        cv2.putText(frame, "Ateşe olan mesafe: {} metre".format(distance), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Görüntüyü gösterme
    cv2.imshow("Ateş Tespiti", frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bellekleri serbest bırakma ve çıkış
cap.release()
cv2.destroyAllWindows()
