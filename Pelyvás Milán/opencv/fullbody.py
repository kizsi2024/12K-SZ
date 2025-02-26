import cv2

# Load the pre-trained classifier for full body detection
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_fullbody.xml")

# Read the image from the specified path
img = cv2.imread("Resources/group2.jpeg")
# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect full bodies in the grayscale image
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Loop through all the detected full bodies and draw rectangles around them
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow("Result", img)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
