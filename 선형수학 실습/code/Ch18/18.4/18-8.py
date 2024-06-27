import numpy as np
import cv2 as cv
import time


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4, 
        minSize=(25, 25), flags=cv.CASCADE_SCALE_IMAGE)


    if len(rects) == 0:
        return []

    # (x1,y1,width,height) -> (x1,y1,x1+width,y1+height) 
    rects[:,2:] += rects[:,:2]

    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)



def overlayImage(background, foreground, location):

    output = background.copy()


    for y in range(max(location[1],0), background.shape[0]):
        fY = y - location[1]

        if fY >= foreground.shape[0]:
            break

        for x in range(max(location[0],0), background.shape[1]):

            fX = x - location[0]

            if fX >= foreground.shape[1]:
                break;

            opacity = foreground.item(fY, fX, 3) / 255.0


            for c in range(0, 3):
                if opacity <= 0:
                    break;

                foregroundPx = foreground.item(fY, fX, c)
                backgroundPx = background.item(y, x, c)
                output.itemset(y, x, c, backgroundPx*(1-opacity)+foregroundPx*opacity)

    return output



glasses_center_width= 320 


img_glasses = cv.imread("sunglasses.png", cv.IMREAD_UNCHANGED)


cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
nestedCascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


 
cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)


while True:

    ret, img_frame = cap.read()
    if ret == False:
        print("캡쳐 실패")
        break;

    result2 = img_frame.copy()


    img_gray = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)
    img_gray = cv.equalizeHist(img_gray)


    start = time.perf_counter()


    faces = detect(img_gray, cascade)



    for x01, y01, x02, y02 in faces:

        img_gray_roi = img_gray[y01:y02, x01:x02]
        img_roi = img_frame[y01:y02, x01:x02]


        subrects = detect(img_gray_roi, nestedCascade)


        if len(subrects)==2:

            
            x1,y1,x2,y2=subrects[0]
            center1 = (x01+int((x1+x2)*0.5), y01+int((y1+y2)*0.5))         

            x1,y1,x2,y2=subrects[1]
            center2 = (x01+int((x1+x2)*0.5), y01+int((y1+y2)*0.5))


            if center1[0] > center2[0]:
                temp = center1
                center1 = center2
                center2 = temp

          
            between_center_width = abs(center2[0]-center1[0])
            between_center_height = abs(center2[1]-center1[1])


            if between_center_width > between_center_height: 

                imgScale = between_center_width / glasses_center_width
            
                glasses_w = int(img_glasses.shape[1]*imgScale)
                glasses_h = int(img_glasses.shape[0]*imgScale)

                
                offsetX = 160 * imgScale
                offsetY = 160 * imgScale


                resized_glasses = cv.resize(img_glasses, (glasses_w,glasses_h))


                result2 = overlayImage(result2, resized_glasses,
                 (int(center1[0]-offsetX), int(center1[1]-offsetY)) )

        else:

            draw_rects(result2, faces, (0, 255, 0))
            draw_rects(img_roi, subrects, (255, 0, 0))
            result2[y01:y02, x01:x02] = img_roi

    cv.imshow('result', result2)


    dt = time.perf_counter()-start
    print('detection time: %.1f ms' % (dt*1000))


    key = cv.waitKey(25)
    if key == 27:
        break

cv.destroyAllWindows()