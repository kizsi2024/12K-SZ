import cv2  # OpenCV könyvtár importálása a képfeldolgozáshoz
import numpy as np  # NumPy könyvtár importálása a képadatok kezeléséhez


# A stackImages függvény, amely lehetővé teszi több kép összeillesztését (horizontálisan vagy vertikálisan)
def stackImages(scale, imgArray):
    rows = len(imgArray)  # A képtömb sorainak száma
    cols = len(imgArray[0])  # A képtömb oszlopainak száma
    rowsAvailable = isinstance(imgArray[0], list)  # Ellenőrizzük, hogy a képek listában vannak-e
    width = imgArray[0][0].shape[1]  # Kép szélessége
    height = imgArray[0][0].shape[0]  # Kép magassága

    # Ha több sor és oszlop is van a képtömbben
    if rowsAvailable:
        for x in range(0, rows):  # Végigmegyünk az összes soron
            for y in range(0, cols):  # Végigmegyünk az összes oszlopon
                # Ellenőrizzük, hogy a képek mérete megegyezik-e
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    # Ha igen, akkor átméretezzük őket a kívánt skálázással
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # Ha nem, akkor az első képhez igazítjuk a méretet
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                # Ha a kép szürkeárnyalatos, akkor átalakítjuk színes képpé
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # Üres kép létrehozása a képek közötti hely kitöltésére
        imageBlank = np.zeros((height, width, 3), np.uint8)

        # Képek vízszintes összeillesztése sorok szerint
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])

        # Képek függőleges összeillesztése
        ver = np.vstack(hor)
    else:
        # Ha nincs több sor, akkor csak egy soros összeillesztés történik
        for x in range(0, rows):
            # A képeket átméretezzük a kívánt skálával
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Ha a kép szürkeárnyalatos, akkor átalakítjuk színes képpé
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # Képek vízszintes összeillesztése
        hor = np.hstack(imgArray)
        ver = hor

    # Visszaadjuk a függőlegesen összeillesztett képet
    return ver


# Kép betöltése
img = cv2.imread("Resources/lena.png")
# A kép átalakítása szürkeárnyalatos képpé
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Képek összeillesztése a stackImages függvénnyel
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))

# Képek vízszintes összeillesztése
imgHor = np.hstack((img, img))

# Képek függőleges összeillesztése
imgVer = np.vstack((img, img))

# Kép megjelenítése az összeillesztett képekkel
cv2.imshow("imageStack", imgStack)
# Várakozás, amíg a felhasználó lenyom egy billentyűt
cv2.waitKey(0)
