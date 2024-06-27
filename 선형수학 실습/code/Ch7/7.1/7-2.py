import numpy as np
import cv2 as cv



width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

 
img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)


cv.circle(img, (100, 300), 10, (0, 255, 255), -1)

cv.imshow("drawing", img)

cv.waitKey(0);
