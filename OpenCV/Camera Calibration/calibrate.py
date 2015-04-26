#!/usr/bin/env python

import numpy as np
import cv2
import os
from glob import glob

def splitfn(fn):
    path, fn = os.path.split(fn)
    name, ext = os.path.splitext(fn)
    return path, name, ext

# defien the image file location
# this shoulf be replaced by camera capture function
img_mask = './img/*.jpg'
img_names = glob(img_mask)

# define the real size of each square
square_size = 1.0

# define parttern size
pattern_size = (9, 6)
pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size

# intialize
obj_points = []
img_points = []
h, w = 0, 0

# find chessboard corners
for fn in img_names:
    print 'processing %s...' % fn,
    img = cv2.imread(fn, 0)
    h, w = img.shape[:2]
    found, corners = cv2.findChessboardCorners(img, pattern_size)
    if found:
        term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
        cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

        # display the corners
        vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.drawChessboardCorners(vis, pattern_size, corners, found)
        path, name, ext = splitfn(fn)
        cv2.namedWindow('Image %s' % name)
        cv2.imshow('Image %s' % name, vis)
    if not found:
        print 'chessboard not found'
        continue
    img_points.append(corners.reshape(-1, 2))
    obj_points.append(pattern_points)

    print 'ok'


rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h))
print "RMS:", rms
print "camera matrix:\n", camera_matrix
print "distortion coefficients: ", dist_coefs.ravel()
cv2.waitKey(0)
cv2.destroyAllWindows()
