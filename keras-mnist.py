import numpy as np 
import keras as kr

# Import the mnist dataset from Keras
# The data, shuffled and split between train and test sets
# x_train, x_test - image data. y_train, y_test - labels
(x_train, y_train), (x_test, y_test) = kr.datasets.mnist.load_data()