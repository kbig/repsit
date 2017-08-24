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


#%%


path1 = 'images\input_test2'
path2 = 'images\input_test_resized2'  
path3 = 'images\inputdata2'
listing = os.listdir(path1)
listing3 = shuffle(os.listdir(path3)) 

img_rows, img_cols = 192, 192
img_channels = 1

for file in listing:
    im = Image.open(path1+'\\' + file)   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')                          
    gray.save(path2 + '\\' +file, "JPEG")
    
imlist = os.listdir(path2)
img2 = cv2.imread('images\input_test_resized2' + '\\'+ imlist[0])
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
avghist = 0

for i in range(5): 
    
    img1 = cv2.imread('images\inputdata2' + '\\'+listing3[i])
    hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])    
    compHist= cv2.compareHist(hist1, hist2,cv2.HISTCMP_CORREL)    
    avghist = avghist + compHist    

if avghist/5 > 0.8:    
    im1 = array(Image.open('images\input_test_resized2' + '\\'+ imlist[0])) # open one image to get size
    m,n = im1.shape[0:2] 
    imnbr = len(imlist)
    num_samples=size(listing)
    immatrix = array([array(Image.open('images\input_test_resized2' + '\\' + im2)).flatten()
                  for im2 in imlist],'f')                
    
    label=np.ones((num_samples,),dtype = int)
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
    model.load_weights("CNN-WEIGHT")
    
    Y_pred = model.predict(X_test)
    Y= np.reshape(Y_pred,(3))    
    y_pred = np.argmax(Y_pred, axis=1)
    
    if y_pred == 0:
        print("경미한 알츠하이머 증상으로 예측되었습니다.")
    elif y_pred==1:
        print("중증 알츠하이머 증상으로 예측되었습니다.")
    elif y_pred==2:
        print("정상으로 예측되었습니다.")
else:
    print("올바른 사진을 업로드하세요.")    
        


                