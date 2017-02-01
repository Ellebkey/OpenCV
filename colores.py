import numpy as np
import cv2
import threading
from threading import Thread, Event, ThreadError

hue = 10
sat = 10
val = 10
hue2 = 180
sat2 = 255	
val2 = 255

class Cam():
  def nothing():
    pass
  def run(self):

    points = []
    global hue
    global sat
    global val
    cap = cv2.VideoCapture(0)

    while True:
      try:
        _,frame = cap.read()

        h = cv2.getTrackbarPos('H','Objeto')
        s = cv2.getTrackbarPos('S','Objeto')
        v = cv2.getTrackbarPos('V','Objeto')
        h2 = cv2.getTrackbarPos('H','Camera')
        s2 = cv2.getTrackbarPos('S','Camera')
        v2 = cv2.getTrackbarPos('V','Camera')

        lower = np.array([h,s,v])
        upper = np.array([h2,s2,v2])

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        hsv2 = hsv.copy()
        thresh = cv2.inRange(hsv,lower, upper)
        thresh = cv2.medianBlur(thresh,7)
        thresh2 = thresh.copy()

        cv2.imshow('Camera',frame)
        cv2.imshow('Objeto',thresh2)

        if cv2.waitKey(1) ==1048603:
        	exit(0)
        	f.close()

      except ThreadError:
        self.thread_cancelled = True

  cv2.namedWindow('Camera',cv2.CV_WINDOW_AUTOSIZE)
  cv2.namedWindow('Objeto',cv2.CV_WINDOW_AUTOSIZE)
  cv2.createTrackbar('H', 'Objeto', hue, 180, nothing)
  cv2.createTrackbar('S', 'Objeto', sat, 255, nothing)
  cv2.createTrackbar('V', 'Objeto', val, 255, nothing)
  cv2.createTrackbar('H', 'Camera', hue2, 180, nothing)
  cv2.createTrackbar('S', 'Camera', sat2, 255, nothing)
  cv2.createTrackbar('V', 'Camera', val2, 255, nothing)
        
 
  
    
if __name__ == "__main__":
  cam = Cam()
  cam.run()
