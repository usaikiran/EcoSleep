
import os

def getDisplayName():
	return os.popen("xrandr --verbose | head -n 2 | tail -n 1 | awk '{print $1}'").read()[:-1]

def getCurrentBrightness():
	return os.popen("xrandr --verbose | grep Brightness | head -n 1 | awk '{ print $2}'").read()[:-1]

def setBrightness( b ):
	cmd = "xrandr --output {} --brightness {}".format(getDisplayName() , b) 
	os.system(cmd)


if __name__ == '__main__' :
	setBrightness(0.5)
	print getCurrentBrightness()
	setBrightness(1.0)
	