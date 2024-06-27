#include <opencv2/opencv.hpp>


using namespace cv;

 

int main()
{
        Mat img_gray = imread( "gradation.png", IMREAD_GRAYSCALE );

 

        Mat img_binary;
        threshold( img_gray, img_binary, 127, 255, 
                THRESH_BINARY );

 
        imshow("garyscale", img_gray);
        imshow("binary", img_binary);

        waitKey(0);

}
