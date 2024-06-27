#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{

    Mat img_edge, img_result;


    Mat src = imread( "test.jpg", IMREAD_GRAYSCALE );

    Canny(src, img_edge, 50, 150);
    cvtColor(img_edge, img_result, COLOR_GRAY2BGR);


    vector<Vec4i> linesP; 
    HoughLinesP(img_edge, linesP, 1, CV_PI/180, 50, 50, 5 ); 

    for( size_t i = 0; i < linesP.size(); i++ )
    {
        Vec4i l = linesP[i];
        line( img_result, Point(l[0], l[1]), Point(l[2], l[3]), Scalar(0,0,255), 3, LINE_AA);
    }

    imshow("Source", src);
    imshow("Probabilistic Line Transform", img_result);

    waitKey();
    return 0;
}