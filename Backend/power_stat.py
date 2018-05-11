
from subprocess import Popen, PIPE
from time import sleep
import os
import signal

def getWatt():
	file = open("tmp" , "w")
	process = Popen(["powerstat -d 0 1"], shell = True , stdout= file , preexec_fn=os.setsid)
	sleep(1.1)
	os.killpg(os.getpgid(process.pid), signal.SIGTERM)
	process.kill()
	file.close()
	sleep(0.01)
	file = open("tmp" , "r")
	content = file.read().split("\n")[:-1]
	os.remove("tmp")
	if len(content) == 1 :
		return None
	else :
		return content[4].split(' ')[-2]

if __name__ == '__main__' :
	print getWatt()