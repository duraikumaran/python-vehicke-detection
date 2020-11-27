import numpy as np
import cv2

cap = cv2.VideoCapture(0)
car_det = cv2.CascadeClassifier('cars.xml')


while True:
    ret, frame = cap.read()
    car = car_det.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in car:
            imu = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = frame[y:y + h, x:x + w]
            roi_color = imu[y:y + h, x:x + w]
            rio_car = frame[y:y + h, x:x + w]
            
    cv2.imshow('op', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()

