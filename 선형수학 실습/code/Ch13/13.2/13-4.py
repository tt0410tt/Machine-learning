import cv2 as cv
import numpy as np

 
src = cv.imread("cat on laptop.jpg", cv.IMREAD_GRAYSCALE)


histSize = 256
histRange = (0, 256) 
accumulate = False

 
gray_hist = cv.calcHist([src], [0], None, [histSize], histRange, 
    accumulate=accumulate)



hist_w = 256
hist_h = 400
histImage = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)


cv.normalize(gray_hist, gray_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)


 
for i in range(0, histSize):

    cv.line(histImage, ( i, hist_h - int(np.round(gray_hist[i])) ),
            ( i, hist_h - 0 ), ( 255, 255, 255), thickness=2)

 
cv.imshow('Source image', src)
cv.imshow('Histogram', histImage)
cv.waitKey()