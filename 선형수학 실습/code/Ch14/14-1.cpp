#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
    Mat img_rgb = imread("test.jpg");
    
    Mat img_gray;
    cvtColor(img_rgb, img_gray, COLOR_BGR2GRAY);
    
    Mat img_template = imread("template.jpg", IMREAD_GRAYSCALE);
    int w = img_template.cols;
    int h = img_template.rows;

    Mat result;
    matchTemplate(img_gray, img_template, result, TM_CCOEFF_NORMED);

    double min_val, max_val;
    Point min_loc, max_loc;
    minMaxLoc(result, &min_val, &max_val, &min_loc, &max_loc);

    Point top_left = max_loc;
    Point bottom_right = Point(top_left.x+w, top_left.y+h);


    rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 2);

    imshow("result", img_rgb);
    waitKey(0);

    return 0;
}