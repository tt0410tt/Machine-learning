#include <opencv2/opencv.hpp>


using namespace cv;

int main()
{
	Mat img_color;
	img_color = imread("box.png", IMREAD_COLOR);
	

	Mat img_gray;
	cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


	Mat img_sobel_x;
	Sobel(img_gray, img_sobel_x, CV_64F, 1, 0, 3);
	convertScaleAbs(img_sobel_x, img_sobel_x);


	Mat img_sobel_y;
	Sobel(img_gray, img_sobel_y, CV_64F, 0, 1, 3);
	convertScaleAbs(img_sobel_y, img_sobel_y);


	Mat img_sobel;
	addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0, img_sobel);


	imshow("Sobel X", img_sobel_x);
	imshow("Sobel Y", img_sobel_y);
	imshow("Sobel", img_sobel);

	waitKey(0);

	return 0;
}