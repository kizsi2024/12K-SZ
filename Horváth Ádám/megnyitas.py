import cv2
import numpy as np


img = cv2 .imread("Resources/cards.jpg")
pts1 = np.float32([[111, 219], [287, 188], [287,388], [111, 419]])
pts2 = np.float32([[0, 0], [200, 0], [200, 200], [0,388]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (250, 350))
cv2.imshow("output", img)
cv2.imshow("output warped", imgOutput)
cv2.waitKey(0)

#my art
#img = np.zeros((500, 500, 3), np.uint8)
#cv2.circle(img, (130, 220), 40, (255, 255, 255), cv2.FILLED)
#cv2.circle(img, (370, 220), 40, (255, 255, 255), cv2.FILLED)
#cv2.putText(img, "^", (190, 370), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 25)
#cv2.line(img, (70, 320), (170, 290), (255, 255, 255), 15)
#cv2.line(img, (70, 360), (170, 330), (255, 255, 255), 15)
#cv2.line(img, (430, 320), (330, 290), (255, 255, 255), 15)
#cv2.line(img, (430, 360), (330, 330), (255, 255, 255), 15)
#cv2.putText(img, "^", (55, 120), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 20)
#cv2.putText(img, "^", (320, 120), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 20)
#cv2.imshow("Image", img)
#cv2.waitKey(0)

#img = np.zeros((512, 512, 3), np.uint8)
#img[200:300, 100:150] = 255, 0, 0
#cv2.line(img, (0, 0), (100, 300), (0, 255, 0), 3)
#cv2.rectangle(img, (0,0), (200,350), (0, 0, 255), #cv2.FILLED
#              3)
#cv2.circle(img, (400, 50), 30, (0, 191, 255), 5)
#cv2.putText(img, "Useless", (200, 300), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1)
#cv2.imshow("Image", img)
#cv2.waitKey(0)

#img = cv2 .imread("Resources/lambo.PNG")
#print(img.shape)
#imgResize = cv2.resize(img, (10000,500))
#print(imgResize.shape)
#imgCropped = img[100:100, 80:200]
#cv2.imshow("Lambo", img)
#cv2.imshow("Cropped Image", imgCropped)
#cv2.waitKey(0)

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Lena", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# this is useless garbage

# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10, 150)
# while True :
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#pip install opencv-python