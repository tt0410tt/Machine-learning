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



    int step = 1;


    while(1)
    {

        bool ret = cap.read(img_frame);

        if (!ret)
        {
            cout << "캡쳐 실패" << endl;
            break;
        }

   
        if (step > 1 ){
            cvtColor(img_frame, img_frame, COLOR_BGR2GRAY);

            if (step > 2)
                Canny(img_frame, img_frame, 30, 90);
        }


        imshow("Result", img_frame);



        int key = waitKey(1);

        if (key == 27)  
            break;

        else if (key == 49)  
            step = 1; 
        else if (key == 50)  
            step = 2;
        else if (key == 51)  
            step = 3;
    }

    cap.release();
    return 0;
}
