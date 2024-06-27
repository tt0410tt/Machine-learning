#include <opencv2/opencv.hpp>

using namespace cv;


int main()
{
	Mat img_color;
	img_color = imread("cat on laptop.jpg", IMREAD_GRAYSCALE);


	Mat img_copyed1(img_color);
	Mat img_copyed2 = img_color;

	threshold( img_color, img_color, 127, 255, THRESH_BINARY);  


	imshow("img_color", img_color);
	imshow("img_copyed1", img_copyed1);
	imshow("img_copyed2", img_copyed2);
	
	waitKey(0);
}