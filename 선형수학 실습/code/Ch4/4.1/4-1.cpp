#include <opencv2/opencv.hpp>


using namespace cv;


static void on_trackbar( int, void* ){

}

int main()
{

    namedWindow("Canny");


    createTrackbar("low threshold", "Canny", 0, 1000, on_trackbar);
    createTrackbar("high threshold", "Canny", 0, 1000, on_trackbar);


    setTrackbarPos("low threshold", "Canny", 50);
    setTrackbarPos("high threshold", "Canny", 150);



    Mat img_gray;
    img_gray = imread("orange.png", IMREAD_GRAYSCALE);


    while(1)
    {

        int low = getTrackbarPos("low threshold", "Canny");
        int high = getTrackbarPos("high threshold", "Canny");

 
        Mat img_canny;
        Canny(img_gray, img_canny, low, high);


        imshow("Canny", img_canny);


        if (waitKey(1) == 27)
            break;
    }


    destroyAllWindows();

    return 0;
}