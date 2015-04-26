#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
using namespace cv;
using namespace std;

int main(void)
{
    Mat image;
    image = imread("1.jpg");

    int cols = image.cols;
    int rows = image.rows;
    for (int i = 0; i <= rows; i++){
        uchar* ImgPtr = image.ptr<uchar>(i);
        for (int j = 0; j <= cols; j++){
            ImgPtr[j] = ImgPtr[j] /64 *64 + 32;
        }
    }
    namedWindow("Quantilized Image");
    imshow("Quantilized Image",image);
    waitKey(50000);
    return 0;
}
