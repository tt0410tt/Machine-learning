#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	
	Mat img_gray;
	img_gray = imread("test3.png", IMREAD_GRAYSCALE);

  	Mat kernel = getStructuringElement( MORPH_RECT, Size( 11, 11 ) );
  	Mat img_result;
  	morphologyEx(img_gray, img_result, MORPH_CLOSE, kernel);


  	imshow("Input", img_gray);
  	imshow("Result", img_result);
  	waitKey(0);


	return 0;
}