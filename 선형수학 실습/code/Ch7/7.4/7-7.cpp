#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{

	int width = 640;
	int height = 480;

	Mat img(height, width, CV_8UC3, Scalar(0, 0, 0));



	circle(img, Point(320, 240), 10, Scalar(0, 255, 0), -1);

	circle(img, Point(320, 240), 100, Scalar(0, 0, 255), 1);


	imshow("result", img);
	waitKey(0);
}