import cv2


img = cv2.imread('median.png')
median = cv2.medianBlur(img, 5)

cv2.imshow('Original', img)
cv2.imshow('Result', median)

cv2.waitKey(0)
cv2.destroyAllWindows()