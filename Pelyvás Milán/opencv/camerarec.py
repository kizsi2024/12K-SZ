import cv2

# Load the pre-trained classifier for frontal face detection
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    success, img = cap.read()
    # Convert the frame to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    # Loop through all the detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow("Result", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

