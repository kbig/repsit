from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
import os
import theano
from PIL import Image
from numpy import *
from sklearn.utils import shuffle
import cv2
import sys

path1 = 'E:\Python\Scripts\images\input_test'
path2 = 'E:\Python\Scripts\images\input_test_resized'  
pathcompare1 = 'E:\Python\Scripts\images\compare1'
pathcompare2 = 'E:\Python\Scripts\images\compare2'
pathcompare3 = 'E:\Python\Scripts\images\compare3'
Y_pred_all=0
if sys.argv[1] != 'null':
    listing_comp = shuffle(os.listdir(pathcompare1))
    img_rows, img_cols = 192, 192
    img_channels = 1    
    im = Image.open(path1+'\\' + sys.argv[1])   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')                          
    gray.save(path2 + '\\' +sys.argv[1], "JPEG")
    imlist = os.listdir(path2)
    img2 = cv2.imread('images\input_test_resized' + '\\'+ sys.argv[1])
    hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
    avghist = 0
    for i in range(5):  
        img1 = cv2.imread('E:\Python\Scripts\images\compare' + '\\'+listing_comp[i])
        hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])    
        compHist= cv2.compareHist(hist1, hist2,cv2.HISTCMP_CORREL)    
        avghist = avghist + compHist
    avghist = avghist/5
    if avghist > 0.8:
        im1 = np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\'+ sys.argv[1])) # open one image to get size
        m,n = im1.shape[0:2] 
        immatrix = np.array([np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\' + sys.argv[1])).flatten()],'f')                
        label=np.ones(1,dtype = int)
        data,Label = shuffle(immatrix,label, random_state=2)
        test_data = [data,Label]
        (X, y) = (test_data[0],test_data[1])
        X_test, y_test = (X, y)
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
        X_test = X_test.astype('float32')
        X_test /= 255
        Y_test = np_utils.to_categorical(y_test, 3)
        model = Sequential()
        model.add(Convolution2D(32,3,3,border_mode='same',input_shape=X_test.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(32, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(64, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(3))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adadelta',metrics=["acc"])
        model.load_weights("E:\Python\Scripts\CNN-WEIGHT")        
        Y_pred = model.predict(X_test)
        Y_pred_all = Y_pred_all+ Y_pred
else:
    print("1번 사진을 확인해 주세요")        
if sys.argv[2] != 'null':
    listing_comp = shuffle(os.listdir(pathcompare2))
    img_rows, img_cols = 192, 192
    img_channels = 1    
    im = Image.open(path1+'\\' + sys.argv[2])   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')                          
    gray.save(path2 + '\\' +sys.argv[2], "JPEG")
    imlist = os.listdir(path2)
    img2 = cv2.imread('images\input_test_resized' + '\\'+ sys.argv[2])
    hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
    avghist = 0
    for i in range(5):  
        img1 = cv2.imread('E:\Python\Scripts\images\compare' + '\\'+listing_comp[i])
        hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])    
        compHist= cv2.compareHist(hist1, hist2,cv2.HISTCMP_CORREL)    
        avghist = avghist + compHist
    avghist = avghist/5
    if avghist > 0.8:
        im1 = np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\'+ sys.argv[2])) # open one image to get size
        m,n = im1.shape[0:2] 
        immatrix = np.array([np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\' + sys.argv[2])).flatten()],'f')                
        label=np.ones(1,dtype = int)
        data,Label = shuffle(immatrix,label, random_state=2)
        test_data = [data,Label]
        (X, y) = (test_data[0],test_data[1])
        X_test, y_test = (X, y)
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
        X_test = X_test.astype('float32')
        X_test /= 255
        Y_test = np_utils.to_categorical(y_test, 3)
        model = Sequential()
        model.add(Convolution2D(32,3,3,border_mode='same',input_shape=X_test.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(32, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(64, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(3))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adadelta',metrics=["acc"])
        model.load_weights("E:\Python\Scripts\CNN-WEIGHT")        
        Y_pred = model.predict(X_test)
        Y_pred_all = Y_pred_all+ Y_pred
else:
    print("2번사진을 확인해 주세요")
if sys.argv[3] != 'null':
    listing_comp = shuffle(os.listdir(pathcompare3))
    img_rows, img_cols = 176, 176
    img_channels = 1    
    im = Image.open(path1+'\\' + sys.argv[3])   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')                          
    gray.save(path2 + '\\' +sys.argv[3], "JPEG")
    imlist = os.listdir(path2)
    img2 = cv2.imread('images\input_test_resized' + '\\'+ sys.argv[3])
    hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
    avghist = 0
    for i in range(5):  
        img1 = cv2.imread('E:\Python\Scripts\images\compare' + '\\'+listing_comp[i])
        hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])    
        compHist= cv2.compareHist(hist1, hist2,cv2.HISTCMP_CORREL)    
        avghist = avghist + compHist
    avghist = avghist/5
    if avghist > 0.8:
        im1 = np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\'+ sys.argv[3])) # open one image to get size
        m,n = im1.shape[0:2] 
        immatrix = np.array([np.array(Image.open('E:\Python\Scripts\images\input_test_resized' + '\\' + sys.argv[3])).flatten()],'f')                
        label=np.ones(1,dtype = int)
        data,Label = shuffle(immatrix,label, random_state=2)
        test_data = [data,Label]
        (X, y) = (test_data[0],test_data[1])
        X_test, y_test = (X, y)
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
        X_test = X_test.astype('float32')
        X_test /= 255
        Y_test = np_utils.to_categorical(y_test, 3)
        model = Sequential()
        model.add(Convolution2D(32,3,3,border_mode='same',input_shape=X_test.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(32, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Convolution2D(64, 3, 3,border_mode='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering="th"))
        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(3))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adadelta',metrics=["acc"])
        model.load_weights("E:\Python\Scripts\CNN-WEIGHT")        
        Y_pred = model.predict(X_test)
        Y_pred_all = Y_pred_all+ Y_pred
            
    y_pred = np.argmax(Y_pred_all, axis=1)
    
    
    if y_pred == 0:
        print("경미!")
    elif y_pred==1:
        print("중증!")
    elif y_pred==2:
        print("정상!")
  
else:
    print("3번사진을 확인해주세요")

                