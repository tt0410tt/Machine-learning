#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{
    Mat img_color;
    img_color = imread("square.png", IMREAD_COLOR);


    Mat img_gray;
    cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


    Mat img_binary;
    threshold(img_gray, img_binary, 150, 255, THRESH_BINARY);


    Mat kernel = getStructuringElement( MORPH_RECT, Size( 5, 5 ) );
    morphologyEx(img_binary, img_binary, MORPH_CLOSE, kernel);


    vector<vector<Point>> contours;
    findContours(img_binary, contours, RETR_LIST, 
                    CHAIN_APPROX_SIMPLE);


    drawContours(img_color, contours, 0, Scalar(0, 0, 255), 3);


    vector<Point> approx;

    for( size_t i = 0; i < contours.size(); i++ )
    {
        double epsilon = 0.03 * arcLength(contours[i], true);
        approxPolyDP(contours[i], approx, epsilon, true);

        vector<vector<Point>> result;
        result.push_back(approx);
        drawContours(img_color, result, -1, Scalar(0, 255, 0), 3);
    }

    imshow("result", img_color);
    waitKey(0);

    return 0;
}
