import cv2
import numpy as np
def empty(a):
    pass


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640,240)
cv2.createTrackbar("hue min", "trackbars", 0,179, empty)
cv2.createTrackbar("hue max", "trackbars", 179,179, empty)
cv2.createTrackbar("sat min", "trackbars", 0,255, empty)
cv2.createTrackbar("sat max", "trackbars", 255,255, empty)
cv2.createTrackbar("val min", "trackbars", 0,255, empty)
cv2.createTrackbar("val max", "trackbars", 255,255, empty)

while True:
    img = cv2.imread("Resources/lambo.png")
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    s_min = cv2.getTrackbarPos("sat min", "trackbars")
    s_max = cv2.getTrackbarPos("sat max", "trackbars")
    v_min = cv2.getTrackbarPos("val min", "trackbars")
    v_max = cv2.getTrackbarPos("val max", "trackbars")
    print(h_max,h_min,s_max,s_min,v_max,v_min)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv, lower, upper)
    imgresult = cv2.bitwise_and(img,img,mask=mask)

    #cv2.imshow("lambo", img)
    #cv2.imshow("lambo2", imghsv)
    imgstack = stackImages(0.5, ([img, imghsv], [mask, imgresult]))
    cv2.imshow("lambo3", imgstack)
    cv2.waitKey(1)
