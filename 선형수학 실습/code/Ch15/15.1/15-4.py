import cv2


def nothing(x):
    pass


cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)


img_color = cv2.imread('ball.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)



while(True):
    thre = cv2.getTrackbarPos('threshold', 'Binary')


    ret,img_binary = cv2.threshold(img_gray, thre, 255, 
        cv2.THRESH_BINARY_INV)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    
    cv2.imshow('Result', img_result)
    cv2.imshow('Binary', img_binary)


    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()