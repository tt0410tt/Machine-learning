#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


int main()
{

    Mat img_frame;


    VideoCapture cap(0);
    if (!cap.isOpened())
    {
        cout << "카메라를 열 수 없습니다." << endl;
        return -1;
    }


    while(1)
    {

        bool ret = cap.read(img_frame);
        if (!ret)
        {
            cout << "캡쳐 실패" << endl;
            break;
        }


        Mat img_hsv;
        cvtColor(img_frame, img_hsv, COLOR_BGR2HSV);


        Mat img_mask;
        Vec3b lower_blue = Vec3b(120-20, 70, 0);
        Vec3b upper_blue = Vec3b(120+20, 255, 255);
        inRange(img_hsv, lower_blue, upper_blue, img_mask);


        Mat kernel = getStructuringElement( MORPH_RECT, Size( 11, 11 ) );
        morphologyEx(img_mask, img_mask, MORPH_CLOSE, kernel);


        Mat img_result;
        bitwise_and(img_frame, img_frame, img_result, img_mask);


        Mat labels, stats, centroids; 
        int nlabels = connectedComponentsWithStats(img_mask, 
            labels, stats, centroids );


        for ( int i=0; i<nlabels; i++ )
        {

            if (i < 1)    continue;

            int area = stats.at<int>(i, CC_STAT_AREA);
            int center_x = centroids.at<double>(i,  0);
            int center_y = centroids.at<double>(i,  1); 
            int left = stats.at<int>(i, CC_STAT_LEFT);
            int top = stats.at<int>(i, CC_STAT_TOP);
            int width = stats.at<int>(i, CC_STAT_WIDTH);
            int height = stats.at<int>(i, CC_STAT_HEIGHT);


            if (area > 10000){

                rectangle(img_frame, Point(left, top), 
                    Point(left + width, top + height),Scalar(0, 0, 255), 3);

                circle(img_frame, Point(center_x, center_y), 5, (255, 0, 0), 3);
                
                putText(img_frame, std::to_string(i), Point(left + 20, top + 20), 
                    FONT_HERSHEY_SIMPLEX, 1, Scalar(255, 0, 0), 3);
            }
        }


        imshow("Color", img_frame);
        imshow("Result", img_result);


        int key = waitKey(1);
        if (key == 27)
            break;
    }

    
    cap.release();
    return 0;
}
