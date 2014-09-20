#!/usr/bin/env python
from cv2 import *
import cv2
import numpy as np

#Create window to display image
cv2.namedWindow('colorhist', cv2.CV_WINDOW_AUTOSIZE)

#Set hist parameters

hist_height = 200
hist_width = 256
nbins = 128
bin_width = hist_width/nbins

#Read image in grayscale mode
img = cv2.imread('flower.jpg',0)

#Create an empty image for the histogram
h = np.zeros((hist_height,hist_width))

#Create array for the bins
bins = np.arange(nbins,dtype=np.int32).reshape(nbins,1)

 #Calculate and normalise the histogram
hist_item = cv2.calcHist([img],[0],None,[nbins],[0,256])
cv2.normalize(hist_item,hist_item,hist_height,cv2.NORM_MINMAX)
hist=np.int32(np.around(hist_item))
pts = np.column_stack((bins,hist))

#Loop through each bin and plot the rectangle in white
for x,y in enumerate(hist):
    cv2.rectangle(h,(x*bin_width,y),(x*bin_width + bin_width-1,hist_height),(255),-1)

#Flip upside down
h=np.flipud(h)

#Show the histogram
cv2.imshow('colorhist',h)
cv2.waitKey(0)