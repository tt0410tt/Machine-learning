#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int main()
{
    Mat img_color;
    img_color = imread("hand.png", IMREAD_COLOR);


    Mat img_gray;
    cvtColor(img_color, img_gray, COLOR_BGR2GRAY);


    Mat img_binary;
    threshold(img_gray, img_binary, 150, 255, THRESH_BINARY);


    Mat kernel = getStructuringElement( MORPH_RECT, Size( 5, 5 ) );
    morphologyEx(img_binary, img_binary, MORPH_CLOSE, kernel);


    vector<vector<Point>> contours;
    findContours(img_binary, contours, RETR_LIST, 
                    CHAIN_APPROX_SIMPLE);


    drawContours(img_color, contours, 0, Scalar(255, 0, 0), 3);



    for( size_t i = 0; i < contours.size(); i++ )
    {
 
        vector<Point> hull;
        convexHull(Mat(contours[i]), hull, true);


        vector<vector<Point>> result;
        result.push_back(hull);
        drawContours(img_color, result, -1, Scalar(255, 0, 255), 5); 
    }



    for( size_t i = 0; i < contours.size(); i++ )
    {

        vector<int> hull;
        convexHull(Mat(contours[i]), hull, false);


        vector<Vec4i> defects;
        convexityDefects(contours[i], hull, defects);

        for (int j = 0; j < defects.size(); j++) {
            Point start = contours[i][defects[j][0]];
            Point end = contours[i][defects[j][1]];
            Point far = contours[i][defects[j][2]];
            int d = defects[j][3];


            if ( d > 10000)
            {
                line(img_color, start, end, Scalar(0, 255, 0), 3);
                circle(img_color, far, 5, Scalar(0, 0, 255), -1);  
            }
        }
    }

    imshow("result", img_color);
    waitKey(0);

    return 0;
}
