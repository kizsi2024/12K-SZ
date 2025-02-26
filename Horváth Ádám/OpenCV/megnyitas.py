#steamprogramedu.com
import cv2
import numpy as np

#https://github.com/austinjoyal/haar-cascade-files
img = cv2.imread("resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("resources/haarcascade_eye.xml")
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
eyes = eyeCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y, x+w, y+h), (0,0,255), 2)
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y, x+w, y+h), (0,255,255), 2)
cv2.imshow("result", img)
cv2.waitKey(0)

img2 = cv2.imread("resources/car.png")
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
carCascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")
cars = carCascade.detectMultiScale(imgGray2, 1.1, 4)
for (x, y, w, h) in cars:
    cv2.rectangle(img2, (x, y, x+w, y+h), (0,0,255), 2)
cv2.imshow("result", img2)
cv2.waitKey(0)

#def stackImages(scale,imgArray):
#    rows = len(imgArray)
#    cols = len(imgArray[0])
#    rowsAvailable = isinstance(imgArray[0], list)
#    width = imgArray[0][0].shape[1]
#    height = imgArray[0][0].shape[0]
#    if rowsAvailable:
#        for x in range ( 0, rows):
#            for y in range(0, cols):
#                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                else:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#        imageBlank = np.zeros((height, width, 3), np.uint8)
#        hor = [imageBlank]*rows
#        hor_con = [imageBlank]*rows
#        for x in range(0, rows):
#            hor[x] = np.hstack(imgArray[x])
#        ver = np.vstack(hor)
#    else:
#        for x in range(0, rows):
#            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#            else:
#                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#        hor= np.hstack(imgArray)
#        ver = hor
#    return ver
#
#def getCentaurs(img):
#    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#    for count in contours:
#        area = cv2.contourArea(count)
#        print(area)
#        if area > 5000:
#            cv2.drawContours(imgCentaur, count, -1, (255,0,0), 3)
#            peri = cv2.approxPolyDP(count, cv2.arcLength(count, True) *0.02, True)
#            print(peri)
#            objCor = len(peri)
#            x, y, w, h = cv2.boundingRect(peri)
#
#            if objCor == 3: objectType = "triangle"
#            elif objCor == 4:
#                aspRatio = w / float(h)
#                if aspRatio > 0.98 and aspRatio < 1.03: objectType = "square"
#                else: objectType = "rectangle"
#            if objCor > 4: objectType = "circle"
#            else: objectType = "fuck me if I know"
#            print (objectType)
#            cv2.rectangle(imgCentaur, (x, y), (x+w, y+h), (0,255,0), 2)
#            cv2.putText(imgCentaur, objectType, (x+(w/2)-10, x+(h/2)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
#
#img = cv2.imread("resources/shapes.png")
#imgCentaur = img.copy()
#cv2.imshow("shapes", img)
#
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
#imgCanny = cv2.Canny(imgBlur, 50, 50)
#getCentaurs(imgCanny)
#imgBlank = np.zeros_like(img)
#imgstack = stackImages(0.8, ([img, imgGray, imgBlur],[imgCanny, imgCentaur, imgBlank]))
#cv2.imshow("stack", imgstack)
#cv2.waitKey(0)

#img = cv2.namedWindow("Trackbars")
#img = cv2.resizeWindow("Trackbars", 640,240)
#img = cv2.imread("Resources/lambo.PNG")
#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("car", img)
#cv2.waitKey(0)
#
#
#def stackImages(scale,imgArray):
#    rows = len(imgArray)
#    cols = len(imgArray[0])
#    rowsAvailable = isinstance(imgArray[0], list)
#    width = imgArray[0][0].shape[1]
#    height = imgArray[0][0].shape[0]
#    if rowsAvailable:
#        for x in range ( 0, rows):
#            for y in range(0, cols):
#                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                else:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#        imageBlank = np.zeros((height, width, 3), np.uint8)
#        hor = [imageBlank]*rows
#        hor_con = [imageBlank]*rows
#        for x in range(0, rows):
#            hor[x] = np.hstack(imgArray[x])
#        ver = np.vstack(hor)
#    else:
#        for x in range(0, rows):
#            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#            else:
#                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#        hor= np.hstack(imgArray)
#        ver = hor
#    return ver
#imgStack = stackImages(0.6, [img, imgHSV], [mask, imgResult])
#cv2.imshow("stacked image", imgStack)
#cv2.waitKey(1)
#
#cv2.createTrackbar("hue min", "trackbars", 0, 179, empty)
#cv2.createTrackbar("hue min", "trackbars", 179, 179, empty)
#cv2.createTrackbar("hue min", "trackbars", 0, 255, empty)
#cv2.createTrackbar("hue min", "trackbars", 255, 255, empty)
#cv2.createTrackbar("hue min", "trackbars", 0, 255, empty)
#cv2.createTrackbar("hue min", "trackbars", 255, 255, empty)
#def empty(a):
#    pass
#
#while True:
#    h_min = cv2.getTrackPos("Hue min", "Trackbars")
#    h_max = cv2.getTrackPos("Hue min", "Trackbars")
#    s_min = cv2.getTrackPos("Hue min", "Trackbars")
#    s_max = cv2.getTrackPos("Hue min", "Trackbars")
#    v_min = cv2.getTrackPos("Hue min", "Trackbars")
#    v_max = cv2.getTrackPos("Hue min", "Trackbars")
#    lower = np.array([h_min, s_min, v_min])
#    upper = np.array ([h_max, s_max, v_max])
#    mask = cv2.inRange(imgHSV, lower, upper)
#    imgResult = cv2.bitwise_and(img, img, mask=mask)

#imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))
#cv2.imshow("ImgageStack", imgStack)

#img = cv2.imread("Resources/lena.png")
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgHor = np.hstack(img,img)
#imgVer = np.vstack(img,img)
# img = cv2.imread("Resources/lena.png")
#cv2.imshow("Lena", img)
#cv2.waitKey(0)

#img = cv2 .imread("Resources/cards.jpg")
#pts1 = np.float32([[111, 219], [287, 188], [287,388], [111, 419]])
#pts2 = np.float32([[0, 0], [200, 0], [200, 200], [0,388]])
#matrix = cv2.getPerspectiveTransform(pts1, pts2)
#imgOutput = cv2.warpPerspective(img, matrix, (250, 350))
#cv2.imshow("output", img)
#cv2.imshow("output warped", imgOutput)
#cv2.waitKey(0)

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
##this is useless garbage
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