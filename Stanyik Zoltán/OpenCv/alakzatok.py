import cv2  # OpenCV könyvtár importálása képfeldolgozáshoz
import numpy as np  # NumPy könyvtár importálása képadatok kezeléséhez

# Létrehozunk egy üres, fekete képet (512x512 pixel méretű, 3 színcsatornás - BGR)
img = np.zeros((512, 512, 3), np.uint8)

# Az alábbi kódok mind különböző geometriai alakzatokat rajzolnak a képre

# Két nagy téglalap: ház alapja, tető, ablakok
cv2.rectangle(img, (200, 300), (400, 500), (255, 0, 0), 3)  # A ház alapja, kék színnel (BGR)
cv2.rectangle(img, (260, 400), (340, 500), (255, 0, 0), 3)  # Bal ablak a házban
cv2.rectangle(img, (230, 320), (280, 375), (255, 0, 0), 3)  # Kisebb ablak a házban
cv2.rectangle(img, (310, 320), (360, 375), (255, 0, 0), 3)  # Jobb ablak a házban

# Két vonal, amely összeköti a tetőt a ház sarkaival (háromszög alakú tető)
cv2.line(img, (200, 300), (300, 100), (255, 0, 0), 3)  # Bal oldali tetővonal
cv2.line(img, (400, 300), (300, 100), (255, 0, 0), 3)  # Jobb oldali tetővonal

# Felirat hozzáadása a képre
cv2.putText(img, "House", (360, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)  # "House" felirat zöld színnel

# A kép megjelenítése
cv2.imshow("Image", img)

# A program várakozik a felhasználó billentyűnyomására, hogy bezárja a képet
cv2.waitKey(0)
