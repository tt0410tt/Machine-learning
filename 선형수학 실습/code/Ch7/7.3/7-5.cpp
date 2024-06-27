#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
    int width = 640;
    int height = 480;

    Mat img(height, width, CV_8UC3, Scalar(0, 0, 0));


    rectangle(img, Point(50, 50),  Point(450, 450), Scalar(0, 0, 255), 3);

    rectangle(img, Point(150, 200), Point(250, 300), Scalar(0, 255, 0), -1);
   
    rectangle(img, Rect(300, 150, 50, 1000), Scalar(255, 0, 255), -1);

    imshow("result", img);
    waitKey(0);


    return 0;
}