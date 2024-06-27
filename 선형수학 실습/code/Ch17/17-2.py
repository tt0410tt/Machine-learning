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

 
    kernel = cv.getStructuringElement( cv.MORPH_RECT, ( 11, 11 ) )
    img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)


    img_result = cv.bitwise_and(img_frame, img_frame, mask = img_mask)


    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(img_mask)


    for i in range(nlabels):

        if i < 1:
            continue

        area = stats[i, cv.CC_STAT_AREA]
        center_x = int(centroids[i, 0])
        center_y = int(centroids[i, 1]) 
        left = stats[i, cv.CC_STAT_LEFT]
        top = stats[i, cv.CC_STAT_TOP]
        width = stats[i, cv.CC_STAT_WIDTH]
        height = stats[i, cv.CC_STAT_HEIGHT]

  
 
        if area > 10000:

            cv.rectangle(img_frame, (left, top), (left + width, top + height), 
                    (0, 0, 255), 3)

            cv.circle(img_frame, (center_x, center_y), 5, (255, 0, 0), 3)

            cv.putText(img_frame, str(i), (left + 20, top + 20), 
                    cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)



    cv.imshow('Color', img_frame)
    cv.imshow('Result', img_result)


    key = cv.waitKey(1) 
    if key == 27:
        break


cap.release()
cv.destroyAllWindows()
