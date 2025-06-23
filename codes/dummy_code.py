import os
import cv2


# Read Image
img = cv2.imread(os.path.join('..','resources','bird.jpg'))

#Write image
cv2.imwrite(os.path.join('..','resources','bird_out.jpg'), img)

# Visualize image
cv2.imshow('image', img)
cv2.waitKey(0)