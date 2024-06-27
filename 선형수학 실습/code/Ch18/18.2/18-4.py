import cv2 as cv
import numpy as np

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, 
      minSize=(30, 30), flags=cv.CASCADE_SCALE_IMAGE)

    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def findFaceAra(img, cascade):
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  gray = cv.equalizeHist(gray)
  rect = detect(gray, cascade)

  return rect

def findMaxArea(contours):
      
  max_area = -1
  max_index = -1


  for i,contour in enumerate(contours):
    area = cv.contourArea(contour)

    x,y,w,h = cv.boundingRect(contour)

    if (w*h)*0.4 > area:
        continue

    if w > h:
        continue

    if area > max_area:
      max_area = area
      max_index = i
  
  if max_area < 10000:
    max_index = -1

  return max_index



def calculateAngle(A, B):

  x1 = A[0]
  y1 = A[1]
  x2 = B[0]
  y2 = B[1]


  dot = x1*x2 + y1*y2      
  det = x1*y2 - y1*x2     
  angle = np.arctan2(det, dot) * 180/np.pi  

  return angle


def distanceBetweenTwoPoints(start, end):
    
  x1,y1 = start
  x2,y2 = end
 
  return int(np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))


def getFingerPosition(max_contour, img_result, debug):
  points1 = []


 
  M = cv.moments(max_contour)

  cx = int(M['m10']/M['m00'])
  cy = int(M['m01']/M['m00'])



  approx = cv.approxPolyDP(max_contour,
    0.02*cv.arcLength(max_contour,True),True)



  hull = cv.convexHull(approx)

 

  for i,point in enumerate(hull):

      if cy > point[0][1]:
        points1.append(tuple(point[0]))


  if debug:
    cv.drawContours(img_result, [hull], 0, (0,255,0), 2)
    for point in points1:
      cv.circle(img_result, tuple(point), 15, (0, 0, 0), -1)


  hull = cv.convexHull(approx, returnPoints=False)
  defects = cv.convexityDefects(approx, hull)

  if defects is None:
    return -1,None


  points2=[]
  for i in range(defects.shape[0]):
    s,e,f,d = defects[i, 0]
    start = tuple(approx[s][0])
    end = tuple(approx[e][0])
    far = tuple(approx[f][0])



    angle = calculateAngle( np.array(end) - np.array(far), 
      np.array(start) - np.array(far))


    if angle > 0 and angle < 45 and d > 10000:

      if start[1] < cy:
        points2.append(start)
      
      if end[1] < cy:
        points2.append(end)

  if debug:
    cv.drawContours(img_result, [approx], 0, (255, 0, 255), 2)
    for point in points2:
      cv.circle(img_result, tuple(point), 20, (0, 255, 0), 5)



  points1 = points1 + points2
  points1 = list(set(points1))



  new_points = []
  for point1 in points1:

    idx = -1
    for j,point2 in enumerate(approx):

      if point1 == tuple(point2[0]):
        idx = j
        break

    if idx == -1:
      continue

    
    if idx-1 >=0:
      pre = np.array(approx[idx-1][0])
    else:
      pre = np.array(approx[len(approx)-1][0])

    if idx+1 <len(approx):
      next = np.array(approx[idx+1][0])
    else:
      next = np.array(approx[0][0])

    angle = calculateAngle( pre-point1, next-point1)
    distance1 = distanceBetweenTwoPoints(pre, point1)
    distance2 = distanceBetweenTwoPoints(next, point1)

    if angle < 45 and distance1 > 40 and distance2 > 40:
      new_points.append(point1)

      

  
  return 1, new_points


def process(img_bgr, img_binary, debug):
    
  img_result = img_bgr.copy()


  contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, 
    cv.CHAIN_APPROX_SIMPLE)

    

  max_idx = findMaxArea(contours)  

  if max_idx == -1:
    return img_result

  if debug:
    cv.drawContours(img_result, [contours[max_idx]], 0, (0, 0, 255), 3)  



  ret, points = getFingerPosition(contours[max_idx], img_result, debug)
  

  if ret > 0 and len(points) > 0:  
    for point in points:
      cv.circle(img_result, point, 20, [ 255, 0, 255], 5)

  return img_result



face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap = cv.VideoCapture('hand.avi')

 
foregroundBackground = cv.createBackgroundSubtractorMOG2(history=500, 
        varThreshold=250, detectShadows=False)



while(1):


    ret, img_frame = cap.read()
    if ret == False:
        break;

    img_frame = cv.flip(img_frame, 1) 
    

    img_blur = cv.GaussianBlur(img_frame, (5,5), 0)
    rect = findFaceAra(img_frame, face_cascade)


    img_gmask = foregroundBackground.apply(img_blur, learningRate=0)


    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img_gmask = cv.morphologyEx(img_gmask, cv.MORPH_CLOSE, kernel, 1)
     

    height,width = img_frame.shape[:2]
    for x1, y1, x2, y2 in rect:
        cv.rectangle(img_gmask, (x1-20, 0), (x2+20, height), (0,0,0), -1)
    

    img_result = process(img_frame, img_gmask, debug=False)


    cv.imshow('mask', img_gmask)
    cv.imshow('result', img_result)


 
    key = cv.waitKey(30) 
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()