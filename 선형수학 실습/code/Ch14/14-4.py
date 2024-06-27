import cv2 as cv
import numpy as np

  
def notInList(newObject):
    for detectedObject in detectedObjects:
        a = newObject[0]-detectedObject[0]
        b = newObject[1]-detectedObject[1]
        if np.sqrt(a*a+b*b) < 5:
            return False
    return True


detectedObjects=[]

img_rgb = cv.imread('test.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

img_template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)


count = 0
for x in range(res.shape[1]):
    for y in range(res.shape[0]):
        if res[y, x] > 0.9 and notInList((x, y)):
            detectedObjects.append((x, y))
            cv.rectangle(img_rgb, (x, y), (x+w, y+h), [0, 0, 255], 1)
            count = count + 1

print(count)
cv.imshow('result', img_rgb)
cv.waitKey(0)