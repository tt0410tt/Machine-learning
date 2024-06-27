#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	
	Mat img_gray;
	img_gray = imread("test2.png", IMREAD_GRAYSCALE);

  	Mat kernel = getStructuringElement( MORPH_RECT, Size( 3, 3 ) );
  	Mat img_result;
  	morphologyEx(img_gray, img_result, MORPH_OPEN, kernel);


  	imshow("Input", img_gray);
  	imshow("Result", img_result);
  	waitKey(0);


	return 0;
}