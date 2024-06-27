#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


int main()
{

    Mat img_color = imread("test.jpg", IMREAD_COLOR);
    Mat img_gray;
    cvtColor(img_color, img_gray, COLOR_BGR2GRAY); 
    imshow("result", img_gray);
    waitKey(0);


    Mat img_edge;
    Canny(img_gray, img_edge, 50, 150);
    imshow("result", img_edge );
    waitKey(0);


    bitwise_not(img_edge, img_edge);
    imshow("result", img_edge );
    waitKey(0); 


    vector<vector<Point>> contours;
    findContours(img_edge.clone(), contours, RETR_LIST, 
        CHAIN_APPROX_SIMPLE);
    drawContours(img_edge, contours, -1, Scalar(0, 0, 0), 1);
    imshow("result", img_edge );
    waitKey(0); 


    Mat labels, stats, centroids; 
    int nlabels = connectedComponentsWithStats(img_edge, 
        labels, stats, centroids );


    for ( int i=0; i<nlabels; i++ )
    {

        if (i < 2)    continue;


        int area = stats.at<int>(i, CC_STAT_AREA);
        int center_x = centroids.at<double>(i,  0);
        int center_y = centroids.at<double>(i,  1); 
        int left = stats.at<int>(i, CC_STAT_LEFT);
        int top = stats.at<int>(i, CC_STAT_TOP);
        int width = stats.at<int>(i, CC_STAT_WIDTH);
        int height = stats.at<int>(i, CC_STAT_HEIGHT);


        if (area > 50){

            rectangle(img_color, Point(left, top), 
                Point(left + width, top + height),Scalar(0, 0, 255), 1);

            circle(img_color, Point(center_x, center_y), 5, (255, 0, 0), 1);

            putText(img_color, std::to_string(i), Point(left + 20, top + 20), 
                FONT_HERSHEY_SIMPLEX, 1, Scalar(255, 0, 0), 3);
        }
    }

    imshow("result", img_color);
    waitKey(0);
}