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


    bool ret = cap.read(img_frame);
    if (!ret)
    {
        cout << "캡쳐 실패" << endl;
        return -1;
    }



    int codec = VideoWriter::fourcc('M', 'J', 'P', 'G');  
    double fps = 30.0;  

    VideoWriter writer("output.avi", codec, fps, img_frame.size());

    if (!writer.isOpened()) {
        cout << "동영상 파일을 준비할 수 없습니다." << endl;
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

        writer.write(img_frame);


        imshow("Color", img_frame);

        int key = waitKey(1);
        if (key == 27)
            break;
    }

    
    cap.release();
    writer.release();
    return 0;
}