
import sys
import os
import numpy as np
import cv2
import imutils

from source import Model

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
 
def pyramid( image, scale=1, minSize=(60, 70) ):

    while True:

        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width=w)

        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        
        scale -= 0.1

if __name__ == "__main__":

    model = Model()
    model.load_model()

    images = []
    img = cv2.imread( "./esd/train/positive/1.jpg", cv2.IMREAD_GRAYSCALE )
    img = img.reshape( 70, 60, 1 )
    images.append( img )

    img = cv2.imread( "./esd/train/positive/2.jpg", cv2.IMREAD_GRAYSCALE )
    img = img.reshape( 70, 60, 1 )
    images.append( img )
    images = np.array( images )

    #pyramid( image )
    print model.predict( images )