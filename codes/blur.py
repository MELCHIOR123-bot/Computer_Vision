import os
import cv2

img= cv2.imread(os.path.join('..','resources','African.jpg'))
k_size = 7
# Classical Blur
img_blur = cv2.blur(img, (k_size, k_size))
# Gaussian Blur
img_gblur = cv2.GaussianBlur(img, (k_size,k_size),3)
# Median Blur
img_mblur = cv2.medianBlur(img,k_size)
cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gblur',img_gblur)
cv2.imshow('img_mblur',img_mblur)

cv2.waitKey(0)