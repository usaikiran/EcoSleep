
from __future__ import division

import cv2
import glob
import os

def main():
    fileList = glob.glob("./*/*/images/*.jpg")
    count = 0
    for imgPath in fileList :
        img = cv2.imread(imgPath)
        if img.shape[0] > 60 and img.shape[1] > 60 :
            cv2.imwrite("img/" + str(count) + ".jpg" , img)
            count = count + 1
            print str(count) + " Done -> " +  "img/" + str(count) + ".jpg"

        


if __name__ == '__main__' :
    main()