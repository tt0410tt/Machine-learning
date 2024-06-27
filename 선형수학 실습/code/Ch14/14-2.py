import cv2 as cv
import numpy as np


img_rgb = cv.imread('test.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

img_template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)


cv.rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 2)

cv.imshow('result', img_rgb)
cv.waitKey(0)