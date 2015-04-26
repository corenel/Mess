import cv2
import numpy as np
import random
import time
import sys
import os

PI = 3.14159

# show image in a window 
def showimg(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)
    

# to find a appropriate threshold to apply binaryzation
def findThreshold(img):
    bins = {}
    bin_interval = 5
    # initialize bins
    for i in range(0, 260, bin_interval):
        bins[i] = 0
    
    # put pixels in bins    
    for row in img:
        for pixel in row:
            i = pixel / bin_interval * bin_interval
            bins[i] = bins[i] + 1
    
    
    peaks = []
    # find peaks
    for i in range(bin_interval, 260-bin_interval, bin_interval):
        if bins[i] > bins[i-bin_interval] and bins[i] > bins[i+bin_interval]:
            peaks.append(i)
    
    # sort the peaks        
    peaks.sort()
    # the threshold should be between the most two highest peaks
    return (peaks[-1]+peaks[-2])/2
    
    
def cellcount(input_filename):    
    # read in image
    img_grey = cv2.imread(input_filename, 0)
    showimg('origin', img_grey)
    
    # binaryzation
    threshold = findThreshold(img_grey)
    ret, img_binary = cv2.threshold(img_grey, threshold, 255, cv2.THRESH_BINARY)
    showimg('binaryzation', img_binary)
    
    #img_grey = cv2.adaptiveBilateralFilter(img_grey, (17,17), 50.0)
    #showimg('bifilter', img_grey)

    # apply canny edge detection
    img_binary = cv2.Canny(img_binary, 200, 250)
    showimg('canny edge', img_binary)

    # find contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # approximate using polygonal curves, to reduce computation amount
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]
    
    # draw out contours    
    cv2.drawContours(img_binary, contours, -1, (255,255,255))
    showimg('contour', img_binary)
        

    ellipses = []
    areas = []
    for contour in contours:
        # fitEllipse needs contours have more than 5 points
        if len(contour) < 5:
            continue
        
        # fit an ellipse            
        ellipse = cv2.fitEllipse(contour)
        
        # calculate area
        area = ellipse[1][0] * ellipse[1][1]
        areas.append(area)
        ellipses.append((ellipse, area))


    # eliminate too large or too small ellipses
    areas.sort()
    #print areas
    
    threshold_min = areas[0]
    threshold_max = areas[-1]
    # use the median as criteria
    median = areas[len(areas)/2]
    for area in areas:
        # too small
        if median / area >= 2 and area > threshold_min:
            threshold_min = area
        # too large
        if area / median >= 2 and area < threshold_max:
            threshold_max = area

    # statics
    cell_count = 0
    total_area = 0
    min_ellipse = None
    min_area = threshold_max
    max_ellipse = None
    max_area = threshold_min
    # convert back to color image
    img = cv2.cvtColor(img_grey, cv2.cv.CV_GRAY2BGR)
    for ellipse,area in ellipses:                
        if (area < threshold_min) or (area > threshold_max):
            continue
        
        # count amount    
        cell_count = cell_count + 1
        # add up area
        total_area = total_area + area
        
        # find the smallest
        if area < min_area:
            min_area = area
            min_ellipse = ellipse
        
        # find the largest
        if area > max_area:
            max_area = area
            max_ellipse = ellipse
            
        # draw ellipse
        cv2.ellipse(img, ellipse, (255,0,0), 2)


    print 'there are %d cells in total.' %cell_count
    # print out info for smallest cell
    area = PI*min_ellipse[1][0]*min_ellipse[1][1]
    perimeter = 2*PI*min_ellipse[1][0] + 4*(min_ellipse[1][1] - min_ellipse[1][0])
    print 'smallest cell: at(%d,%d), angle:%f, perimeter:%f, area:%f' %(min_ellipse[0][0], min_ellipse[0][1], min_ellipse[2], perimeter, area)

    # print out info for largest cell
    area = PI*max_ellipse[1][0]*max_ellipse[1][1]
    perimeter = 2*PI*max_ellipse[1][0] + 4*(max_ellipse[1][1] - max_ellipse[1][0])
    print 'largest cell: at(%d,%d), angle:%f, perimeter:%f, area:%f' %(max_ellipse[0][0], max_ellipse[0][1], max_ellipse[2], perimeter, area)    
    
    print 'average area: %f' %(total_area/cell_count)

    # create a window
    cv2.namedWindow('done')
    # show the processed image
    cv2.imshow('done', img)
    cv2.waitKey(0)
    
    # destroy windows
    cv2.destroyAllWindows()





def usage():
    print 'Usage: python cellcount.py {input filename}'
    
if __name__=='__main__':
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
        
        
    cellcount(input_filename)
    