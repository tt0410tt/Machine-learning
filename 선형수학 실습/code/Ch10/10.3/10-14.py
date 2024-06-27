import cv2


img_gray = cv2.imread('house.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", img_gray)

img_gray = cv2.blur(img_gray,(3, 3));
img_canny = cv2.Canny(img_gray, 50, 150)
cv2.imshow("Canny Edge", img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()