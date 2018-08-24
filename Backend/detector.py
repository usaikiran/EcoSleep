'''

FACE-DETECTOR , HOG , DLIB , PRE-TRAINED MODEL

'''
from __future__ import division
import sys

import dlib
import os
import cv2
import time
import sys
import json
import predict
import numpy as np
from datetime import datetime

#from pynput import mouse , keyboard
#from threading import Timer
 
def getImgBrightness( img ):

	cvt = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	y, u, v = cv2.split(cvt)
	return np.average(y)


def auto_brightness( img ):

    prediction = getImgBrightness( img )
    prediction = max( 0.2, min( 1, prediction/180 ) )
    print prediction

class Detector:

	monitor_state = 1
	setFlag = 0
	offCount = 0

	input_ev = False

	def __init__( self ):

		try:

			self.non_face_count = 0
			self.wait_time = 3
			self.detector = dlib.get_frontal_face_detector()
			self.fps = 15
			self.scale = 1
			self.wait_time = 3

			self.brightness_interval = 10

			with open( "../UI/data/settings.json" ) as fh:
				data = json.loads( fh.read() )
			
			self.brightness_interval = int( data["brightness_interval"] )
			self.fps = int( data["fps"] )
			self.scale = float( data["scale"] )
			self.wait_time = int( data["wait_time"] )

		except err as Exception:
			
			print "Exceptions caught @ __init__ : ", err

	def changeFlag( self ):

		global input_ev , setFlag
		
		setFlag = 0
		input_ev = False

	def rect_to_bb(rect):
		
		x = rect.left()
		y = rect.top()
		w = rect.right() - x
		h = rect.bottom() - y
	
		return (x, y, w, h)

	def run_detector( self , on, off, state ):

		global monitor_state

		try:

			skip_frame = 3
			downsample_ratio = self.scale
			delay = ( 1/self.fps )
			max_non_face_count = int( ( self.wait_time )/delay )
			self.non_face_count = 0
			count = 0

			brightness_count = 0
			auto_brightness_interval = int( self.brightness_interval/delay )
			#monitor_state = 1

			print " delay : ", delay, " max_non_face_count : ", max_non_face_count, " ratio : ", downsample_ratio

			cam = cv2.VideoCapture( 0 )
			start = time.time()
			
			prev_state = state()
			while True:

				before = datetime.now()

				retval, frame = cam.read( )
				small = cv2.resize( frame, ( 0,0 ), fx=1/downsample_ratio, fy=1/downsample_ratio )

				if retval == True:
					if count % skip_frame == 0 :
						dets = self.detector( small )

					if len( dets ) == 0 :
						self.non_face_count = self.non_face_count + 1
						if self.non_face_count == 1:
							print self.non_face_count, datetime.now()
					
					elif state() != 1:
						#print "on"
						on()
						state( 1 )
						self.non_face_count = 0

					if self.non_face_count > max_non_face_count :
						
						#print "off"
						if state() != 0:
							#print "off"
							off()
							state( 0 )

					count += 1

				else:
					break
				'''
				brightness_count += 1
				if brightness_count == auto_brightness_interval:
					brightness_count = 0
					auto_brightness_callback( frame )
				'''
				after = datetime.now()

				#print ( after-before ).total_seconds()
				time.sleep( max( 0, delay-( after-before ).total_seconds() ) )

		except KeyboardInterrupt:

			cam.release()
			print "\nterminating detector"

def on():

    print "on", datetime.now()


def off( *args ):

    print "off", datetime.now()


def state_handler( state=None ):

    global monitor_state

    if state is None:
        return monitor_state
    else:
        monitor_state = state


if __name__ == "__main__":

	global monitor_state
	monitor_state = 1

	dlib_detector = Detector()
	dlib_detector.run_detector( on = on, off = off, state = state_handler )