import os
import cv2

img= cv2.imread(os.path.join('..','resources','bird.jpg'))
# BGR TO RGB Conversion
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# BGR TO GRAYSCALE CONVERSION
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# BGR TO HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img', img)
cv2.imshow('img_rgb',img_rgb)
cv2.imshow('img_grayscale',img_gray)
cv2.imshow('img_hsv',img_hsv)
cv2.waitKey(0)