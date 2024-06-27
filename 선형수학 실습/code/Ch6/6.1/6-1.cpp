#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;


int main()
{
    Mat img1, img2;

    double alpha = 0.0;
    double beta = 1.0;

    while(alpha <= 1.0){

        img1 = imread("beach.png", IMREAD_COLOR);
        img2 = imread("cat.png", IMREAD_COLOR);

 
        Mat dst;
        addWeighted(img1, alpha, img2, beta, 0, dst);


        cout << alpha << " " << beta << endl;


        imshow("dst", dst);
        waitKey(0);

  
        alpha = alpha + 0.1;
        beta = beta - 0.1;
    }

    return 0;
}