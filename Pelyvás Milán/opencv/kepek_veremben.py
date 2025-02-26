import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


# Read the image
img = cv2.imread("Resources/lena.png")  # Load the image from the specified path
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

# Stack images for display
imgstack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))  # Stack images using the stackImages function

# Create horizontal and vertical stacks of images
imgHor = np.hstack((img, img))  # Stack images horizontally
imgVer = np.vstack((img, img))  # Stack images vertically

# Display the result
# cv2.imshow("lena", img)  # Display the original image (commented out)
# cv2.imshow("horizontal", imgHor)  # Display the horizontally stacked images (commented out)
# cv2.imshow("ver", imgVer)  # Display the vertically stacked images (commented out)
cv2.imshow("stack", imgstack)  # Display the stacked images using the stackImages function
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows