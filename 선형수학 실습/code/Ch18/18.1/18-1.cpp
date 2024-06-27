#include <opencv2/opencv.hpp>
#include <iostream>  
#include <string> 

using namespace cv;
using namespace std;


void setLabel(Mat& image, string str, vector<Point> contour)
{
    int fontface = FONT_HERSHEY_SIMPLEX;
    double scale = 0.5;
    int thickness = 1;
    int baseline = 0;

    Size text = getTextSize(str, fontface, scale, thickness, &baseline);
    Rect r = boundingRect(contour);

    Point pt(r.x + ((r.width - text.width) / 2), 
        r.y + ((r.height + text.height) / 2));

    rectangle(image, pt + Point(0, baseline), pt + Point(text.width,
        -text.height), CV_RGB(200, 200, 200), FILLED);
    putText(image, str, pt, fontface, scale, CV_RGB(0, 0, 0), thickness, 8);
}



int main(int, char**)
{
    Mat img_color, img_result, img_gray;
 
    img_color = imread("test.png", IMREAD_COLOR);
    cvtColor(img_color, img_gray, COLOR_BGR2GRAY);

    Mat binary_image;
    threshold(img_gray, img_gray, 30, 255, THRESH_BINARY_INV | THRESH_OTSU);

    vector<vector<Point> > contours;
    findContours(img_gray, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);


    vector<Point2f> approx;
    img_result = img_color.clone();

    for (size_t i = 0; i < contours.size(); i++)
    { 
        approxPolyDP(Mat(contours[i]), approx, 
            arcLength(Mat(contours[i]), true)*0.005, true);

        int size = approx.size();
        line(img_result, approx[0], approx[approx.size() - 1], 
            Scalar(0, 255, 0), 3);

        for (int k = 0; k < size - 1; k++)
            line(img_result, approx[k], approx[k + 1], 
                Scalar(0, 255, 0), 3);

        if (isContourConvex(Mat(approx)))
        {
            if (size == 3)
                setLabel(img_result, "triangle", contours[i]); 

            else if (size == 4) 
                setLabel(img_result, "rectangle", contours[i]); 

            else if (size == 5) 
                setLabel(img_result, "pentagon", contours[i]); 

            else if (size == 6) 
                setLabel(img_result, "hexagon", contours[i]);  

            else if (size == 10) 
                setLabel(img_result, "decagon", contours[i]);    
            else 
                setLabel(img_result, to_string(approx.size()), contours[i]);
        }

        else setLabel(img_result, to_string(approx.size()), contours[i]);
        

    }


    imshow("result", img_result);


    waitKey(0);


    return 0;
}