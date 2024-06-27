import cv2 as cv
import numpy as np


bins = np.arange(256).reshape(256,1)


def draw_histogram(img):

    hist_h = img.shape[0]
    hist_w = 256
    img_histogram1 = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

    
    histSize = 256
    histRange = (0, 256) 
    accumulate = False
    hist_item = cv.calcHist([img], [0], None, [histSize], histRange,
        accumulate=accumulate)

    cv.normalize(hist_item, hist_item, alpha=0, beta=hist_h, 
        norm_type=cv.NORM_MINMAX)

    for i in range(0, histSize):

        cv.line(img_histogram1, ( i, hist_h-int(np.round(hist_item[i])) ),
            ( i, hist_h ), ( 255, 255, 255))


    img_histogram2 = np.zeros((hist_h, hist_w, 1), dtype=np.uint8)

    c_hist = np.zeros(hist_item.shape, dtype=hist_item.dtype)
 
    c_hist[0] = hist_item[0]
    for i in range(1, hist_item.shape[0]):
        c_hist[i] = hist_item[i] + c_hist[i-1]

    cv.normalize(c_hist, c_hist, alpha=0, beta=hist_h, 
        norm_type=cv.NORM_MINMAX)


    for i in range(1, histSize):
        pts = []
        pts.append((i, hist_h - np.round(c_hist[i])))
        pts.append(((i-1), hist_h - np.round(c_hist[i-1])))
        pts= np.array(pts)
        pts = np.int32(pts)
        cv.polylines(img_histogram2, [pts], False, (255,255,255))


    result = cv.hconcat((img_histogram1, img_histogram2))

    return result


img_gray = cv.imread('test.png', cv.IMREAD_GRAYSCALE)

img_histo1 =  draw_histogram(img_gray)
img_result1 = cv.hconcat((img_gray, img_histo1))
cv.imshow('result1', img_result1)


clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe = clahe.apply(img_gray)


img_histo2 =  draw_histogram(img_clahe)
img_result2 = cv.hconcat((img_clahe, img_histo2))
cv.imshow('result2', img_result2)


cv.waitKey(0)
cv.destroyAllWindows()