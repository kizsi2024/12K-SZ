import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#img[200:300, 100:150] = 255,0,0

'''cv2.line(img, (0,0), (100,300), (0,255,0), 3)
cv2.rectangle(img, (0,0), (200,300), (0,0,255), cv2.FILLED)
cv2.circle(img, (400,50), 30, (255,255,0), 5)
cv2.putText(img, "Dr.Goon", (300,200), cv2.FONT_HERSHEY_COMPLEX,1,(0,100,0), 3)'''

cv2.rectangle(img, (300,430), (200,300), (0,0,255), 4)
cv2.rectangle(img, (250,350), (210,320), (0,0,255), 4)
cv2.rectangle(img, (285,430), (260,380), (19,69,139), 4)
cv2.line(img, (250,200), (200,300), (0,255,0), 3)
cv2.line(img, (250,200), (300,300), (0,255,0), 3)
cv2.putText(img, "Dr.Goon", (300,200), cv2.FONT_HERSHEY_COMPLEX,1,(0,100,0), 3)
cv2.imshow("image", img)
cv2.waitKey(0)