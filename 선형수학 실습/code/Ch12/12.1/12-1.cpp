#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{

    Mat img_edge, img_result;


    Mat img_src = imread( "test.jpg", IMREAD_GRAYSCALE );

    Canny(img_src, img_edge, 50, 150);
    cvtColor(img_edge, img_result, COLOR_GRAY2BGR);


    vector<Vec2f> lines; 
    HoughLines(img_edge, lines, 1, CV_PI/180, 150 ); 

    for( size_t i = 0; i < lines.size(); i++ )
    {
        float rho = lines[i][0], theta = lines[i][1];
        Point pt1, pt2;
        double a = cos(theta), b = sin(theta);
        double x0 = a*rho, y0 = b*rho;

        pt1.x = cvRound(x0 + 1000*(-b));
        pt1.y = cvRound(y0 + 1000*(a));
        pt2.x = cvRound(x0 - 1000*(-b));
        pt2.y = cvRound(y0 - 1000*(a));
        
        line( img_result, pt1, pt2, Scalar(0,0,255), 3);
    }


    imshow("Source", img_src);
    imshow("Standard Hough Line Transform", img_result);


    waitKey();
    return 0;
}