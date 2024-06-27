#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	
	Mat img;
	img = imread("median.png");


	Mat img_blur;
	medianBlur(img, img_blur, 5);


	imshow("Original", img);
	imshow("Result", img_blur);

	waitKey(0);
}
