#include <opencv2/opencv.hpp>
#include <iostream>


using namespace std;
using namespace cv;


int main()
{
 
    Mat src = imread("cat on laptop.jpg", IMREAD_GRAYSCALE);


    int histSize = 256;
    float range[] = { 0, 256 }; 
    const float* histRange = { range }; 
    bool uniform = true, accumulate = false;


   
    Mat gray_hist;
    calcHist( &src, 1, 0, Mat(), gray_hist, 1, 
        &histSize, &histRange, uniform, accumulate );

    
    int hist_w = 256, hist_h = 400;
    Mat histImage( hist_h, hist_w, CV_8UC1, Scalar( 0,0,0) );


    normalize(gray_hist, gray_hist, 0, histImage.rows, NORM_MINMAX, -1, Mat() );

 
    for( int i = 0; i < histSize; i++ )
    {
        line( histImage, 
              Point( i, hist_h - cvRound(gray_hist.at<float>(i)) ),
              Point( i, hist_h - 0 ), Scalar( 255, 255, 255), 2);
    }


    imshow("Source image", src );
    imshow("Histogram", histImage );
    waitKey();
    return EXIT_SUCCESS;
}