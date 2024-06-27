import cv2 as cv
import numpy as np
import os


cap = cv.VideoCapture('output.avi')


foregroundBackground = cv.createBackgroundSubtractorMOG2(history=500, 
        varThreshold=250, detectShadows=False)


while(1):

    ret, img_frame = cap.read()
    if ret == False:
        break;
    
    blur = cv.GaussianBlur(img_frame, (5,5), 0)

    img_mask = foregroundBackground.apply(blur, learningRate=0)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)
    

    cv.imshow('mask', img_mask)
    cv.imshow('color', img_frame)

 
    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()