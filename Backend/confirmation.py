from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import math

class ConfirmFace():

    def __init__(self , path = "./landmarks.dat"):

        self.faceList = []
        self.threshold = 0.3
        self.consecFrames = 3
        self.counter = []
        self.total = 0
        self.path = path
        self.predictor = dlib.shape_predictor(self.path)

        (self.lStart, self.lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.rStart, self.rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    def eye_aspect_ratio(self , eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])

        C = dist.euclidean(eye[0], eye[3])
    
        ear = (A + B) / (2.0 * C)
        
        return ear

    def getEARList(self , gray , faceList):
        earList = []
        for face in faceList :
            shape = self.predictor(gray , face)
            shape = face_utils.shape_to_np(shape)
            
            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            leftEAR = self.eye_aspect_ratio(leftEye)
            rightEAR = self.eye_aspect_ratio(rightEye)
            
            ear = (leftEAR + rightEAR) / 2.0
            earList.append(ear)
        
        return earList

    def confirm( self , gray , faceList , verbose = False):

        if len(faceList) != len(self.faceList) :
            self.faceList = self.getEARList( gray , faceList )
            self.counter = [0 for i in range( len(faceList) )]


        newList = self.getEARList( gray , faceList )

        diff = 0

        for i in range(len(newList)) :
            diff = max (diff , abs(newList[i] - self.faceList[i]) )

        diff = float("{:0.2f}".format(diff))

        for i in range(len(newList)):
            if newList[i] < self.threshold :
                self.counter[i] += 1
            else :

                if self.counter[i] >= self.consecFrames :
                    print "blinked - face no." ,i  

                self.counter[i] = 0

                
        self.faceList = newList

        print diff



if __name__ == '__main__' :
    
    c = ConfirmFace()

    #cam = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()

    # while True:
    #     ret_val, img = cam.read()
    #     img = cv2.flip(img, 1)
    #     gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    #     rects = detector(gray , 0)
    #     cv2.imshow('my webcam', img )

    #     c.confirm(gray , rects)


    #     if cv2.waitKey(1) == 27: 
    #         break

    #     #time.sleep(0.05)

	# cv2.destroyAllWindows()

    ts = ["./t1.jpeg" , "./t2.jpeg"]

    for t in ts :
        img = cv2.imread(t , 0)
        rects = detector(img , 0)
        c.confirm(img , rects)


        



    