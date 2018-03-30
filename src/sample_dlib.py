from __future__ import division
import sys

import dlib
from skimage import io

import cv2
from time import time

detector = dlib.get_frontal_face_detector()
#win = dlib.image_window()

skip_frame = 2
downsample_ratio = 2
count = 0

cam = cv2.VideoCapture(0)  #set the port of the camera as before
start = time()

while True:

	retval, frame = cam.read() 
	small = cv2.resize(frame, (0,0), fx=1/downsample_ratio, fy=1/downsample_ratio) 
	
	if retval == True:
		
		if count % skip_frame == 0 :
			dets = detector(small)
		
		for i, d in enumerate( dets ):
			
			try :
				x1, y1, x2, y2, w, h = d.left() * downsample_ratio,  \
										d.top() * downsample_ratio,  \
										(d.right() + 1)* downsample_ratio, \
										(d.bottom() + 1)* downsample_ratio, \
										d.width()* downsample_ratio, \
										d.height()* downsample_ratio
				cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
			
			except :
				print x1 , x2 , y1 , y2
		
		cv2.imshow('Frame',frame)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

		count = count + 1

	else: 
		break