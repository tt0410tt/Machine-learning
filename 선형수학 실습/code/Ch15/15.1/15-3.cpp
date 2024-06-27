#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


static void on_trackbar( int a, void* ){
}



int main()
{
        namedWindow("Binary"); 
        createTrackbar("threshold1", "Binary", 0, 255, on_trackbar);
        setTrackbarPos("threshold1", "Binary", 127);

 
        Mat img_color = imread( "ball.jpg", IMREAD_COLOR );
        Mat img_gray;
        cvtColor(img_color, img_gray, COLOR_BGR2GRAY);
 

        while(1)
        {
                int thre = getTrackbarPos("threshold1", "Binary");


                Mat img_binary;
                threshold( img_gray, img_binary, thre, 255, 
                        THRESH_BINARY_INV );

                Mat img_result;
                bitwise_and(img_color, img_color, img_result, img_binary);

                imshow("Result", img_result);
                imshow("Binary", img_binary);

                if (waitKey(1) == 27)
                        break;
        }

}