import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

 
cv.line(img, (width-1, 0), (0, height-1), (0, 255, 0), 3)
cv.line(img, (0, 0), (width-1, height-1), (0, 0, 255), 3) 


cv.imshow("result", img)
cv.waitKey(0);