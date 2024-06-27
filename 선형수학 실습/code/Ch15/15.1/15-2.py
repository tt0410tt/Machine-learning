import cv2 as cv


 
img_gray = cv.imread("gradation.png", cv.IMREAD_GRAYSCALE)


ret,img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)


cv.imshow("grayscale", img_gray)
cv.imshow("binary", img_binary)

cv.waitKey(0)