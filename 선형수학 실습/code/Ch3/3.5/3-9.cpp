#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;


int main()
{
	Mat img_color;
	img_color = imread("color.png", IMREAD_COLOR);

 
	Mat img_channels[3];
	split(img_color, img_channels);



	vector<Mat> channels;
	channels.push_back(img_channels[2]); 
	channels.push_back(img_channels[1]); 
	channels.push_back(img_channels[0]); 

	Mat img_result;
	merge(channels, img_result);


	imshow("Color", img_result);
	imshow("B", img_channels[0]);
	imshow("G", img_channels[1]);
	imshow("R", img_channels[2]);

	waitKey(0);
	return 0;
}
