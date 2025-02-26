import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread("Resources/lena.png")
# Create a kernel matrix for dilation and erosion
kernel = np.ones((5, 5), np.uint8)

# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply Gaussian blur to the grayscale image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 8)
# Apply Canny edge detection to the image
imgCanny = cv2.Canny(img, 158, 200)
# Dilate the edges detected by the Canny edge detector
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode the dilated edges
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

'''
cv2.imshow("Lena", img)  # Display the original image
cv2.imshow("szurke", imgGray)  # Display the grayscale image
cv2.imshow("augh", imgBlur)  # Display the blurred image
cv2.imshow("tf", imgCanny)  # Display the edges detected by Canny
cv2.imshow("gg", imgDilation)  # Display the dilated edges
'''
# Display the eroded edges
cv2.imshow("ni", imgEroded)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
