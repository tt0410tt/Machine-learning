#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;


int main()
{

	Mat img_color = imread("house.png", IMREAD_COLOR); 


	Mat img_gray;
	cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


	Mat img_edge;
	blur(img_gray, img_gray, Size(3, 3));
	Canny(img_gray, img_edge, 50, 150, 3);


	imshow("Original", img_gray);
	imshow("Canny Edge", img_edge);
	waitKey(0);


	return 0;
}