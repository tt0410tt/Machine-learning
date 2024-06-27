#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{
    
    int width = 640;
    int height = 640;


    Mat img(height, width, CV_8UC3, Scalar(0, 0, 0));


    Scalar red(0, 0, 255);
    Scalar green(0, 255, 0);
    Scalar yellow(0, 255, 255);

    int thickness = 2; 



    vector<Point> contour;
    contour.push_back(Point(315, 50));
    contour.push_back(Point(570, 240));
    contour.push_back(Point(475, 550));
    contour.push_back(Point(150, 550));
    contour.push_back(Point(50, 240));

    const Point *pts1 = (const cv::Point*) Mat(contour).data;
    int npts1 = Mat(contour).rows;

    polylines(img, &pts1, &npts1, 1, false, red, thickness); 



    contour.clear();
    contour.push_back(Point(315, 160));
    contour.push_back(Point(150, 280));
    contour.push_back(Point(210, 480));
    contour.push_back(Point(420, 480));
    contour.push_back(Point(480, 280));

    const Point *pts2 = (const cv::Point*) Mat(contour).data;
    int npts2 = Mat(contour).rows;

    polylines(img, &pts2, &npts2, 1, true, green, thickness);   


    contour.clear();
    contour.push_back(Point(320, 240));
    contour.push_back(Point(410, 315));
    contour.push_back(Point(380, 415));
    contour.push_back(Point(265, 415));
    contour.push_back(Point(240, 315));

    const Point *pts3 = (const cv::Point*) Mat(contour).data;
    int npts3 = Mat(contour).rows;

    fillPoly(img, &pts3, &npts3, 1, yellow);


    imshow("result", img);
    waitKey(0);


    return 0;
}