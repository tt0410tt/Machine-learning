#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
    Mat img_color;
    img_color = imread("cat.jpg");
    imshow("original", img_color);


    int height = img_color.rows;
    int width = img_color.cols;


    Mat M(2,3,CV_64F,Scalar(0.0));

    M.at<double>(0,0) = 1;
    M.at<double>(1,1) = 1;
    M.at<double>(0,2) = 100;
    M.at<double>(1,2) = 50;


    Mat img_translation;
    warpAffine(img_color, img_translation, M, Size(width, height));

    imshow("translation", img_translation);
    waitKey(0);

}