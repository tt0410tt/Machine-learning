import numpy as np
import cv2 as cv


width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)


center = ( int(width/2), int(height/2))


  
cv.ellipse(img, center, (200, 10), 0, 0, 360, (0, 255, 255), 3 ) 
 
cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3 )  
 
cv.ellipse(img, center, (200, 200), 0, 0, 360, (0, 0, 255), 3 ) 


cv.imshow("result", img)
cv.waitKey(0);