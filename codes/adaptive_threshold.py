import os
import cv2


# Read Image
img = cv2.imread(os.path.join('..','resources','handwriting.jpg'))
# convert  to Grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Global Thresholding
ret, thresh = cv2.threshold(img_gray, 80, 255,cv2.THRESH_BINARY)
# Adaptive thresholding 
thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30) 
#Two different ways to apply it so adaptive thresh gaussian, and adaptive mean
# Visualize image
cv2.imshow('image', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)