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
#%%
img_rows, img_cols = 192, 192
img_channels = 1

path1 = 'C:\Python\Scripts\images\input_test'
path2 = 'C:\Python\Scripts\images\input_test_resized'  

listing = os.listdir(path1) 
num_samples=size(listing)

for file in listing:
    im = Image.open(path1+'\\' + file)   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')
                #need to do some more processing here           
    gray.save(path2 + '\\' +file, "JPEG")

imlist = os.listdir(path2)

im1 = array(Image.open('C:\Python\Scripts\images\input_test_resized' + '\\'+ imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open('C:\Python\Scripts\images\input_test_resized' + '\\' + im2)).flatten()
              for im2 in imlist],'f')
                

label=np.ones((num_samples,),dtype = int)

data,Label = shuffle(immatrix,label, random_state=2)
test_data = [data,Label]




#%%
(X, y) = (test_data[0],test_data[1])


# STEP 1: split X and y into training and testing sets

X_test, y_test = (X, y)


X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)

X_test = X_test.astype('float32')

X_test /= 255


# convert class vectors to binary class matrices
Y_test = np_utils.to_categorical(y_test, 3)


#%%

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

#%%       
model.load_weights("CNN-WEIGHT")

#%%


Y_pred = model.predict(X_test)
Y= np.reshape(Y_pred,(3))
maxprob = max(Y)

#0경미1중증2정상
y_pred = np.argmax(Y_pred, axis=1)
print(y_pred)

if y_pred == 0:
    print(round(maxprob*100,2), "% 확률로 경미한 알츠하이머 증상이 있습니다.")
elif y_pred==1:
    print(round(maxprob*100,2), "% 확률로 중증 알츠하이머 증상이 있습니다.")
elif y_pred==2:
    print(round(maxprob*100,2), "% 확률로 정상입니다.")
    