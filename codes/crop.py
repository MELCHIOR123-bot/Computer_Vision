import os
import cv2
img = cv2.imread(os.path.join('..','resources','bird.jpg'))
print(img.shape)
cropped_img = img[30:180, 30:200]
cv2.imshow('img',img)
cv2.imshow('Cropped_img',cropped_img)
cv2.waitKey(0)