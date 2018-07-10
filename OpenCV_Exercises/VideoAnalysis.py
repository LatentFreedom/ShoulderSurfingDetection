import cv2
import numpy as np

img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)

# pull bgr color for that specific pixels
px = img[55,55]
# print(px)

img[55,55] = [255,255,255]
# print(px)

# Region of image
#roi = img[0:200, 0,2]

img[100:150,100:150] = (255,255,255)

face = img[100:350,100:250]
img[0:250,0:150] = face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()