#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


int step = 0;
bool mouse_is_pressing = false;
Point2f g_points[4];



double distanceBetweenTwoPoints(Point2f start, Point2f end)
{
  float x1 = start.x;
  float y1 = start.y;
  float x2 = end.x;
  float y2 = end.y;  
 
  return (float)(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)));
}



void mouse_callback(int event, int x, int y, int flags, void *userdata){

    if (step !=1)
        return;

    if (event == EVENT_MOUSEMOVE)
    {
        if (mouse_is_pressing == true)
        {
            for(int i=0; i < 4; i++)
            {
                if (distanceBetweenTwoPoints(Point2f(x,y), g_points[i]) < 15)
                {
                    g_points[i].x = x;
                    g_points[i].y = y;
                    break;
                }
            }
        }
    }else if (event == EVENT_LBUTTONDOWN)
    {
        for (int i=0; i < 4; i++)
        {
            if (distanceBetweenTwoPoints(Point2f(x,y), g_points[i]) < 10)
            {
                mouse_is_pressing = true;

                
            }
        }
    }else if (event == EVENT_LBUTTONUP)
    {
        mouse_is_pressing = false;
    }
}


 
double angle_between(Point A, Point B)
{

    double dot = A.x*B.x + A.y*B.y; 
    double det = A.x*B.y - A.y*B.x; 
    double angle = atan2(det, dot) * 180/CV_PI; 

    return angle;
}



void sort_points(Point2f points[], Point2f points2[])
{
    vector <Point2f> temp;
    int max_index, min_index;
    float max=0.0, min=10000.0;


    for (int i=0; i<4; i++)
    {
        temp.push_back(points[i]);
    }

    for (int i=0; i<4; i++)
    {
        float sum = temp[i].x + temp[i].y;

        if (min > sum){
            min_index = i;
            min = sum;
        }
    }
    points2[0] = temp[min_index];
    temp.erase(temp.begin()+min_index);


    for (int i=0; i<3; i++)
    {
        float sum = temp[i].x + temp[i].y;

        if (max < sum){
            max_index = i;
            max = sum;
        }
    }
    points2[2] = temp[max_index]; 
    temp.erase(temp.begin()+max_index);


    Point v0 = temp[0] - points2[0];
    Point v1 = temp[1] - points2[0];

    double angle = angle_between(v0, v1);

    if (angle < 0)
    {
        points2[1] = temp[1];
        points2[3] = temp[0];
    }
    else
    {
        points2[1] = temp[0];
        points2[3] = temp[1];
    }
}



Mat transform(Mat img_input, Point2f points[])
{

    Point2f points2[4];
    sort_points(points, points2);


    Point2f topLeft = points2[0];
    Point2f topRight = points2[1];
    Point2f bottomRight = points2[2];
    Point2f bottomLeft = points2[3];

    cout << topLeft << ' ' << topRight << ' ' << bottomRight << ' ' << bottomLeft << endl;
    cout << topLeft.x+topLeft.y << ' ' << topRight.x + topRight.y << ' ';
    cout << bottomRight.x+bottomRight.y << ' ' << bottomLeft.x + bottomLeft.y << endl;


    int topWidth = distanceBetweenTwoPoints(bottomLeft, bottomRight);
    int bottomWidth = distanceBetweenTwoPoints(topLeft, topRight);
    int maxWidth = max(topWidth, bottomWidth);
 
    int leftHeight = distanceBetweenTwoPoints(topLeft, bottomLeft);
    int rightHeight = distanceBetweenTwoPoints(topRight, bottomRight);
    int maxHeight = max(leftHeight, rightHeight);
 
    
    Point2f dst[4];
    dst[0] = Point2f(0, 0);
    dst[1] = Point2f(maxWidth-1, 0);
    dst[2] = Point2f(maxWidth-1, maxHeight-1);
    dst[3] = Point2f(0, maxHeight-1);
 

    Mat H = getPerspectiveTransform(points2, dst);
    Mat img_warped;
    warpPerspective(img_input, img_warped, H, Size(maxWidth, maxHeight));
 
    return img_warped;
}



