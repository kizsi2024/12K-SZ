import cv2

# Commented out code for displaying an image and playing a video
'''
img = cv2.imread("Resources/lena.png")  # Read the image from the specified path
cv2.imshow("Lena", img)  # Display the image in a window
cv2.waitKey()  # Wait for a key press to close the window

cap = cv2.VideoCapture("Resources/test_video.mp4")  # Capture video from the specified file

while True:
    success, img = cap.read()  # Read frames from the video
    cv2.imshow("Video", img)  # Display the video frames
    if cv2.waitKey(10) & 0xFF == ord("q"):  # Break the loop if 'q' key is pressed
        break
'''

# Set the frame width and height for the webcam capture
framewidth = 640
frameheight = 400

# Capture video from the webcam (usually indexed as 0)
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)  # Set the frame width
cap.set(4, frameheight)  # Set the frame height
cap.set(10, 150)  # Set the brightness (property ID 10)

while True:
    success, img = cap.read()  # Read frames from the webcam
    cv2.imshow("Result", img)  # Display the webcam frames
    if cv2.waitKey(1) & 0xFF == ord("q"):  # Break the loop if 'q' key is pressed
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
