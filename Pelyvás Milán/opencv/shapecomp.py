import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# Define a function to get contours and label them
def getContours(img, imgContour):
    # Find contours in the image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)  # Calculate the area of each contour
        if area > 500:
            # Draw contours on the image
            cv2.drawContours(imgContour, [cnt], -1, (0, 255, 0), 3)
            peri = cv2.arcLength(cnt, True)  # Calculate the perimeter of each contour
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # Approximate the shape of the contour
            x, y, w, h = cv2.boundingRect(approx)  # Create a bounding rectangle around the contour
            objCol = len(approx)  # Number of vertices of the contour

            # Determine the type of shape based on the number of vertices
            if objCol == 3:
                objectType = "Triangle"
            elif objCol == 4:
                aspRatio = w / float(h)
                if 0.95 < aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCol == 5:
                objectType = "Pentagon"
            elif objCol > 5:
                objectType = "Circle"
            else:
                objectType = "None"

            # Draw the bounding rectangle and label the shape on the image
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x + (w // 2) - 30, y + (h // 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 0), 2)


# Read the image
img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()  # Create a copy of the original image to draw contours

# Preprocess the image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)  # Apply Gaussian blur to the image
imgCanny = cv2.Canny(imgBlur, 50, 50)  # Detect edges in the image using Canny edge detector

# Get contours and draw them on the image
getContours(imgCanny, imgContour)

# Stack images for display
imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, np.zeros_like(img)]))

# Display the result
cv2.imshow("Stacked Images", imgStack)  # Show the stacked images in a window
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows