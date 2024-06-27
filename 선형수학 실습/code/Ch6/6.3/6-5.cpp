#include <opencv2/opencv.hpp>


using namespace cv;


int main()
{ 
	Mat img_logo, img_background;
	img_logo = imread("logo.png", IMREAD_COLOR);
	img_background = imread("background.png", IMREAD_COLOR);


	Mat img_gray;
	cvtColor(img_logo, img_gray, COLOR_BGR2GRAY);

	Mat img_mask;
	threshold(img_gray, img_mask, 200, 255, THRESH_BINARY);


	Mat img_mask_inv;
	bitwise_not(img_mask, img_mask_inv);


	int height = img_logo.rows;
	int width = img_logo.cols;

	Mat img_roi(img_background, Rect(0, 0, width, height));


	Mat img1, img2;
	bitwise_and(img_logo, img_logo, img1, img_mask_inv);
	bitwise_and(img_roi, img_roi, img2, img_mask);


	Mat dst;
	add(img1, img2, dst);


	dst.copyTo(img_background(Rect(0, 0, width, height)));


	imshow("background", img_background);
	// imshow("logo", img_logo);
	// imshow("img_mask_inv", img_mask_inv);
	// imshow("img_mask", img_mask);
	// imshow("img1", img1);
	// imshow("img2", img2);
	// imshow("dst", dst);
	waitKey(0);
}