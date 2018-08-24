
import os

cmds = [
	"sudo apt update -y" ,

	"sudo apt install python-pip -y" ,
	"sudo pip install --upgrade pip" ,

	"sudo apt-get install software-properties-common -y" ,
	"sudo add-apt-repository ppa:george-edison55/cmake-3.x -y" ,
	"sudo apt-get update -y" ,
	"sudo apt-get install cmake -y" ,
	"sudo pip install dlib" ,
	"sudo pip install imutils -y"

	"sudo pip install keyboard -y" ,
	"sudo pip install pynput -y" ,

	"sudo pip install opencv-python" , 

	"sudo pip install numpy scipy" ,
	"sudo pip install scikit-learn" ,
	"sudo pip install pillow" ,
	"sudo pip install h5py" ,
	"sudo pip install tensorflow" ,
	"sudo pip install keras" ,

	"sudo apt install nodejs -y" ,
	"sudo apt install npm -y" ,
	"npm list -g electron || sudo npm i -g electron --unsafe-perm=true --allow-root" ,
	"npm list -g http || npm i -g http" ,
	"npm list -g net || npm i -g net" ,
	"npm list -g electron-ipc || npm i -g electron-ipc" , 
	"npm list -g system-sleep || npm i -g system-sleep" ,

	"sudo apt-get install wmctrl -y",
	"sudo ln -s /usr/bin/nodejs /usr/bin/node",

	"sudo apt-get install powerstat -y",
	"sudo pip install pexpect"
]

for cmd in cmds :
	os.system(cmd)
