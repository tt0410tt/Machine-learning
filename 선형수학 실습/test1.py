import cv2
import numpy as np

print("4번문항 1번")
print("5번문항 2번")
print("6번문항 3번")
img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 못 불러옴")
    exit(1)

cv2.imwrite("test2.jpg", img_color)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow("img_color", img_color)
cv2.imshow("img_gray", img_gray)
img_sub=img_gray[0:101,0:101]
cv2.imshow("ROI",img_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()
