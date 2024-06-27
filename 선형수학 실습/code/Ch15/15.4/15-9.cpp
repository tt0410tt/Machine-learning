#include <opencv2/opencv.hpp>
#include <iostream>


using namespace std;
using namespace cv;


int main()
{

    Mat img_frame;
    


    VideoCapture cap("output.avi");

    
    Ptr<BackgroundSubtractorMOG2> foregroundBackground = 
                    createBackgroundSubtractorMOG2(500, 250, false);

    while(1)
    {

        bool ret = cap.read(img_frame);
        if (!ret)
        {
            cout << "캡쳐 실패" << endl;
            break;
        }


        GaussianBlur(img_frame, img_frame, Size(5, 5), 0);

        Mat img_mask;
        foregroundBackground->apply(img_frame, img_mask, 0);

        Mat kernel = getStructuringElement(MORPH_ELLIPSE, Size(5, 5));
        morphologyEx(img_mask, img_mask, MORPH_CLOSE, kernel);


        imshow("mask", img_mask);
        imshow("Color", img_frame);

        int key = waitKey(30); 
        if (key == 27)
            break;
    }


    cap.release();
    return 0;
}
