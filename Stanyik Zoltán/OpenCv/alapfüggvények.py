import cv2
import numpy as np

# Kép betöltése
img = cv2.imread("Resources/lena.png")

# Szürkeárnyalatossá konvertálás
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gauss-elmosás alkalmazása
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Canny éldetektálás
imgCanny = cv2.Canny(img, 150, 200)

# Morfológiai műveletek
Kernel = np.ones((5, 5), np.uint8)
imgDialation = cv2.dilate(imgCanny, Kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, Kernel, iterations=1)

# Eredmények megjelenítése
cv2.imshow("Eredeti Kép", img)
cv2.imshow("Szürkeárnyalat", imgGray)
cv2.imshow("Elmosott Kép", imgBlur)
cv2.imshow("Canny Élek", imgCanny)
cv2.imshow("Dilatált Kép", imgDialation)
cv2.imshow("Erozióval Kezelt Kép", imgEroded)

cv2.waitKey(0)
