
import os
import numpy as np
import cv2

def getImgBrightness( img ) :
	cvt = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	y, u, v = cv2.split(cvt)
	return np.average(y)

def show_webcam(mirror=False):
	cam = cv2.VideoCapture(0)
	count = 0
	while True:
		ret_val, img = cam.read()
		count = count + 1
		if count % 50 == 0 :
			print getImgBrightness(img)
		if mirror: 
			img = cv2.flip(img, 1)
		cv2.imshow('my webcam', img)
		if cv2.waitKey(1) == 27: 
			break  # esc to quit
	cv2.destroyAllWindows()

def getDisplayName():
	return os.popen("xrandr --verbose | head -n 2 | tail -n 1 | awk '{print $1}'").read()[:-1]

def getCurrentBrightness():
	return os.popen("xrandr --verbose | grep Brightness | head -n 1 | awk '{ print $2}'").read()[:-1]

def setBrightness( b ):
	cmd = "xrandr --output {} --brightness {}".format(getDisplayName() , b) 
	os.system(cmd)


if __name__ == '__main__' :

	show_webcam()
	