
from cv2 import *

import os
import os.path
import hashlib

def wget(url):
    a = os.system("wget " + url + " 2>/dev/null")

def main():

    file = open("pub_dataset.txt")
    content = file.read().split('\n')
    totalCount = 1294
    failureCount = 0
    failureList = []

    for i in range(1295 , len(content)):

        totalCount = totalCount + 1

        try :
            line = content[i].split('\t')
            url = line[2]
            fname = (os.path.join(os.getcwd() , url.split('/')[-1]))
            wget(url)
            crop = line[3].split(',')
            crop = map(int, crop)
            im = imread(fname)
            
            cv2.imwrite("./img/" + str(totalCount) + ".jpg" , im[crop[1]:crop[3] , crop[0]:crop[2]])
            print "Image " + str(totalCount) + " finished."
        
        except :
            failureCount = failureCount + 1
            failureList.append( totalCount - 1 )

        finally :
            if os.path.isfile(fname) :
                os.remove(fname)

        
    print "Total \t: " + totalCount 
    print "Failure \t:" + failureCount 

        

if __name__ == '__main__' :
    main()