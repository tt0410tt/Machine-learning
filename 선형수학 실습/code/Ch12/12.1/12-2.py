import math
import cv2 as cv
import numpy as np

    

img_src = cv.imread("test.jpg", cv.IMREAD_GRAYSCALE)

img_edge = cv.Canny(img_src, 50, 150)

img_result = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)
img_result_P = np.copy(img_result)

lines = cv.HoughLines(img_edge, 1, np.pi / 180, 150)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho

        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        
        cv.line(img_result, pt1, pt2, (0,0,255), 3)


cv.imshow("Source", img_src)
cv.imshow("Standard Hough Line Transform", img_result)

cv.waitKey()
