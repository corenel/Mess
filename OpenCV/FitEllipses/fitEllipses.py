import cv2
import sys
import os
import datetime

g_c_process_image_width = 640
g_c_process_image_height = 320


def showimg(name, img):
    # show image in a window
    cv2.namedWindow(name)
    cv2.imshow(name, img)


def findThreshold(img):
    # to find a appropriate threshold to apply binaryzation
    bins = {}
    bin_interval = 5
    # initialize bins
    for i in xrange(0, 260, bin_interval):
        bins[i] = 0

    # put pixels in bins
    for row in img:
        for pixel in row:
            i = pixel / bin_interval * bin_interval
            bins[i] += 1

    peaks = []
    # find peaks
    for i in xrange(bin_interval, 260 - bin_interval, bin_interval):
        if (bins[i] > bins[i - bin_interval] and
                bins[i] > bins[i + bin_interval]):
            peaks.append(i)
    # sort the peaks
    peaks.sort()00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # the threshold should be between the most two highest peaks
    # print peaks
    return (peaks[-1] + peaks[-2]) / 2


def recFieldBorder(img, img_TH):
    # count the time
    starttime = datetime.datetime.now()

    # Define the const
    COLOR_GREEN = 4
    # WHITE = 130
    g_c_process_image_width = 640
    g_c_process_image_height = 320
    FIRST_LINE_GREEN_NUM = 200
    WHITE_GREEN_NUM = 290
    Median = 20

    endtime0 = datetime.datetime.now()
    print 'Initial time: ',
    print (endtime0 - starttime).microseconds / 1000.0

    # Traverse the first line and count the white or green pixels
    first_line_white = 0
    first_line_green = 0
    for i in xrange(0, g_c_process_image_width):
        if img_TH[0, i, 0] == COLOR_GREEN:
            first_line_green += 1
        # elif yuvimg[0,i] > WHITE:
        #           first_line_white += 1

    endtime1 = datetime.datetime.now()
    print 'Step 1: ',
    print (endtime1 - endtime0).microseconds / 1000.0

    # If green pixels are more than set value or in other condition
    # set the first line as field border
    FieldBorder = [0] * g_c_process_image_width
    if (first_line_green > FIRST_LINE_GREEN_NUM or
        (first_line_green + first_line_white > WHITE_GREEN_NUM and
            float(first_line_green) / first_line_white > 1)):
        for i in xrange(0, g_c_process_image_width):
            FieldBorder[i] = 0
        # return FieldBorder

    endtime2 = datetime.datetime.now()
    print 'Step 2: ',
    print (endtime2 - endtime1).microseconds / 1000.0

    # If there are 4 consecutive pixels in height are green,
    # set the first pixel as field border
    for i in xrange(0, g_c_process_image_width):
        for j in xrange(0, g_c_process_image_height - 3):
            if (img_TH[j, i, 0] == COLOR_GREEN and
                img_TH[j + 1, i, 0] == COLOR_GREEN and
                img_TH[j + 2, i, 0] == COLOR_GREEN and
                    img_TH[j + 3, i, 0] == COLOR_GREEN):
                FieldBorder[i] = j
                break
            # If can't find green pixles,
            # set the third lowest line as field border
            FieldBorder[i] = g_c_process_image_height - 3

    # Change the width as inside 'for'
    # for j in range(0, g_c_process_image_height - 3):
    #     for i in range(0, g_c_process_image_width):
    #         if (img_TH[j, i, 0] == COLOR_GREEN and
    #             img_TH[j + 1, i, 0] == COLOR_GREEN and
    #             img_TH[j + 2, i, 0] == COLOR_GREEN and
    #                img_TH[j + 3, i, 0] == COLOR_GREEN):
    #             FieldBorder[i] = j

    endtime3 = datetime.datetime.now()
    print 'Step 3: ',
    print (endtime3 - endtime2).microseconds / 1000.0

    # Median filter
    MedianFilter = [0] * (Median * 2 + 1)
    for i in xrange(Median, g_c_process_image_width - Median - 1):
        for j in xrange(0, Median * 2 + 1):
            MedianFilter[j] = FieldBorder[i - Median + j]
        for n in xrange(0, Median * 2):
            for m in xrange(0, Median * 2 - n):
                if MedianFilter[m] > MedianFilter[m + 1]:
                    MedianFilter[m], MedianFilter[m + 1] = MedianFilter[m + 1], MedianFilter[m]
        FieldBorder[i] = MedianFilter[Median]

    endtime4 = datetime.datetime.now()
    print 'Step 4: ',
    print (endtime4 - endtime3).microseconds / 1000.0

    # process original image
    for i in xrange(0, g_c_process_image_width):
        for j in xrange(0, FieldBorder[i]):
            img[j, i] = 0

    endtime5 = datetime.datetime.now()
    print 'Step 5: ',
    print (endtime5 - endtime4).microseconds / 1000.0
    print 'Total: ',
    print (endtime5 - starttime).microseconds / 1000.0

    return img


