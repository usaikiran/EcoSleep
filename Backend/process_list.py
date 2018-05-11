
import os

def getNameFromPid( pid ):
    return  str.capitalize(os.popen('cat /proc/' + str(pid) +'/status | head -n 1 | awk \'{ print $2 }\'').read())[:-1]

def getRunningPid():
    cmd = "wmctrl -lp | awk '{print $3}'"
    return set(os.popen(cmd).read().split('\n')[1:-1])

def getKernelProcesses():
    l = []
    for s in os.popen('ps aux').read().split('\n') :
        user = s.split(' ')[0]
        id = os.popen('echo "' + s + '" | awk \'{ print $2 }\'').read()
        if user != "root" :
            l.append(id[:-1])
    return l

def getList() :
    l = []
    for pid in getRunningPid():
        l.append(getNameFromPid(pid))
    k = set(getKernelProcesses())

    return "\n".join(set(l) - k)

def getPidList( name ):
    l = []
    for pid in getRunningPid():
        iname = getNameFromPid(pid)
        if iname == name :
            l.append(pid)
    return l

#getPidList('Chrome')
#print getRunningPid()