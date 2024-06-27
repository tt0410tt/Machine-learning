import numpy as np
import cv2 as cv


width = 640
height = 640
bpp = 3


img = np.zeros((height, width, bpp), np.uint8)


red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)


thickness = 2 


pts = np.array([[315, 50], [570, 240], [475, 550], 
    [150, 550], [50, 240]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], False, red, thickness)  



pts = np.array([[315, 160], [150, 280], [210, 480], 
    [420, 480], [480, 280]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, green, thickness)  

 
pts = np.array([[320, 245], [410, 315], [380, 415], 
    [265, 415], [240, 315]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], yellow)  



cv.imshow("drawing", img)
cv.waitKey(0);