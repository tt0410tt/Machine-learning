import cv2 as cv
import numpy as np


img_color = cv.imread('hand.png', cv.IMREAD_COLOR)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)


ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)


kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)


contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)


cv.drawContours(img_color, contours, 0, (255, 0, 0), 3)  


for contour in contours:

    hull = cv.convexHull(contour)

    cv.drawContours(img_color, [hull], 0, (255, 0, 255), 7)


for contour in contours:

    hull = cv.convexHull(contour, returnPoints = False)


    defects = cv.convexityDefects(contour, hull)

    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])


        if d > 10000:
            cv.line(img_color, start, end, (0, 255, 0), 3)
            cv.circle(img_color, far, 5, (0, 0, 255), -1)


cv.imshow("result", img_color)
cv.waitKey(0)