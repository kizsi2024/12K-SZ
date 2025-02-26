import cv2  # OpenCV könyvtár importálása, amely képfeldolgozást és számítógépes látást biztosít.

# segít képek betöltésében és megjelenítésében.
# img = cv2.imread("Resources/lena.png")  # Kép betöltése a 'Resources/lena.png' elérési útról.

# cv2.imshow("Lena", img)  # Kép megjelenítése egy ablakban, 'Lena' névvel.
# cv2.waitKey(0)  # Megvárja, hogy a felhasználó nyomjon egy gombot, mielőtt bezárná az ablakot.

# cap = cv2.VideoCapture("Resources/test_video.mp4")  # Videó fájl beolvasása (kommentált kód).

# while True:
# success, img = cap.read()  # Olvassa be a videó képkockáit.
# cv2.imshow("video", img)  # Képkockák megjelenítése egy ablakban.
# if cv2.waitKey(10) & 0XFF == ord("q"):  # Ha a felhasználó megnyomja a 'q' gombot, megszakítja a ciklust.
#   break  # Kilép a ciklusból.

# Kamera beállítások
frameWidth = 640  # A képkockák szélessége.
frameHeight = 480  # A képkockák magassága.

cap = cv2.VideoCapture(0)  # Kamerával való kapcsolatfelvétel. A '0' az alapértelmezett webkamera.
cap.set(3, frameWidth)  # A videó szélességét beállítjuk 640 pixelre.
cap.set(4, frameHeight)  # A videó magasságát beállítjuk 480 pixelre.
cap.set(10, 150)  # A fényerőt 150-ra állítjuk (0 - 255 között).

# Végtelen ciklus, amely folytatódik, amíg a felhasználó le nem állítja.
while True:
    success, img = cap.read()  # Kép beolvasása a kamerából.
    cv2.imshow("Result", img)  # Kép megjelenítése a 'Result' ablakban.

    # Ha a felhasználó megnyomja a 'q' gombot, megszakítja a ciklust.
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break  # Kilép a ciklusból.
