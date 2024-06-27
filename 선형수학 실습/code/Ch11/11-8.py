import cv2
import numpy as np


img_gray = cv2.imread('test3.png', cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( 11, 11 ) )
img_result = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Input", img_gray)
cv2.imshow("Result", img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()