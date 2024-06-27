#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;



int main()
{
    Mat img_color = imread("apple.png", IMREAD_COLOR);


    int height = img_color.rows;
    int width = img_color.cols;


    Mat img_gray(height, width, CV_8UC1);


    for (int y = 0; y < height; y++) {
 
        uchar* pointer_input = img_color.ptr<uchar>(y);
        uchar* pointer_ouput = img_gray.ptr<uchar>(y);
        for (int x = 0; x < width; x++) {
  
            uchar b = pointer_input[x * 3 + 0];
            uchar g = pointer_input[x * 3 + 1];
            uchar r = pointer_input[x * 3 + 2];

            pointer_ouput[x] = r * 0.2126 + g * 0.7152 + b * 0.0722;
        }
    }


    Mat img_result;
    cvtColor(img_gray, img_result, COLOR_GRAY2BGR);


    for (int y = 150; y < 200; y++) {

        uchar* pointer_input = img_result.ptr<uchar>(y);
        for (int x = 200; x < 250; x++) {

            pointer_input[x * 3 + 0] = 0;   
            pointer_input[x * 3 + 1] = 255; 
            pointer_input[x * 3 + 2] = 0;   
        }
    }


    imshow("color", img_color);
    imshow("result", img_result);

    waitKey(0);


    return 0;
}