#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;

int main()
{

    int width = 640;
    int height = 480;

    Mat img(height, width, CV_8UC3);


    RNG rng(-1);

    int img_h = img.rows;
    int img_w = img.cols;


    for (int y = 0; y < img_h; y++) {

        uchar* pointer_input = img.ptr<uchar>(y);
        for (int x = 0; x < img_w; x++) {

            pointer_input[x * 3 + 0] = rng.uniform(0,256); 
            pointer_input[x * 3 + 1] = rng.uniform(0,256); 
            pointer_input[x * 3 + 2] = rng.uniform(0,256); 
        }
    }



    imshow("drawing", img);
    waitKey(0);
}
