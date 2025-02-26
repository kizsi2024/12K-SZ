import cv2
import numpy as np

# Betöltjük a képet
img = cv2.imread("Resources/lambo.PNG")
print(img.shape)  # Kiírjuk a kép eredeti méreteit

# Átméretezzük a képet 1000x500 pixelre
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)  # Kiírjuk az átméretezett kép méreteit

# Kivágunk egy részt a képből: az első 200 sor és a 200-500. oszlopok
imgCropped = img[0:200, 200:500]

# Kivágunk egy másik részt a képből: a 40-400. sorok és a 50-500. oszlopok
imgCropped2 = img[40:400, 50:500]

# Megjelenítjük az eredeti képet
cv2.imshow("Image", img)

# Megjelenítjük az átméretezett képet
cv2.imshow("Image Resize", imgResize)

# Megjelenítjük az első kivágott részt
cv2.imshow("Image Cropped", imgCropped)

# Megjelenítjük a második kivágott részt
cv2.imshow("Image Cropped2", imgCropped2)

# Várunk egy billentyűleütésre, majd bezárjuk az ablakokat
cv2.waitKey(0)
cv2.destroyAllWindows()
