
from subprocess import Popen, PIPE
from time import sleep
import os
import signal

<<<<<<< HEAD
def getWatt( interval=1 ):

	interval = min( interval, 1 )
	sleep( max( 0, interval-1.1 ) )

	file = open("tmp" , "w")
	process = Popen(["powerstat -d 0 1"], shell = True , stdout= file , preexec_fn=os.setsid)
	sleep( 1.1 )
=======

def getWatt( dur = 1 ):
	file = open("tmp" , "w")
	process = Popen(["powerstat -d 0 " + str(int(dur))], shell = True , stdout= file , preexec_fn=os.setsid)
	sleep(dur + 0.1)
>>>>>>> bf8743ce1282d742d3a404cdf273c76e99c4c302
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