import cv2

# Az arc detektor betöltése
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Webkamera elindítása
cap = cv2.VideoCapture(0)

while True:
    # Képkocka olvasása a webkamerából
    success, img = cap.read()
    if not success:
        break

    # Szürkeárnyalatos képpé alakítás
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Arcok detektálása
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    # Téglalapok rajzolása az arcok köré
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Eredmény megjelenítése
    cv2.imshow("Result", img)

    # Kilépés, ha 'q' billentyűt nyomnak
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Webkamera felszabadítása és összes ablak bezárása
cap.release()
cv2.destroyAllWindows()
