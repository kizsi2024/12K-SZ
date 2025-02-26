import cv2  # OpenCV könyvtár importálása, amely képfeldolgozást biztosít.
import numpy as np  # NumPy könyvtár importálása, amely segít a tömbök és mátrixok kezelésében.

# Kép összerakó függvény, amely képes több képet összeilleszteni egyetlen képként
def stackImages(scale, imgArray):
    rows = len(imgArray)  # Sorok száma a képek listájában
    cols = len(imgArray[0])  # Oszlopok száma az első sorban
    rowsAvailable = isinstance(imgArray[0], list)  # Ellenőrzi, hogy kétdimenziós listát használunk-e
    width = imgArray[0][0].shape[1]  # Az első kép szélessége
    height = imgArray[0][0].shape[0]  # Az első kép magassága

    if rowsAvailable:
        # Ha kétdimenziós listát használunk, a képeket először át kell méretezni és összegyűjteni.
        for x in range(rows):
            for y in range(cols):
                # Ha a kép mérete megegyezik az első kép méretével, akkor átméretezés nem szükséges
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # Ha a képek mérete eltér, akkor az első kép méretére állítjuk be őket.
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # Ha a képek szürkeárnyalatúak, akkor átalakítjuk őket színes képekké.
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        # Üres kép létrehozása, amelyet később az összes képen alapuló összekapcsolásnál használunk.
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows  # Üres sorok létrehozása.
        hor_con = [imageBlank] * rows
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])  # Sorokba rendezzük a képeket vízszintesen.
        ver = np.vstack(hor)  # A sorokat függőlegesen egyesítjük.

    else:
        # Ha csak egy dimenzióban vannak a képek, akkor vízszintesen egyesítjük őket.
        for x in range(rows):
            # Képek átméretezése az első képhez
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Ha a képek szürkeárnyalatúak, akkor átalakítjuk őket színes képekké.
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        # A képeket vízszintesen egyesítjük.
        hor = np.hstack(imgArray)
        ver = hor  # Ha csak egy sor van, akkor nem kell további függőleges egyesítés.

    return ver  # Az összeillesztett képet visszaadja.

# Kontúr detektáló függvény
def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # Kontúrok keresése
    for cnt in contours:
        area = cv2.contourArea(cnt)  # A kontúr területe
        if area > 500:  # Csak a nagyobb kontúrokat kezeljük
            cv2.drawContours(imgContour, [cnt], -1, (0, 255, 0), 3)  # Kontúr kirajzolása zöld színnel
            peri = cv2.arcLength(cnt, True)  # A kontúr kerületének kiszámítása
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # A kontúrt approximáljuk egy poligonra
            x, y, w, h = cv2.boundingRect(approx)  # Képernyő koordináták és a kontúrhoz tartozó téglalap

            objCol = len(approx)  # Az objektum oldalszáma

            # A felismerett forma típusának meghatározása
            if objCol == 3:
                objectType = "Triangle"  # Háromszög
            elif objCol == 4:
                aspRatio = w / float(h)  # Téglalap-arány kiszámítása
                if 0.95 < aspRatio < 1.05:  # Ha a szélesség és magasság aránya körülbelül 1, akkor négyzet
                    objectType = "Square"
                else:
                    objectType = "Rectangle"  # Ha nem, akkor téglalap
            elif objCol == 5:
                objectType = "Pentagon"  # Ötszög
            elif objCol > 5:
                objectType = "Circle"  # Kör
            else:
                objectType = "None"  # Ha nincs felismerhető forma

            # Téglalap rajzolása a formák köré és a forma típusának hozzáadása
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x + (w // 2) - 30, y + (h // 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

# Kép betöltése
img = cv2.imread("Resources/shapes.png")  # A 'Resources/shapes.png' képet betöltjük
imgContour = img.copy()  # A képet egy másolatba másoljuk, hogy a kontúrokat ezen rajzolhassuk.

# Kép előfeldolgozása
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # A képet szürkeárnyalatossá alakítjuk
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)  # Elmosás a képen, hogy csökkentsük a zajt
imgCanny = cv2.Canny(imgBlur, 50, 50)  # A Canny élesítő algoritmus alkalmazása a képre

# Kontúrok keresése és kirajzolása
getContours(imgCanny, imgContour)  # A kontúrok kinyerése és kirajzolása a képre

# Képek összerakása és megjelenítése
imgStack = stackImages(0.6, ([img, imgGray, imgBlur],  # A képek méretezése és rendezése egy nagy képpé
                             [imgCanny, imgContour, np.zeros_like(img)]))

# Eredmény megjelenítése
cv2.imshow("Stacked Images", imgStack)  # Az összerakott képek megjelenítése
cv2.waitKey(0)  # Várakozás, amíg a felhasználó nem zárja be az ablakot
cv2.destroyAllWindows()  # Az összes ablak bezárása
