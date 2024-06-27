#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


int main()
{
	Mat img_color;


 
	img_color = imread("ball.png", IMREAD_COLOR);
	
	if (img_color.empty())
	{
		cout << "이미지 파일을 읽을 수 없습니다." << endl;
		return -1;
	}


	Mat img_gray;
	cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


	Mat img_canny;
	Canny(img_gray, img_canny, 90, 180);


	vector<Mat> matrices = { img_gray, img_canny};

	Mat img_result;
 
	hconcat( matrices, img_result );

	imshow("Result", img_result);

	waitKey(0);
	destroyAllWindows();
}
