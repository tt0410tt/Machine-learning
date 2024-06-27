#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	
	Mat img_gray;
	img_gray = imread("test.png", IMREAD_GRAYSCALE);

  	Mat kernel = getStructuringElement( MORPH_RECT, Size( 3, 3 ) );
  	Mat img_result;
  	erode(img_gray, img_result, kernel, Point(-1, -1), 1);


  	imshow("Input", img_gray);
  	imshow("Result", img_result);
  	waitKey(0);


	return 0;
}