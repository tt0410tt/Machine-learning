import cv2 as cv
import numpy as np
from random import randint



width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)



img_h = img.shape[0]
img_w = img.shape[1]



for y in range(img_h):
    for x in range(img_w):

        img.itemset(y, x, 0, randint(0, 255))  
        img.itemset(y, x, 1, randint(0, 255))  
        img.itemset(y, x, 2, randint(0, 255))  


cv.imshow("drawing", img)

cv.waitKey(0);
