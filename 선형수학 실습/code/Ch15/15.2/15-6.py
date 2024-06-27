import cv2 as cv


cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)


while(True):

    ret, img_frame = cap.read()
    if ret == False:
        print("캡쳐 실패")
        break;



    img_hsv = cv.cvtColor(img_frame, cv.COLOR_BGR2HSV)


    lower_blue = (120-20, 70, 0)
    upper_blue = (120+20, 255, 255)
    img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)

    img_result = cv.bitwise_and(img_frame, img_frame, mask = img_mask)



    cv.imshow('Color', img_frame)
    cv.imshow('Result', img_result)


    key = cv.waitKey(1) 
    if key == 27:
        break


cap.release()
cv.destroyAllWindows()
