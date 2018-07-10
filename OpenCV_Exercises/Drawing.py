import cv2
import numpy as np

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (80,80), (0,255,0), 15)

cv2.rectangle(img, (15,25), (200,150), (255,0,0), -5)
cv2.circle(img, (50,50), 50, (0,0,255), -10)

pts = np.array([[10,5],[50,20],[20,30],[40,20]], np.int32)
#pts = np.reshape((-1,1,2))

cv2.polylines(img,[pts],True, (0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'My 1st Drawing in OpenCV',(0,130),font,1,(200,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()