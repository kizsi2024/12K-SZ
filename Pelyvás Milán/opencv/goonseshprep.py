import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread("Resources/cards.jpg")

# Set the desired output width and height
width, height = 250, 350

# Define points on the original image for the first perspective transform
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# Define points on the output image for the first perspective transform
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# Compute the perspective transform matrix for the first set of points
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# Apply the perspective transform to the image
imgoutput = cv2.warpPerspective(img, matrix, (width, height))

# Define points on the original image for the second perspective transform
ptsa = np.float32([[276, 130], [450, 130], [274, 350], [454, 372]])
# Define points on the output image for the second perspective transform
ptsb = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# Compute the perspective transform matrix for the second set of points
matrix2 = cv2.getPerspectiveTransform(ptsa, ptsb)
# Apply the perspective transform to the image
imgoutput2 = cv2.warpPerspective(img, matrix2, (width, height))

# Display the original image
cv2.imshow("image", img)
# Display the first perspective-transformed image
cv2.imshow("output", imgoutput)
# Display the second perspective-transformed image
cv2.imshow("output2", imgoutput2)
cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()  # Close all OpenCV windows
