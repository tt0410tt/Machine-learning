#include <opencv2/opencv.hpp>

using namespace cv;


int main()
{
	Mat img_color;
	img_color = imread("cat on laptop.jpg", IMREAD_GRAYSCALE);


	Mat img_sub1(img_color, Rect(20, 20, 150, 150));
	Mat img_sub2 = img_color(Range(100, 150), Range::all());

	threshold( img_sub1, img_sub1, 127, 255, THRESH_BINARY);  


	imshow("img_color", img_color);
	imshow("img_sub1", img_sub1);
	imshow("img_sub2", img_sub2);
	
	waitKey(0);
}