int findMaxArea(vector<vector<cv::Point>> contours)
{
      
  int max_area = -1;
  int max_index = -1;


  for (int i; i<contours.size(); i++)
  {
  
    int area = contourArea(contours[i]);
    Rect rect = boundingRect(contours[i]);

    if ((rect.width*rect.height)*0.4 > area)
        continue;

    if (rect.width > rect.height)
        continue;

    if (area > max_area){
      max_area = area;
      max_index = i;
    }
  }
  
  if (max_area < 10000)
    max_index = -1;

  return max_index;
}



bool process(Mat img_input, Point2f points[], bool debug)
{

    int height = img_input.rows;
    int width = img_input.cols; 

 
    Mat img_mask(height, width, CV_8UC1, Scalar(0, 0, 0));


    Mat bgdModel, fgdModel;

    Rect rect;
    rect.x = 10;
    rect.y = 10;
    rect.width = width-30;
    rect.height = height-30;


    grabCut( img_input, img_mask, rect, bgdModel, fgdModel,
        3, GC_INIT_WITH_RECT );

    compare(img_mask, GC_PR_FGD, img_mask, CMP_EQ);
    Mat img_grabcut(img_input.size(), CV_8UC3, Scalar(0, 0, 0));

    img_input.copyTo(img_grabcut, img_mask);


    if (debug)
        imshow("grabCut", img_grabcut);




    Mat img_gray;
    cvtColor(img_grabcut, img_gray, COLOR_BGR2GRAY);

    Mat img_canny;
    Canny(img_gray, img_canny, 30, 90);

    if (debug)
        imshow("Canny", img_canny);



    Mat kernel = getStructuringElement( MORPH_ELLIPSE, 
        Size( 5, 5 ) );
    morphologyEx(img_canny, img_canny, MORPH_CLOSE, kernel);

    if (debug)
        imshow("morphology", img_canny);



    vector<vector<Point>> contours;
    findContours(img_canny, contours, RETR_LIST, 
                    CHAIN_APPROX_SIMPLE);

    int max_index = findMaxArea(contours);
    if (max_index < 0)
        return false;

    vector <Point> max_contour = contours[max_index];

    if (debug)
    {
        Mat img_contour = img_input.clone();

        vector<vector<cv::Point>> result;
        result.push_back(max_contour);
        drawContours(img_contour, result, -1, Scalar(0, 0, 255), 3);
        imshow("Contour", img_contour);

    }



    vector<Point> approx;
    approxPolyDP(Mat(max_contour), approx, 
        arcLength(Mat(max_contour), true)*0.02, true);

    vector<cv::Point> hull;
    convexHull(Mat(approx), hull, true);

    if (debug)
    {

        Mat img_convexhull = img_input.clone();

        vector<vector<Point>> result;
        result.push_back(hull);
        drawContours(img_convexhull, result, -1, Scalar(0, 0, 255), 3);
        imshow("convexHull", img_convexhull);
    }



    int size = max_contour.size();

    if (size==4) 
    {
        for (int i; i<max_contour.size(); i++)
        {
            points[i] = max_contour[i];    
        }
        

    }else   
    {
        RotatedRect box = minAreaRect(max_contour);
        box.points(points);
    }


    bool found = false;

    for (int i; i<4; i++)
    {
        if (points[i].x < 0 || points[i].x > width-1
            || points[i].y < 0 || points[i].y > height -1)
        {
            found = true;
            break;
        }
    }

    if (found)
    {
        points[0] = Point(10, 10);
        points[1] = Point(width-11, 10);
        points[2] = Point(width-11, height-11);
        points[3] = Point(10, height-11);
    }

    return true;
}


int main()
{


    Mat img_input = imread("book.jpg");
    int height = img_input.rows;
    int width = img_input.cols;


    Point2f points[4];
    bool ret = process(img_input, points, false);



    if (ret)
    {
        
        namedWindow("input");
        setMouseCallback("input", mouse_callback, 0);

        copy(points, points+4, g_points);

        step = 1;



        Mat img_result;

        while(1)
        {

            img_result = img_input.clone();

            for (int i=0; i<4; i++)
                circle(img_result, g_points[i], 10, 
                    Scalar(255, 0, 0), 3);

            imshow("input", img_result);

            int key = waitKey(1);
            if (key == 32)
                break;
        }


        Mat img_final = transform(img_input, g_points);

        imshow("input", img_result);
        imshow("result", img_final);
    }else
        imshow("input", img_input);

    waitKey(0);

    return 0;
}