import cv2
import numpy as np

# Create a black image with dimensions 512x512 and 3 color channels (BGR)
img = np.zeros((512, 512, 3), np.uint8)
# Uncomment the line below to set a region of the image to blue
# img[200:300, 100:150] = 255, 0, 0

'''
# Draw a green line from (0,0) to (100,300) with thickness 3
cv2.line(img, (0, 0), (100, 300), (0, 255, 0), 3)
# Draw a filled red rectangle from (0,0) to (200,300)
cv2.rectangle(img, (0, 0), (200, 300), (0, 0, 255), cv2.FILLED)
# Draw a circle with center (400,50), radius 30, color yellow, and thickness 5
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# Write "Dr.Goon" on the image at position (300,200) with font size 1 and color dark green
cv2.putText(img, "Dr.Goon", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 100, 0), 3)
'''

# Draw a red rectangle from (300,430) to (200,300) with thickness 4
cv2.rectangle(img, (300, 430), (200, 300), (0, 0, 255), 4)
# Draw a smaller red rectangle from (250,350) to (210,320) with thickness 4
cv2.rectangle(img, (250, 350), (210, 320), (0, 0, 255), 4)
# Draw a rectangle with color (19,69,139) from (285,430) to (260,380) with thickness 4
cv2.rectangle(img, (285, 430), (260, 380), (19, 69, 139), 4)
# Draw a green line from (250,200) to (200,300) with thickness 3
cv2.line(img, (250, 200), (200, 300), (0, 255, 0), 3)
# Draw a green line from (250,200) to (300,300) with thickness 3
cv2.line(img, (250, 200), (300, 300), (0, 255, 0), 3)
# Write "Dr.Goon" on the image at position (300,200) with font size 1 and color dark green
cv2.putText(img, "Dr.Goon", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 100, 0), 3)

# Display the image in a window
cv2.imshow("image", img)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
