import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)


cv.rectangle(img, (50, 50),  (450, 450), (0, 0, 255), 3)


cv.rectangle(img, (150, 200), (250, 300), (0, 255, 0), -1)


cv.rectangle(img, (300, 150, 50, 100), (255, 0, 255), -1)


cv.imshow("result", img)
cv.waitKey(0);