import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)


center = (int(width/2), int(height/2))

 
cv.ellipse(img, center, (100, 100), 0, 0, 90,  (0, 0, 255), 3 ) 


cv.imshow("result", img)
cv.waitKey(0);