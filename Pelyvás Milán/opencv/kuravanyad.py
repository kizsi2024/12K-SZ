import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)

#imgresize = cv2.resize(img, (1000,500))
imgcropped = img[0:200, 200:500]
imgcropped2 = img[40:400, 50:500]

cv2.imshow("car", img)
#cv2.imshow("l", imgcropped)
cv2.imshow("ll", imgcropped2)
#cv2.imshow("a", imgresize)

cv2.waitKey()