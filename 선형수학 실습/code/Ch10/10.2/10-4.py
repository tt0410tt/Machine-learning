import cv2


img = cv2.imread('test.png')
img_blur = cv2.blur(img,(5,5))


cv2.imshow('Original', img)
cv2.imshow('Result', img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()