#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{
	Mat img_color;
	img_color = imread("green.png", IMREAD_COLOR);


	int height = img_color.rows;
	int width = img_color.cols;

	int center_x = (int)width*0.5;
	int center_y = (int)height*0.5;



	Mat img_roi;
	img_roi = img_color(Rect(center_x-100,center_y-100,200,200)).clone();


	Mat img_gray; 
	cvtColor(img_roi, img_gray, COLOR_BGR2GRAY);
	Mat img_edge;
	Canny(img_gray, img_edge, 100, 300);

	cvtColor(img_edge, img_edge, COLOR_GRAY2BGR);

	img_edge.copyTo(img_color(Rect(center_x-100,center_y-100,200,200)));


	imshow("COLOR", img_color);
	imshow("ROI", img_roi);
	waitKey(0);

	destroyAllWindows();
}