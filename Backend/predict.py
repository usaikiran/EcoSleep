
import sys
import os
import numpy as np
import cv2
import imutils
import time

from source import Model

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import load_model
from keras.callbacks import ModelCheckpoint

def pyramid(img , scale = 1.2 , minSize = (15, 15)) :
  yield img
  
  while True :
    img = cv2.resize(img, (0,0), fx= 1.0 / scale , fy= 1.0 / scale )
    if img.shape[0] < minSize[0] or img.shape[1] < minSize[1] :
      break
    yield img


def sliding_window(image, stepSize, windowSize):
    
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])


def displayImage( img ):
  # plt.axis("off")
  # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  # plt.imshow( img , shape = img.shape[:2] )
  # plt.show()
  cv2.imshow("1" , img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


if __name__ == "__main__":

  # model = build(iwidth , iheight , 1 , num_classes)
  image = cv2.imread("./esd/test/1.jpg" , 0)
  image = image.reshape( image.shape[0], image.shape[1], 1 )
  winW = 60
  winH = 70
  stepSize = 10
  imgList = []

  for resized in pyramid(image, scale=1.2):
    for (x, y, window) in sliding_window(resized, stepSize=stepSize, windowSize=(winW, winH)):
      if window.shape[0] != winH or window.shape[1] != winW:
              continue
      
      #clone = resized.copy()
      #cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
      #cv2.imshow("Window", clone)
      #cv2.waitKey(0)
      #time.sleep(0.0025)
      np.array(window).resize()
      window = np.reshape(np.array([window]) , (winH , winW , 1))
      imgList.append(window)

  x_test = np.array(imgList)
  x_test = x_test.astype('float32')
  x_test /= 255
  wpath = "weights_v2.hdf5"

  model = Model()
  model.load_weights(wpath)
  output = model.predict_classes(x_test , verbose=1)

  for i in range(len(output)) :

      print output[i]
      if output[i] == 1 :
          cv2.imshow("Window", imgList[i])
          cv2.waitKey(0)
          time.sleep(0.0025)