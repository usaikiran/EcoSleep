
import os
import time

time.sleep( 0.01 )
res = os.popen("ps aux | grep python | grep main.py | awk '{ print $2 }'").read().split('\n')
print res

for pid in res :
    os.system("sudo kill -KILL " + pid)