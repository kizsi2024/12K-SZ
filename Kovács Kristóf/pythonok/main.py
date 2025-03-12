import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")

cv2.imshow("Shapes", img)

cv2.waitKey(0)

img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()
