import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 8)
imgCanny= cv2.Canny(img, 158,200)
imgDilation= cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

'''cv2.imshow("Lena", img)
cv2.imshow("szurke", imgGray)
cv2.imshow("augh", imgBlur)
cv2.imshow("tf", imgCanny)
cv2.imshow("gg", imgDilation)'''
cv2.imshow("ni", imgEroded)
cv2.waitKey()