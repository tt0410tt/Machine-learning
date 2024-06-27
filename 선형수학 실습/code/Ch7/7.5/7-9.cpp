#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{

	int width = 640;
	int height = 480;

	Mat img(height, width, CV_8UC3, Scalar(0, 0, 0));

  
	line(img, Point(width-1, 0), Point(0, height-1), Scalar(0, 255, 0), 3);
	line(img, Point(0, 0), Point(width-1, height-1), Scalar(0, 0, 255), 3);


	imshow("result", img);
	waitKey(0);

	return 0;
}