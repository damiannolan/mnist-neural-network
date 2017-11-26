# MNIST Neural Network

This repository contains a [Flask Python](http://flask.pocoo.org/) Application which is intended to serve as a Back-End Server API used in conjunction with an Angular Client Application which can be found [HERE!](https://github.com/damiannolan/mnist-ngclient) 

The Flask App provides one end-point `/uploads` in which a function is called to take an image from the Request Object and make a prediction of the digit in the image. 

## Emerging Technologies - Project

An Artificial Neural Network written using Keras / Tensorflow for prediction of handwritten digits. The Neural Network is based on and has been trained and evaluated using the [MNIST Data Set of Handwritten Digits](http://yann.lecun.com/exdb/mnist/).

### MNIST Data Set

The MNIST data set of handwritten digits is a subset of a larger set available from [NIST](https://www.nist.gov/). MNIST contains a training set of 60,000 samples and test set of 10,000 samples. The digits have been size-normailised and centered in a fixed-size image - 28 x 28 pixels, with the digit itself being 20 x 20 in size.

A simple Python Flask app serving as a back-end.

## Prerequistes

[Tensorflow](https://www.tensorflow.org/)
[Keras](https://keras.io)
[Flask](http://flask.pocoo.org/)

