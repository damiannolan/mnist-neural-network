# Damian Nolan - https://github.com/damiannolan
# MNIST Dataset - Neural Network for handwritten digits using Keras - a high-level neural networks API
# Adapted from:
#   Keras Examples - https://github.com/fchollet/keras/tree/master/examples
#   Dr. Ian McLoughlin - https://github.com/emerging-technologies/keras-iris

import numpy as np 
import keras as kr

batch_size = 128
epochs = 5
num_classes = 10

# Import the mnist dataset from Keras
# The data, shuffled and split between train and test sets
# x_train, x_test - image data. y_train, y_test - labels
(x_train, y_train), (x_test, y_test) = kr.datasets.mnist.load_data()

# x_train and x_test are 3 dim with shape (60000, 28, 28) and (10000, 28, 28)
# Flatten x_train and x_test to 2 dim with shape (60000, 784) and (10000, 784)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
# The mnist import data is of type of uint8 so must be converted to float32 for use with Keras models
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
# Divide elements of x_train and x_test by 255 to make them values between 0-1
x_train /= 255
x_test /= 255

print('Training samples: %d' % x_train.shape[0])
print('Test samples: %d' % x_test.shape[0])

# Using Keras utils - to_categorical convert the labels to binary class matrices
# This is for use with categorical_crossentropy and classification of digits 0-9
# E.g. The label y_train[0] of 5 will now be represented as a vector - [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]
# This is also known as One-Hot encoding where we start from 0 and go all the way up to N-1 categories
# See: https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f
y_train = kr.utils.to_categorical(y_train, num_classes)
y_test = kr.utils.to_categorical(y_test, num_classes)

# Create a neural network using Keras' Sequential Model
# Ref: https://keras.io/getting-started/sequential-model-guide/
# The Model is a linear stack of layers which define a neural network
# This encapsulates training, evaluation and predictions similarly to Tensorflow Estimators
# See: https://www.tensorflow.org/versions/r1.3/programmers_guide/estimators
model = kr.models.Sequential()

# Add an initial layer of 512 hidden nodes with input_shape 784
# Add a second layer of 512 hidden nodes
# These layers apply the Sigmoid activation function
# Add the ouput layer with 10 nodes - one per class/digit
# Apply Softmax activation function
# Softmax regression is very commonly used in ML for multi-class classification 
#   - assuming classes are mutually exclusive. 
model.add(kr.layers.Dense(512, activation='sigmoid', input_shape=(784,)))
model.add(kr.layers.Dense(512, activation='sigmoid'))
model.add(kr.layers.Dense(num_classes, activation='softmax'))

# Use Model Summary to display a summary in the terminal
model.summary()

# Configure the model for training.
# Use Adam Optimizer & Categorical cross entropy as the loss function.
# Add in some extra metrics - accuracy being the only one.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model using our training data.
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

# Evaluate the model using the test data set.
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
# Output the accuracy of the model.
print('\n\nLoss: %6.4f\tAccuracy: %6.4f' % (loss, accuracy))

# Save the model
model.save('mnist-neural.h5')