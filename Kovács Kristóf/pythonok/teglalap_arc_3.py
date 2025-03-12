import cv2

faceCascade = cv2.CascadeClassifier("Resources/")

img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColoe(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Result", img)

    cv2.waitKey(0)