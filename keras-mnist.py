import numpy as np 
import keras as kr

# Import the mnist dataset from Keras
# The data, shuffled and split between train and test sets
# x_train, x_test - image data. y_train, y_test - labels
(x_train, y_train), (x_test, y_test) = kr.datasets.mnist.load_data()

# x_train and x_test are 3 dim with shape (60000, 28, 28) and (10000, 28, 28)
# Flatten x_train and x_test to 2 dim with shape (60000, 784) and (10000, 784)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
# The mnist import data is of type of uint8 so must be converted to float32 for use with Keras
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
