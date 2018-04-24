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

#from pynput import mouse , keyboard
#from threading import Timer

class Detector:

	monitor_state = 1
	setFlag = 0
	offCount = 0

	input_ev = False

	def __init__( self ):

		self.non_face_count = 0

		self.detector = dlib.get_frontal_face_detector()	

	def changeFlag( self ):

		global input_ev , setFlag
		
		setFlag = 0
		input_ev = False


	def haarcascade_detector():

		faceCascade = cv2.CascadeClassifier( "haarcascade_frontalface.xml" )

		video_capture = cv2.VideoCapture(0)

		while True:
			# Capture frame-by-frame
			ret, frame = video_capture.read()

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags=cv2.cv.CV_HAAR_SCALE_IMAGE
			)

			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			cv2.imshow('Video', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		video_capture.release()
		cv2.destroyAllWindows()

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
			downsample_ratio = 1
			delay = 0.1
			self.wait_time = 3
			max_non_face_count = self.wait_time/delay
			self.non_face_count = 0
			count = 0
			#monitor_state = 1

			cam = cv2.VideoCapture( 0 )
			start = time.time()
			
			prev_state = state()
			while True:

				retval, frame = cam.read( )
				small = cv2.resize( frame, ( 0,0 ), fx=1/downsample_ratio, fy=1/downsample_ratio )

				if retval == True:
					if count % skip_frame == 0 :
						dets = self.detector( small )

					if len( dets ) == 0 :
						self.non_face_count = self.non_face_count + 1
					
					else :

						if state() != 1:
							print "on"
							on()
							state( 1 )
							self.non_face_count = 0

					if self.non_face_count > max_non_face_count :
						
						#print "off"
						if state() != 0:
							print "off"
							off()
							state( 0 )

					count += 1

				else:
					break

				#print dets
				'''for i, obj in enumerate( dets ):
					
					#print dir( obj ), obj.left(), obj.right(), obj.top(), obj.bottom(), obj.top
					x = obj.left()
					w = obj.right()-x
					y = obj.top()
					h = obj.bottom()-y
					#x, y, w, h = rect_to_bb( obj[0] )
					cv2.rectangle( frame, ( x, y ), ( x+w, y+h ), ( 0, 255, 0 ), 2 )

				cv2.imshow('Video', frame)

				if cv2.waitKey(1) & 0xFF == ord('q'):
					break'''
				time.sleep( delay )

		except KeyboardInterrupt:

			cam.release()
			print "\nterminating detector"

def on():

    pass


def off( *args ):    

    pass

def off( *args ):    

    pass

def state_handler( state=None ):

    global monitor_state

    if state is None:
        return monitor_state
    else:
        monitor_state = state


if __name__ == "__main__":

	pass	