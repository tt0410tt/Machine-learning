#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;

int main()
{
	VideoCapture capture(0);

	while(1)
	{

		Mat img_color;
		bool ret = capture.read(img_color);


		Mat img_result = img_color.clone();
		int width = img_color.cols;
		int height = img_color.rows;
		int center_x = img_color.cols/2.0;
		int center_y = img_color.rows/2.0;


		rectangle(img_result, Point(center_x-100, center_y-100), 
			Point(center_x+100, center_y+100), Scalar(0,0,255), 3);


        Mat img_roi(img_color, Rect(center_x-100, center_y-100, 200, 200));
        Scalar m = mean(img_roi);


		Mat img_mean(img_roi.rows, img_roi.cols, CV_8UC3, Scalar(m[0], m[1], m[2]));


	    imshow("mean", img_mean);
	    imshow("Color", img_result);
	    imshow("roi", img_roi);


		int key = waitKey(1);
		if (key == 27)
			break;
	}

    
	capture.release();
	return 0;
}
