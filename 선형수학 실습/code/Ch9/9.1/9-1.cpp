#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
    Mat img_color;
    img_color = imread("cat.jpg", IMREAD_COLOR);
    imshow("color", img_color);


    int height = img_color.rows;
    int width = img_color.cols;
 
    Mat M = getRotationMatrix2D(Point(width/2.0, height/2.0), 45, 1); 


    Mat img_rotated;
    warpAffine(img_color, img_rotated, M, Size(width, height));

    imshow("rotation", img_rotated);
    waitKey(0);


    return 0;
}