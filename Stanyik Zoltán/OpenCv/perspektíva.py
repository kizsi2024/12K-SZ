import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
# , height = 250, 350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))


width, height = 250, 350
pts1 = np.float32([[276, 130], [452, 127], [274, 350], [458, 373]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", img)
cv2.imshow("Output perspective", imgOutput)

cv2.waitKey(0)
