
import os

cmds = [
	"npm list electron || npm i -g electron --unsafe-perm=true --allow-root" ,
	"npm list http || npm i -g http" ,
	"npm list net || npm i -g net" ,
	"npm list electron-ipc || npm i -g electron-ipc" , 
	"npm list system-sleep || npm i -g system-sleep" , 
	"sudo apt-get install wmctrl"
]

for cmd in cmds :
	os.system(cmd)