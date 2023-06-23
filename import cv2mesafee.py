import cv2
import numpy as np
#2224 byte
# Kamera bağlantısını aç
cap = cv2.VideoCapture(0)

# Kamera çözünürlüğü
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 

# Sıcaklık eşik değerleri
lower = (50, 50, 50)
upper = (255, 255, 255)

# Ateş tespit edildiği zaman yazacak olan fontu yükle
font = cv2.FONT_HERSHEY_SIMPLEX

# Kamera açıkken
while True:
    # Görüntü yakala
    ret, frame = cap.read()
    
    # Görüntüyü boyutlandır
    scale_percent = 50 # boyutlandırma yüzdesi
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    
    # Sıcaklık filtresi uygula
    mask = cv2.inRange(resized_frame, lower, upper)

    # Kontur tespiti
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ateş tespit edildiği zaman yazacak olan flag değişkeni
    fire_detected = False

    # Her bir kontur için işlem yap
    for contour in contours:
        # Konturun çevresini al
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Konturun merkez noktasını hesapla
        center_x = int(x + (w/2))
        center_y = int(y + (h/2))
        
        # Görüntü boyutuna göre uzaklığı hesapla
        distance = (640*100) / (2 * w * 1.05)
        
        # Merkez noktasını ve uzaklığı ekranda göster
        cv2.circle(resized_frame, (center_x, center_y), 5, (0, 0, 255), -1)
        cv2.putText(resized_frame, '{:.2f} cm'.format(distance), (center_x - 40, center_y - 20), font, 0.5, (255, 255, 255), 2)

        # Ateş tespit edildiyse, flag değişkenini True yap ve ekrana yazı yazdır
        if distance <= 30:
            fire_detected = True
    
    # Ateş tespit edildi ise ekrana yazı yazdır
    if fire_detected:
        cv2.putText(resized_frame, 'ATEŞ TESPİT EDİLDİ!', (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Görüntüyü göster
    cv2.imshow('Kamera', resized_frame)
    
    # Çıkış
