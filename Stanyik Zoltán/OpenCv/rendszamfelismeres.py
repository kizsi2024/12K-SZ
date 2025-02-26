import cv2  # OpenCV könyvtár importálása, amely lehetővé teszi a képfeldolgozást és számítógépes látást.

# Arcfelismerő vagy rendszámtábla felismerő modell betöltése
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
# A 'haarcascade_russian_plate_number.xml' fájl egy előre betanított modell, amely orosz rendszámtáblák felismerésére van kiképezve.
# Ha arcokat szeretnél felismerni, akkor másik modellt, például 'haarcascade_frontalface_default.xml'-t használhatsz.

# Kép betöltése
img = cv2.imread("Resources/p1.jpg")  # Betölti a 'Resources/p1.jpg' képet a változóba.

# A képet szürkeárnyalatossá alakítjuk
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# A képből szürkeárnyalatos képet készítünk, mert az arcfelismerő algoritmusok jobban működnek, ha nincs színinformáció.

# Arcfelismerés elvégzése
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
# Az arcfelismerő algoritmus segítségével megkeressük az arcokat a szürkeárnyalatos képen.
# Az első paraméter az input kép, a második paraméter (1.1) az a scaling factor, amely segít a méretarányok megtalálásában,
# a harmadik paraméter (4) pedig a minimális szomszédos ablakok száma, amelyeket az arcok érvényesítésekor figyelembe veszünk.

# A felismerett arcokat egy téglalap segítségével kijelöljük
for (x, y, w, h) in faces:
    # Minden egyes arc koordinátáját és méretét (x, y, szélesség, magasság) tartalmazza a 'faces' változó.
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # A felismerett arc köré egy téglalapot rajzolunk. A téglalap bal felső sarka (x, y), a jobb alsó sarka (x + w, y + h).
    # A szín (255, 0, 0) piros, és a téglalap vastagsága 2 pixel.

# Az eredményt megjelenítjük
cv2.imshow("Result", img)
# Az 'img' képet a 'Result' ablakban jelenítjük meg, amely tartalmazza a felismerett arcokat.

# Megvárjuk, hogy a felhasználó nyomjon egy gombot, hogy bezárja az ablakot
cv2.waitKey(0)
# A 'cv2.waitKey(0)' megvárja, hogy a felhasználó nyomjon egy gombot, mielőtt bezárja az ablakot.
