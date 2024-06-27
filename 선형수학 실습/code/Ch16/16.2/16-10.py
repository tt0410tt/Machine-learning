import cv2 as cv
import numpy as np


img_color = cv.imread('test.jpg', cv.IMREAD_COLOR)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)


kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)


contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)


cv.drawContours(img_color, contours, 0, (0, 0, 255), 3)  
cv.drawContours(img_color, contours, 1, (0, 255, 0), 3)  


for contour in contours:

    x, y, w, h = cv.boundingRect(contour)
    cv.rectangle(img_color, (x, y), (x + w, y + h), (255, 255, 0), 3)



    rect = cv.minAreaRect(contour)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img_color, [box], 0, (255, 0, 255), 3)

cv.imshow("result", img_color)
cv.waitKey(0)