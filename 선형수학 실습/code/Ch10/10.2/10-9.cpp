#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	
	Mat img;
	img = imread("texture.png");


	Mat img_blur;
	bilateralFilter(img, img_blur, 9,75,75);


	imshow("Original", img);
	imshow("Result", img_blur);

	waitKey(0);
}