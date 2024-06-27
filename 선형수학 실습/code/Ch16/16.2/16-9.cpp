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



    for( size_t i = 0; i < contours.size(); i++ )
    {

        Rect rect = boundingRect(contours[i]);
        rectangle(img_color, rect, Scalar(255, 255, 0), 3);


        Point2f points[4];
        RotatedRect box = minAreaRect(contours[i]);
        box.points(points);

        for( int j = 0; j < 4; j++ )
            line(img_color, points[j], points[(j+1)%4], 
                Scalar(255, 0, 255), 3);
    }

    imshow("result", img_color);
    waitKey(0);

    return 0;
}
