import cv2

# Haar-kaskád betöltése a jobb szemhez
eye_cascade = cv2.CascadeClassifier("Resources/haarcascade_righteye_2splits.xml")

# Kép betöltése
img = cv2.imread("Resources/faces.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Szemek detektálása
eyes = eye_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)

# Szemek kiemelése
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Eredmény megjelenítése
cv2.imshow("Result", img)
cv2.waitKey(0)