def findCenterEllipse(input_filename):

    # read in image
    # img_gray = cv2.imread(input_filename, 0)
    # img_gray = cv2.imread('./img/Image7.yuv.rgb.jpg', 0)
    # showimg('origin', img_gray)

    # binaryzation
    # threshold = findThreshold(img_gray)
    # threshold = 124
    # ret, img_binary = cv2.threshold(img_gray, threshold,
    #                                255, cv2.THRESH_BINARY)
    img_binary = cv2.imread('./img/Image7.yuv.WHITE2.png')
    # showimg('binaryzation', img_binary)

    # Remove field border
    img_TH = cv2.imread('./img/Image7.yuv.TH.png')
    img_binary = recFieldBorder(img_binary, img_TH)
    # showimg('recongnize field border', img_binary)

    # apply canny edge detection
    # img_median = cv2.medianBlur(img_binary, 5)
    # showimg('Median Filter', img_median)
    img_binary = cv2.Canny(img_binary, 137, 137 * 3)
    # showimg('canny edge', img_binary)

    # find contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # approximate using polygonal curves, to reduce computation amount
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]

    # draw out contours
    cv2.drawContours(img_binary, contours, -1, (255, 255, 255))
    # showimg('contour', img_binary)

    areas = []
    ellipses = []
    for contour in contours:
        # fitEllipse needs contours have more than 5 points
        if len(contour) < 5:
            continue
        # print contour
        # fit an ellipse
        ellipse = cv2.fitEllipse(contour)
        # append to ellipses
        area = ellipse[1][0] * ellipse[1][1]
        if (area > 2000 and ellipse[1][1] < ellipse[1][0] * 5):
            areas.append(area)
            ellipses.append((ellipse, area))
    areas.sort()
    threshold_min = areas[0]
    threshold_max = areas[-1]
    median = areas[len(areas) / 2]
    for area in areas:
        # too small
        if median / area >= 2 and area > threshold_min:
            threshold_min = area
        # too large
        if area / median >= 2 and area < threshold_max:
            threshold_max = area

    # min_ellipse = None
    # min_area = threshold_max
    max_ellipse = None
    max_area = threshold_min
    # convert back to color image
    # img = cv2.cvtColor(img_gray, cv2.cv.CV_GRAY2BGR)

    # print every ellipse
    for ellipse, area in ellipses:
        if (area < threshold_min):
            continue
            # cv2.ellipse(img, ellipse, (255,0,0), 2)
        # find the largest
        if area > max_area:
            max_area = area
            max_ellipse = ellipse
            print 'Ellipse: at(%d,%d), angle:%f, size:(%f,%f)' % (ellipse[0][1], ellipse[0][1], ellipse[2], ellipse[1][0], ellipse[1][1])

    # cv2.ellipse(img, max_ellipse, (0, 255, 0), 2)
    print 'Max Ellipse: at(%d,%d), angle:%f, size:(%f,%f)' % (max_ellipse[0][1], max_ellipse[0][1], max_ellipse[2], max_ellipse[1][0], max_ellipse[1][1])

    # create a window
    # cv2.namedWindow('done')
    # show the processed image
    # cv2.imshow('done', img)
    cv2.waitKey(0)

    # destroy windows
    cv2.destroyAllWindows()


def usage():
    print 'Usage: python fitEllipses.py {input filename}'


if __name__ == '__main__':
    input_filename = ''

    # command input control
    if len(sys.argv) == 2:
        input_filename = sys.argv[1]
        print 'input filename set to:', input_filename
    else:
        usage()
        sys.exit(0)

    # check if the file exists
    if not os.path.exists(input_filename):
        print 'file', input_filename, 'not found'
        sys.exit(0)

    findCenterEllipse(input_filename)
