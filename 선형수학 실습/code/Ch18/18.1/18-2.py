import cv2 as cv


def setLabel(image, str, contour):

    (text_width, text_height), baseline = cv.getTextSize(str, 
        cv.FONT_HERSHEY_SIMPLEX, 0.7, 1)

    x,y,width,height = cv.boundingRect(contour)

    pt_x = x + int((width-text_width)/2)
    pt_y = y + int((height + text_height)/2)

    cv.rectangle(image, (pt_x, pt_y+baseline), 
        (pt_x+text_width, pt_y-text_height), (200,200,200), cv.FILLED)
    cv.putText(image, str, (pt_x, pt_y), cv.FONT_HERSHEY_SIMPLEX, 
        0.7, (0,0,0), 1, 8)


img_color = cv.imread('test.png', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)


ret,img_binary = cv.threshold(img_gray, 50, 255, 
    cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
cv.imshow('binary', img_binary)


contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon = 0.005 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)


    size = len(approx)
    cv.line(img_color, tuple(approx[0][0]), tuple(approx[size-1][0]), 
        (0, 255, 0), 3)
    for k in range(size-1):
        cv.line(img_color, tuple(approx[k][0]), tuple(approx[k+1][0]), 
            (0, 255, 0), 3)


    if cv.isContourConvex(approx):
        if size == 3:
            setLabel(img_color, "triangle", cnt)
        elif size == 4:
            setLabel(img_color, "rectangle", cnt)
        elif size == 5:
            setLabel(img_color, "pentagon", cnt)
        elif size == 6:
            setLabel(img_color, "hexagon", cnt)
        elif size == 8:
            setLabel(img_color, "octagon", cnt)
        elif size == 10:
            setLabel(img_color, "decagon", cnt)
        else:
            setLabel(img_color, str(size), cnt)
    else:
        setLabel(img_color, str(size), cnt)


cv.imshow('result', img_color)
cv.waitKey(0)