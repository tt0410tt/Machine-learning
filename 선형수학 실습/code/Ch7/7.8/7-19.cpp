#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{

    int img_w = 640;
    int img_h = 480;

    Mat img(img_h, img_w, CV_8UC3, Scalar(0, 0, 0));


    Scalar red(0, 0, 255);
    Scalar green(0, 255, 0);
    Scalar white(255, 255, 255);
    Scalar yellow(0, 255, 255);


    int center_x = int(img_w / 2.0);
    int center_y = int(img_h / 2.0);


    int thickness = 2;
    Point location(center_x - 200, center_y - 100);
    int font = FONT_HERSHEY_SCRIPT_SIMPLEX;
    double fontScale = 3.5;
    putText(img, "OpenCV", location, font, fontScale, yellow, thickness);



    location = Point(center_x - 150, center_y + 20);
    font = FONT_ITALIC; 
    fontScale = 2;
    putText(img, "Tutorial", location, font, fontScale, red, thickness);



    location = Point(center_x - 250, center_y + 100);
    font = FONT_HERSHEY_SIMPLEX;  
    fontScale = 1.5;
    putText(img, "webnautes.tistory.com", location, font, fontScale, white, thickness);



    location = Point(center_x - 130, center_y + 150);
    font = FONT_HERSHEY_COMPLEX; 
    fontScale = 1.2;
    putText(img, "webnautes", location, font, fontScale, green, thickness);


    imshow("drawing", img);
    waitKey(0);



    return 0;
}