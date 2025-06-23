import os
import cv2

# read webcam
webcam = cv2.VideoCapture(0)

# visualize webcam
while True :
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    # Go out of the while true when the user presses the letter q
    # The amount of time  is slightly more complex here than with a simple video 
    if cv2.waitKey(40) & 0xFF == ord("q") :
        break

webcam.release()
cv2.destroyAllWindows()