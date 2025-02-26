import cv2  # OpenCV könyvtár importálása, amely képfeldolgozást és számítógépes látást biztosít.

# Betöltjük az előre betanított szemüveges szemfelismerő modellt
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_eye_tree_eyeglasses.xml")
# A 'haarcascade_eye_tree_eyeglasses.xml' egy előre betanított modell, amely a szemüveges szemeket felismeri.
# Ez különbözik a sima szemfelismerő modelltől, mivel kifejezetten a szemüvegekkel rendelkező embereket célozza meg.

# Kép betöltése
img = cv2.imread("Resources/szemüveg.jpg")
# Betölti a 'Resources/szemüveg.jpg' képet a változóba.

# A képet szürkeárnyalatossá alakítjuk
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# A képből szürkeárnyalatos képet készítünk, mivel a szemfelismerő algoritmusok jobban működnek szürkeárnyalaton.

# Szemüveges szemek keresése
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
# A 'detectMultiScale' függvénnyel keresünk szemüveges szemeket a szürkeárnyalatos képen.
# Az első paraméter a bemeneti kép, a második paraméter (1.1) a scaling factor, ami segít a méretarányok megtalálásában,
# a harmadik paraméter (4) a minimális szomszédos ablakok száma, amelyeket szem érvényesítésekor figyelembe veszünk.

# A felismerett szemüveges szemek köré téglalapot rajzolunk
for (x, y, w, h) in faces:
    # Minden egyes szemüveges szem koordinátáját és méretét (x, y, szélesség, magasság) tartalmazza a 'faces' változó.
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # A téglalap bal felső sarka (x, y), a jobb alsó sarka (x + w, y + h).
    # A téglalap piros színű, és vastagsága 2 pixel.

# Az eredményt megjelenítjük
cv2.imshow("Result", img)
# Az 'img' képet a 'Result' ablakban jelenítjük meg, amely tartalmazza a felismerett szemüveges szemeket.

# Megvárjuk, hogy a felhasználó nyomjon egy gombot, hogy bezárja az ablakot
cv2.waitKey(0)
# A 'cv2.waitKey(0)' megvárja, hogy a felhasználó nyomjon egy gombot, mielőtt bezárja az ablakot.
