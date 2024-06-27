#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{

	int width = 640;
	int height = 480;

	Mat img(height, width, CV_8UC3, Scalar(0, 0, 0));


	Point center(int(width/2), int(height/2));

 
	ellipse(img, center, Size(200, 10), 0, 0, 360, Scalar(0, 255, 255), 3 );

	ellipse(img, center, Size(10, 200), 0, 0, 360, Scalar(0, 255, 0), 3 ); 

	ellipse(img, center, Size(200, 200), 0, 0, 360, Scalar(0, 0, 255), 3 );


	imshow("result", img);
	waitKey(0);

	return 0;
}