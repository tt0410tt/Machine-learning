import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)


cv.circle(img, (320, 240), 10, (0, 255, 0), -1)
  
cv.circle(img, (320, 240), 100, (0, 0, 255), 1)


cv.imshow("result", img)
cv.waitKey(0);