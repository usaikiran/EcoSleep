
from __future__ import division

import cv2
import dlib
from skimage import io
import glob
import time


def main():

    l = glob.glob("./*/*.jpg")
    detector = dlib.get_frontal_face_detector()
    count = 0
    tcount = 0
    start = time.clock()
    for fname in l :

        img = cv2.imread(fname)
        dets = detector(img, 1)
        tcount = tcount + 1

        for i, d in enumerate(dets):

            crop_img = img[d.top():d.bottom(),d.left():d.right()]
            cv2.imwrite("img/" + str(count) + ".jpg" , crop_img)
            count = count + 1
            print str(count) + " Done -> " +  "img/" + str(count) + ".jpg"

    print time.clock() - start
    print (time.clock() - start) / tcount

if __name__ == '__main__' :
    main()