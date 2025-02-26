import cv2  # OpenCV könyvtár importálása, amely képfeldolgozást és számítógépes látást biztosít.
import numpy as np  # NumPy könyvtár importálása, amely a tömbökkel és matematikai műveletekkel dolgozik.


# Üres függvény, amelyet a trackbarokhoz használunk
def empty(a):
    pass


# Képstackelés: Több képet egyesítünk egy nagy képbe (horizontálisan és vertikálisan)
def stackImages(scale, imgArray):
    rows = len(imgArray)  # A sorok száma
    cols = len(imgArray[0])  # Az oszlopok száma
    rowsAvailable = isinstance(imgArray[0], list)  # Ellenőrizzük, hogy van-e több sor
    width = imgArray[0][0].shape[1]  # Képek szélessége
    height = imgArray[0][0].shape[0]  # Képek magassága

    # Ha több sor van, akkor minden képet át kell méretezni és egyesíteni
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # A képek méretének igazítása
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                # Ha a kép szürkeárnyalatos, színesképpé alakítjuk
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # Üres kép létrehozása
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        # Sorok egyesítése
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Sorok vertikális egyesítése
        ver = np.vstack(hor)
    else:
        # Ha nincs több sor, csak egyszerűen egyesítjük a képeket vízszintesen
        for x in range(0, rows):
            # A képek méretének igazítása
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Ha a kép szürkeárnyalatos, színesképpé alakítjuk
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Képek vízszintes egyesítése
        hor = np.hstack(imgArray)
        ver = hor
    return ver  # Visszaadjuk az egyesített képet


# Trackbarok létrehozása a színskála szabályozásához
cv2.namedWindow("Trackbars")  # Létrehozzuk a trackbar ablakot
cv2.resizeWindow("Trackbars", 640, 240)  # Beállítjuk az ablak méretét
cv2.createTrackbar("Hue min", "Trackbars", 0, 179, empty)  # Hue minimum beállítása
cv2.createTrackbar("Hue max", "Trackbars", 24, 179, empty)  # Hue maximum beállítása
cv2.createTrackbar("Sat min", "Trackbars", 18, 255, empty)  # Saturation minimum beállítása
cv2.createTrackbar("Sat max", "Trackbars", 255, 255, empty)  # Saturation maximum beállítása
cv2.createTrackbar("Val min", "Trackbars", 0, 255, empty)  # Value minimum beállítása
cv2.createTrackbar("Val max", "Trackbars", 255, 255, empty)  # Value maximum beállítása

while True:
    # Kép betöltése
    img = cv2.imread("Resources/lambo.PNG")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # A képet HSV színmodellre alakítjuk

    # A trackbarok értékeinek lekérése
    h_min = cv2.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val max", "Trackbars")

    # A színskála alsó és felső határainak meghatározása
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # A kép maszkja, ami az adott színskála alapján szűri a képet
    mask = cv2.inRange(imgHSV, lower, upper)
    # A maszkot alkalmazzuk az eredeti képre
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Képek összefűzése a megjelenítéshez
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))

    # Az eredményt megjelenítjük
    cv2.imshow("Stacked Images", imgStack)

    # A következő iterációig várunk egy billentyűnyomásra
    cv2.waitKey(1)
