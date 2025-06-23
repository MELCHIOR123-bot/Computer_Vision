import os
import cv2


# Read Image
image_path = os.path.join('..','resources','bird.jpg')
img = cv2.imread(image_path)

#Write image
cv2.imwrite(os.path.join('..','resources','bird_out.jpg'), img)

# Visualize image
cv2.imshow('image', img)
cv2.waitKey(5000)