import cv2  # OpenCV könyvtár importálása, amely számítógépes látást és képfeldolgozást biztosít.

# Létrehozzuk a faceCascade objektumot, amely a Haar-cascade osztályozót használja az arcok felismerésére
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Kép betöltése
img = cv2.imread("Resources/faces.jpg")

# A kép szürkeárnyalatosra alakítása, mivel az arcok felismeréséhez szürkeárnyalatos képre van szükség
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Arcok detektálása a képben, a detectMultiScale() függvény segítségével
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# A megtalált arcokat körülhatároljuk téglalappal
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Kék téglalap rajzolása az arc köré

# A módosított képet megjelenítjük
cv2.imshow("Result", img)

# Várunk egy billentyűnyomásra, mielőtt bezárnánk az ablakot
cv2.waitKey(0)
