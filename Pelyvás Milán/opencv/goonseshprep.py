import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
width, height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgoutput = cv2.warpPerspective(img,matrix, (width,height))

ptsa = np.float32([[276,130],[450,130],[274,350],[454,372]])
ptsb = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix2 = cv2.getPerspectiveTransform(ptsa, ptsb)
imgoutput2 = cv2.warpPerspective(img,matrix2, (width,height))

cv2.imshow("image", img)
cv2.imshow("output", imgoutput)
cv2.imshow("output2", imgoutput2)
cv2.waitKey(0)