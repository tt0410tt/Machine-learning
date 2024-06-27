import cv2


img = cv2.imread('test.png')
img_blur = cv2.GaussianBlur(img,(5,5),0)


cv2.imshow('Original', img)
cv2.imshow('Result', img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()