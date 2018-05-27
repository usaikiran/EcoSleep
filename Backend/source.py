

import sys
import os
import numpy as np
import cv2

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import load_model
from keras.callbacks import ModelCheckpoint

class Model( Sequential ):

    def __init__( self ):
        Sequential.__init__( self )

        self.weights_path = "./weights.hdf5"
        self.dataset_path = "./esd/"

        np.random.seed( 123 )
        self.create_model()


    def create_model( self ):
    
        self.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(70,60,1)))
        self.add(Convolution2D(32, 3, 3, activation='relu'))
        self.add(MaxPooling2D(pool_size=(2,2)))
        self.add(Dropout(0.25))
        
        self.add(Flatten())
        self.add(Dense(128, activation='relu'))
        self.add(Dropout(0.5))
        self.add(Dense(2, activation='softmax'))


    def train( self ):
        
        self.create_model()
        
        if os.path.exists( self.weight_path ):
            self.load_weights(weights_path)

        self.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        checkpointer = ModelCheckpoint(filepath=self.weights_path, verbose=1, save_best_only=True)
        self.fit( self.train_set, self.train_labels, 
                batch_size=32, nb_epoch=10, verbose=1, validation_data=( self.test_set, self.test_labels ), callbacks=[checkpointer])


    def load_dataset( self ):

        self.train_set = []
        self.train_labels = []
        self.test_set = []
        self.test_labels = []

        paths = os.listdir( self.dataset_path+"train/positive" )
        
        pos_ratio = 0.8
        pos_range = range( 0, int( len( paths )*pos_ratio ) )
        val_range = range( int( len( paths )*pos_ratio ), len( paths ) )
        neg_range = range( 0, int( len( paths )*pos_ratio )*4 )

        for i in pos_range:

            img_path = paths[i]
            img = cv2.imread( self.dataset_path+"train/positive/"+img_path, cv2.IMREAD_GRAYSCALE )
            img = img.reshape( 70, 60, 1 )
            self.train_set.append( img )
            self.train_labels.append( 1 )

        print np.array( self.train_set ).shape

        paths = os.listdir( self.dataset_path+"train/negative" )
        for i in neg_range:

            img_path = paths[i]
            img = cv2.imread( self.dataset_path+"train/negative/"+img_path, cv2.IMREAD_GRAYSCALE )
            img = img.reshape( 70, 60, 1 )

            print np.array( self.train_set ).shape
            self.train_set.append( img )
            self.train_labels.append( 0 )

        paths = os.listdir( self.dataset_path+"train/positive" )
        for i in val_range:

            img_path = paths[i]
            img = cv2.imread( self.dataset_path+"train/positive/"+img_path, cv2.IMREAD_GRAYSCALE )
            img = img.reshape( 70, 60, 1 )
            self.test_set.append( img )
            self.test_labels.append( 1 )

        self.train_set = np.array( self.train_set )
        self.test_set = np.array( self.test_set )

        print self.train_set.shape, self.test_set.shape

        #self.train_set = self.train_set.reshape(self.train_set.shape[0], 70, 60, 1)
        #self.test_set = self.test_set.reshape(self.test_set.shape[0], 60, 70, 1)
        self.train_set = self.train_set.astype('float32')
        self.test_set = self.test_set.astype('float32')
        self.train_set /= 255
        self.test_set /= 255
        
        self.train_labels = np_utils.to_categorical(self.train_labels, 2)
        self.test_labels = np_utils.to_categorical(self.test_labels, 2)


    def load_cnn_model( self ):
        
        self.create_model()

        if os.path.exists( self.weights_path ):
            self.load_weights(self.weights_path)


if __name__ == "__main__":

    model = Model()
    model.load_dataset()

    model.create_model()
    #model.train()

    model.load_cnn_model()
    #model.save( "model.hdf5" )

    score = self.evaluate( model.test_set, model.test_labels, verbose=0)
    print "\n\n SCORE : ", score, "\n\n"
