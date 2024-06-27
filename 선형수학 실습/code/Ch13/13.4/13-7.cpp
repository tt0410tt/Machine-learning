#include <opencv2/opencv.hpp>


using namespace cv;
using namespace std;


Mat draw_histogram(Mat img)
{
    // 히스토그램을 그릴 이미지를 생성합니다. 
    int hist_h = img.rows;
    int hist_w = 256;
    Mat img_histogram1( hist_h, hist_w, CV_8UC1, Scalar(0,0,0));

    
    // 히스토그램을 계산하여 히스토그램을 그립니다. 
    Mat hist_item;
    int histSize = 256;
    float range[] = { 0, 256 }; 
    const float* histRange = { range };
    bool uniform = true; bool accumulate = false;

    calcHist(&img, 1, 0, Mat(), hist_item, 1, &histSize, &histRange,  
                uniform, accumulate );
    normalize(hist_item,hist_item, 0, 255, NORM_MINMAX);

    for( int i = 1; i < histSize; i++ )
        line(img_histogram1, 
            Point(i, hist_h - cvRound(hist_item.at<float>(i))), 
            Point(i, hist_h), Scalar(255,255,255));



    // 누적 히스토그램을 그릴 이미지를 생성합니다.
    Mat img_histogram2( hist_h, hist_w, CV_8UC1, Scalar(0,0,0));


    // 누적 히스토그램을 계산하여 누적 히스토그램을 그립니다.
    Mat c_hist(hist_item.size(), hist_item.type());

    c_hist.at<float>(0) = hist_item.at<float>(0);
    for(int i = 1; i < hist_item.rows; ++i)
        c_hist.at<float>(i) = hist_item.at<float>(i) 
                    + c_hist.at<float>(i-1);

    normalize(c_hist,c_hist, 0, 255, NORM_MINMAX);

    vector<Point> contour;

    for( int i = 1; i < histSize; ++i)
    {
        contour.clear();
        contour.push_back(Point(i, 
hist_h - cvRound(c_hist.at<float>(i))));
        contour.push_back(Point((i-1), 
hist_h - cvRound(c_hist.at<float>(i-1))));

        const Point *pts = (const cv::Point*) Mat(contour).data;
        int npts = Mat(contour).rows;

        polylines(img_histogram2, &pts, &npts, 
1, true, Scalar(255,255,255));
    }               


    Mat result;
    hconcat(img_histogram1, img_histogram2, result);

    return result;
 
}


int main()
{
    Mat img_gray = imread("test.png", IMREAD_GRAYSCALE);

    Mat img_histo1 = draw_histogram(img_gray);
    Mat result1;
    hconcat(img_gray, img_histo1, result1);
    imshow("result1", result1);

    Mat img_clahe;
    Ptr<CLAHE> clahe = createCLAHE();
    clahe->setClipLimit(2.0);
    clahe->setTilesGridSize(Size(8,8));

    clahe->apply(img_gray, img_clahe);


    Mat img_histo2 = draw_histogram(img_clahe);
    Mat result2;
    hconcat(img_clahe, img_histo2, result2);
    imshow("result2", result2);

    waitKey(0);

    return 0;
}
