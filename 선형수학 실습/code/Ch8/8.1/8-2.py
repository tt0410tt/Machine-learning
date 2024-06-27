import cv2 as cv



mouse_is_pressing = False
start_x, start_y, end_x, end_y = 0,0,0,0
step = 0


def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp



def mouse_callback(event, x, y, flags, param):

    global step, start_x, end_x, start_y, end_y, mouse_is_pressing

    if event == cv.EVENT_LBUTTONDOWN:
        step = 1

        mouse_is_pressing = True
        start_x = x
        start_y = y

    elif event == cv.EVENT_MOUSEMOVE:


        if mouse_is_pressing:

            end_x = x
            end_y = y

            step = 2

    elif event == cv.EVENT_LBUTTONUP:

        mouse_is_pressing = False

        end_x = x
        end_y = y
        
        step = 3




cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(-1)

cv.namedWindow("Color")
cv.setMouseCallback("Color", mouse_callback)


while True:

    ret, img_color = cap.read()
    if ret == False:
        print("캡쳐 실패")
        break;


    if step == 1:
        cv.circle(img_color, (start_x, start_y), 
            10, (0, 255, 0), -1);

    elif step == 2:

        cv.rectangle(img_color, (start_x, start_y), (end_x, end_y), 
            (0, 255, 0), 3);

    elif step == 3:
        if start_x > end_x:
            swap(start_x, end_x)
            swap(start_y, end_y)


        ROI = img_color[start_y:end_y, start_x:end_x]

 
        ROI = cv.cvtColor(ROI, cv.COLOR_BGR2GRAY)
        ROI = cv.Canny(ROI, 150, 50)
        ROI = cv.cvtColor(ROI, cv.COLOR_GRAY2BGR)


        img_color[start_y:end_y, start_x:end_x] = ROI
 

    cv.imshow("Color", img_color);


    if cv.waitKey(25) > 0:
        break;

