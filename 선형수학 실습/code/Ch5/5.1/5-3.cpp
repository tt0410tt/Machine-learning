#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


static void on_trackbar( int, void* ){

}


int main()
{
	Mat img_color;
	img_color = imread("red ball.png", IMREAD_COLOR);
	if (img_color.empty())
	{
		cout << "이미지 파일을 읽을 수 없습니다." << endl;
		return -1;
	}


	Mat img_gray;
	cvtColor(img_color, img_gray, COLOR_BGR2GRAY);
	imshow("Grayscale", img_gray);
	
 
	namedWindow("Binary");
	createTrackbar("threshold", "Binary", 0, 255, on_trackbar);
	setTrackbarPos("threshold", "Binary", 127);
	

 
	while(1)
	{
 
		int thresh = getTrackbarPos("threshold", "Binary");

		Mat img_binary;
		threshold(img_gray, img_binary, thresh, 255, THRESH_BINARY_INV);


		imshow("Binary", img_binary);

        if (waitKey(1) == 27)
            break;
	}

}