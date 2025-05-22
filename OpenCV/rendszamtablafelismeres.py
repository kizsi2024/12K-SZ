import cv2
import numpy as np

img = cv2.imread("resources/car.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y, x+w, y+h), (0,0,255), 2)
cv2.imshow("result", img)
cv2.waitKey(0)