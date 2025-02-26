import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread("Resources/lambo.png")
print(img.shape)  # Print the dimensions of the image (height, width, channels)

# Resize the image (commented out)
# imgresize = cv2.resize(img, (1000, 500))

# Crop a region of the image from (0,200) to (200,500)
imgcropped = img[0:200, 200:500]
# Crop another region of the image from (40,400) to (50,500)
imgcropped2 = img[40:400, 50:500]

# Display the original image
cv2.imshow("car", img)
# Display the first cropped image (commented out)
# cv2.imshow("l", imgcropped)
# Display the second cropped image
cv2.imshow("ll", imgcropped2)
# Display the resized image (commented out)
# cv2.imshow("a", imgresize)

cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()  # Close all OpenCV windows
