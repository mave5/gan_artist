from __future__ import print_function
import numpy as np
# import sys
import os
backend="tensorflow"
os.environ['KERAS_BACKEND'] = backend
import argparse
from datadownload import download_celeb_a
from h5tool import create_celeba_channel_last
import glob
from PIL import Image

###################################################################
# Variables                                                       #
# When launching project or scripts from Visual Studio,           #
# input_dir and output_dir are passed as arguments.               #
# Users could set them from the project setting page.             #
###################################################################
input_dir = None
output_dir = None
log_dir = None


#################################################################################
# Keras configs.                                                                #
# Please refer to https://keras.io/backend .                                    #
#################################################################################
# import keras
from keras import backend as K

#K.set_floatx('float32')
#String: 'float16', 'float32', or 'float64'.

#K.set_epsilon(1e-05)
#float. Sets the value of the fuzz factor used in numeric expressions.

K.set_image_data_format('channels_last')
#data_format: string. 'channels_first' or 'channels_last'.


#################################################################################
# Keras imports.                                                                #
#################################################################################

from keras.models import Model
from keras.models import Sequential
from keras.layers import Input
from keras.layers import Lambda
from keras.layers import Layer
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.optimizers import SGD
from keras.optimizers import RMSprop
from train import *

def main():

    np.random.seed(config.random_seed)
    func_params = config.train

    func_name = func_params['func']
    del func_params['func']
    
    # call method train_gan located in train.py
    globals()[func_name](**func_params) 
    exit(0)


def images2h5(path2images,genre,imgWH):
    w,h=imgWH
    h5name=genre+"_"+str(h)+"by"+str(w)+".h5"
    h5path = os.path.join(os.getcwd(),'datasets',h5name);
    if os.path.exists(h5path):
        print(h5path+ "exists locally!")
        return

    print("Creating "+ h5path)
    glob_pattern = os.path.join(path2images, genre,'*.jpg')
    image_filenames = sorted(glob.glob(glob_pattern))
    num_images = len(image_filenames)
    print("there are %s images " %(num_images))
    
    for imgfn in image_filenames:
        print("loading "+ imgfn)
        img = Image.open(imgfn)
        #img = np.asarray(Image.open(imgfn))
        print ("original image size: ", img.size)
        img=img.resize((256,256),Image.ANTIALIAS)
        print ("resize image size: ", img.size)
        img = np.asarray(img)



path2images="../images/"    
imgWH=256,256
genre="landscape"
images2h5(path2images,genre,imgWH)

