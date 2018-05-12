
import os

cmds = [
	"npm i -g electron --unsafe-perm=true --allow-root" ,
	"npm i -g http" ,
	"npm i -g net" ,
	"npm i -g electron-ipc" , 
	"npm i -g system-sleep" , 
	"sudo apt-get install wmctrl"
]

for cmd in cmds :
	os.system(cmd)