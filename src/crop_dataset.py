
from __future__ import division

import os
import cv2
import dlib
import numpy as np
import time

detector = None
face_cascade = None
count = 0

def get_files( dir, files ):

    for x in os.listdir( dir ):

        if os.path.isdir( dir+"/"+x ):
            get_files( dir+"/"+x, files )
        else:
            files.append( dir+"/"+x )

    return 

def hog_detector( detector, frame ):

    downsample_ratio = 2
    small = cv2.resize(frame, (0,0), fx=1/downsample_ratio, fy=1/downsample_ratio) 
	
    dets = detector(small)
    
    for i, d in enumerate( dets ):
        
        try :

            x1, y1, x2, y2, w, h = d.left() * downsample_ratio,  \
                                    d.top() * downsample_ratio,  \
                                    (d.right() + 1)* downsample_ratio, \
                                    (d.bottom() + 1)* downsample_ratio, \
                                    d.width()* downsample_ratio, \
                                    d.height()* downsample_ratio
                                    
            frame = frame[ y1:y2, x1:x2 ]

            return frame
        
        except :

            print x1 , x2 , y1 , y2
            return None

    return None        
            

def haar_cascade( face_cascade, img ):

    #img = np.asarray( img )
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:

        try:

            return img[y:y+h, x:x+w]

        except Exception as err:

            print err
    
    return None

if __name__ == "__main__":

    EXT = "/ROBOTS.OX"
    root = "/media/test/WorkSpace/Codes/PROJECT_ES/project_es/dataset"+EXT
    output_path = "/media/test/WorkSpace/Codes/PROJECT_ES/project_es/dataset"+EXT+"/img/"
    false_negative_path = "/media/test/WorkSpace/Codes/PROJECT_ES/project_es/false_negative/"
    files = []
    frame = None
    false_count = 0

    get_files( root, files )
    print "\nImage count : ", len( files )

    detector = dlib.get_frontal_face_detector()
    face_cascade = cv2.CascadeClassifier( '/media/test/WorkSpace/Codes/PROJECT_ES/project_es/haarcascade_frontalface.xml' )

    for path in files:

        try:

            img = cv2.imread( path )

            frame = hog_detector( detector, img )
            if frame is not None:
                frame = haar_cascade( face_cascade, frame )

            if frame is not None:

                cv2.imwrite( output_path+str( count )+".jpg", frame )
                count += 1

                #cv2.imshow( "dataset"+str( count ) , frame )
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
            else:
                frame = haar_cascade( face_cascade, img )

                if frame is not None:
                    cv2.imwrite( output_path+str( count )+".jpg", frame )
                    count += 1
                else:
                    cv2.imwrite( false_negative_path+str( false_count )+".jpg", img )
                    false_count += 1

        except Exception as err:

            print err