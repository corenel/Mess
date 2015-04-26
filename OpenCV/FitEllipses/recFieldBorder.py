import cv2
import numpy as np
import random
import time
import sys
import os

def recFieldBorder(img, img_TH):
	# Define the const
	COLOR_GREEN = 4
	WHITE = 130
	g_c_process_image_width = 640
	g_c_process_image_height = 320
	FIRST_LINE_GREEN_NUM = 200
	WHITE_GREEN_NUM = 290
	Median = 20

	# Traverse the first line and count the white or green pixels
	first_line_white = 0
	first_line_green = 0
	for i in range(0, g_c_process_image_width):
		if img_TH[0,i,0] == COLOR_GREEN:
			first_line_green += 1
#		elif yuvimg[0,i] > WHITE:
#			first_line_white += 1

	# If green pixels are more than set value or in other condition, set the first line as field border
	FieldBorder = [0] * g_c_process_image_width
	if (first_line_green > FIRST_LINE_GREEN_NUM or (first_line_green+first_line_white>WHITE_GREEN_NUM and float(first_line_green)/first_line_white > 1) ):
		for i in range(0, g_c_process_image_width):
			FieldBorder[i] = 0
#			return FieldBorder

	# If there are 4 consecutive pixels in height are green, set the first pixel as field border
	for i in range(0, g_c_process_image_width):
		for j in range(0, g_c_process_image_height - 3):
			if (img_TH[j,i,0] == COLOR_GREEN and img_TH[j+1,i,0] == COLOR_GREEN and img_TH[j+2,i,0]== COLOR_GREEN and img_TH[j+3,i,0] == COLOR_GREEN):
				FieldBorder[i] = j
				break
			# If can't find green pixles, then set the third lowest line as field border
			FieldBorder[i] = g_c_process_image_height - 3

	# Median filter
	MedianFilter = [0] * (Median * 2 + 1)
	for i in range(Median, g_c_process_image_width - Median - 1):
		for j in range(0,Median * 2 + 1):
			MedianFilter[j] = FieldBorder[i - Median + j]
		for n in range(0, Median * 2):
			for m in range(0, Median *2 - n):
				if MedianFilter[m] > MedianFilter[m+1]:
					MedianFilter[m], MedianFilter[m+1] = MedianFilter[m+1], MedianFilter[m]
		FieldBorder[i] = MedianFilter[Median]

	# Print the result
	print FieldBorder
	for i in range(0,g_c_process_image_width):
		for j in range(0,FieldBorder[i]):
			img[j,i] = 0
	cv2.namedWindow('Image')
	cv2.imshow('Image', img)
	cv2.waitKey(0)


Image_TH = cv2.imread('./img/Image6.yuv.TH.png')
Image = cv2.imread('./img/Image6.yuv.rgb.jpg')
recFieldBorder(Image, Image_TH)