#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


int main()
{

	Mat img_frame;


	VideoCapture cap("output.avi");
	if (!cap.isOpened())
	{
		cout << "카메라를 열 수 없습니다." << endl;
		return -1;
	}


	while(1)
	{

		bool ret = cap.read(img_frame);
		if (!ret)
		{
			cout << "동영상 파일 읽기 완료" << endl;
			break;
		}


		imshow("Color", img_frame);

		int key = waitKey(25);
		if (key == 27)
			break;
	}

    
	cap.release();
	return 0;
}