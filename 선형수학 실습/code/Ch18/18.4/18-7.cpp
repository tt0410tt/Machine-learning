#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>


using namespace std;
using namespace cv;



void detect(Mat img, CascadeClassifier cascade, vector<Rect> &faces)
{
    cascade.detectMultiScale( img, faces,
        1.1, 4, CASCADE_SCALE_IMAGE,  Size(25, 25) );
}


void draw_rects(Mat img, Rect rect, Scalar color)
{

    rectangle( img, Point(cvRound(rect.x), cvRound(rect.y)),
               Point(cvRound((rect.x + rect.width-1)), 
               cvRound((rect.y + rect.height-1))),  color, 2);
}


void overlayImage(Mat background, Mat foreground,
    Mat &output, Point2i location)
{
    background.copyTo(output);

    for (int y = max(location.y, 0); y < background.rows; ++y)
    {
        int fY = y - location.y; 

        if (fY >= foreground.rows){
            break;
        }

        for (int x = max(location.x, 0); x < background.cols; ++x)
        {
            int fX = x - location.x; 

            if (fX >= foreground.cols){
                break;
            }

            double opacity = ((double)foreground.data[fY * foreground.step 
                    + fX * foreground.channels() + 3]) / 255.;


            for (int c = 0; opacity > 0 && c < output.channels(); ++c){
                unsigned char foregroundPx = 
                    foreground.data[fY * foreground.step + fX * foreground.channels() + c];
                unsigned char backgroundPx = 
                    background.data[y * background.step + x * background.channels() + c];
                output.data[y*output.step + output.channels()*x + c] =
                    backgroundPx * (1. - opacity) + foregroundPx * opacity;
            }
        }
    }
}


int main()
{
    Mat img_frame, img_glasses;
    CascadeClassifier cascade, nestedCascade;

    int glasses_center_width = 320; 
 
    img_glasses = imread("sunglasses.png", IMREAD_UNCHANGED);

    cascade.load("haarcascade_frontalface_alt.xml");
    nestedCascade.load("haarcascade_eye_tree_eyeglasses.xml");  



    VideoCapture cap(0);
    if (!cap.isOpened())
    {
        cout << "카메라를 열 수 없습니다." << endl;
        return -1;
    }


    while(1)
    {

        cap >> img_frame;
        if(img_frame.empty())
        {
            cout << "캡쳐 실패" << endl;
            break;
        }


        Mat result1, result2;
        img_frame.copyTo(result2);



        Mat img_gray;
        cvtColor( img_frame, img_gray, COLOR_BGR2GRAY );
        equalizeHist( img_gray, img_gray );


        double start = 0;
        start = (double)getTickCount();

        

        vector<Rect> faces;
        detect(img_gray, cascade, faces );


        for ( int i = 0; i < faces.size(); i++ )
        {
            Rect r = faces[i];
            Mat img_gray_roi;
            


            img_gray_roi = img_gray( r );


            vector<Rect> subrects;
            detect(img_gray_roi, nestedCascade, subrects );


            if ( subrects.size() == 2){


                Point center1, center2;

                center1.x = cvRound((r.x + subrects[0].x + 
                    subrects[0].width*0.5));
                center1.y = cvRound((r.y + subrects[0].y + 
                    subrects[0].height*0.5));

                center2.x = cvRound((r.x + subrects[1].x + 
                    subrects[1].width*0.5));
                center2.y = cvRound((r.y + subrects[1].y + 
                    subrects[1].height*0.5));

  

                if ( center1.x > center2.x ){
                    Point temp;
                    temp = center1;
                    center1 = center2;
                    center2 = temp;
                }


                int between_center_width = abs(center2.x - center1.x);
                int between_center_height = abs(center2.y - center1.y);

 
                if ( between_center_width > between_center_height){

                    
                    float imgScale = between_center_width/(float)glasses_center_width;
                    
                    int glasses_w, glasses_h;
                    glasses_w = img_glasses.cols * imgScale;
                    glasses_h = img_glasses.rows * imgScale;


                    int offsetX = 160 * imgScale;
                    int offsetY = 160 * imgScale;

              

                    Mat resized_glasses;
                    resize( img_glasses, resized_glasses, 
                        Size( glasses_w, glasses_h), 0, 0 );


                    overlayImage(img_frame, resized_glasses, result1, 
                        Point(center1.x-offsetX, center1.y-offsetY));

                    imshow( "result", result1 );
                }
            }else{

                for ( int j = 0; j < subrects.size(); j++ )
                {
                    Rect nr = subrects[j];

                    draw_rects(result2, Rect(nr.x+r.x, nr.y+r.y, 
                        nr.width, nr.height), Scalar(255, 0, 0));
                }

                draw_rects(result2, r, Scalar(255, 0, 0));

                imshow( "result", result2 );
            }
        }
        
        
        double dt = (double)getTickCount() - start;
        printf( "detection time = %g ms\n", dt*1000/getTickFrequency());

        int key = waitKey(25);
        if( key == 27 )
            break;
    }

    return 0;
}
