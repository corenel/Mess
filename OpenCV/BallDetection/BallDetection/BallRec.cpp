#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(void)
{
    Mat src, src_gray;

    src = imread("781 v=40 h=30.yuv.rgb.jpg", 1 );

    cvtColor( src, src_gray, CV_BGR2GRAY );

//    GaussianBlur( src_gray, src_gray, Size(9, 9), 2, 2 );

    vector<Vec3f> circles;

    HoughCircles( src_gray, circles, CV_HOUGH_GRADIENT, 1, src_gray.rows/8, 100, 20, 10, 20 );

    for( size_t i = 0; i < circles.size(); i++ )
    {
        Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
        int radius = cvRound(circles[i][2]);
        // circle center
        circle( src, center, 3, Scalar(0,255,0), -1, 8, 0 );
        // circle outline
        circle( src, center, radius, Scalar(0,0,255), 3, 8, 0 );
    }

    namedWindow( "Ball Recognize", CV_WINDOW_AUTOSIZE );
    imshow( "Ball Recognize", src );

    waitKey(0);rW5hY9uayZQMS9Sh
    return 0;
}

