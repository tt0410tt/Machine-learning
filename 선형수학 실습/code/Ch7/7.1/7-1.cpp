#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;

int main()
{

    int width = 640;
    int height = 480;

    Mat img(height, width, CV_8UC3);


    int img_h = img.rows;
    int img_w = img.cols;
    int img_bpp = img.channels();

    cout << img_h << " " << img_w << " " << img_bpp << endl;


    circle(img, Point(100, 300), 10, Scalar(0, 255, 255), -1);


    imshow("drawing", img);
    waitKey(0);
}
