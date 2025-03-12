import cv2
import numpy as np

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y, x + w, y + h), (0, 0, 255), 2)
    cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break