import math
import cv2 as cv
import numpy as np

    

img_src = cv.imread("test.jpg", cv.IMREAD_GRAYSCALE)

img_edge = cv.Canny(img_src, 50, 150)

img_result = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)



linesP = cv.HoughLinesP(img_edge, 1, np.pi / 180, 50, None, 50, 5)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(img_result, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

cv.imshow("Source", img_src)
cv.imshow("Probabilistic Line Transform", img_result)

cv.waitKey()
