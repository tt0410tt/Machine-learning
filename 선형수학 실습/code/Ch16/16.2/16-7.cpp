#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{
    Mat img_color;
    img_color = imread("test.jpg", IMREAD_COLOR);


    Mat img_gray;
    cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


    Mat img_binary;
    threshold(img_gray, img_binary, 150, 255, THRESH_BINARY_INV);


    Mat kernel = getStructuringElement( MORPH_RECT, Size( 5, 5 ) );
    morphologyEx(img_binary, img_binary, MORPH_CLOSE, kernel);


    vector<vector<Point>> contours;
    findContours(img_binary, contours, RETR_LIST, 
                    CHAIN_APPROX_SIMPLE);


    drawContours(img_color, contours, 0, Scalar(0, 0, 255), 3);
    drawContours(img_color, contours, 1, Scalar(0, 255, 0), 3);


    // 컨투어의 무게 중심을 계산하여 원을 그려줍니다. 
    for( size_t i = 0; i < contours.size(); i++ )
    {
        Moments mu;
        mu = moments( contours[i] );

        int cx = static_cast<float>(mu.m10 / (mu.m00 + 1e-5));
        int cy = static_cast<float>(mu.m01 / (mu.m00 + 1e-5));
        circle(img_color, Point(cx, cy), 15, Scalar(0,255,255), -1);
    }

    imshow("result", img_color);
    waitKey(0);

    return 0;
}
