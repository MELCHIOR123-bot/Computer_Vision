# Resizing 
import os
import cv2
img = cv2.imread(os.path.join('..','resources','bird.jpg'))
resized_img = cv2.resize(img, (398, 508))
print(img.shape)
print(resized_img.shape)
cv2.imshow('img',img)
cv2.imshow("Resized_img",resized_img)
cv2.waitKey(0)

