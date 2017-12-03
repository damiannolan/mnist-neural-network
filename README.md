# MNIST Neural Network - A Python Flask Server Application

## Overview

An Artificial Neural Network written using Keras / Tensorflow for prediction of handwritten digits. The Neural Network is based on and has been trained and evaluated using the [MNIST Data Set of Handwritten Digits](http://yann.lecun.com/exdb/mnist/).

This repository contains a [Flask Python](http://flask.pocoo.org/) Application which is intended to serve as a Back-End Server API used in conjunction with an Angular Client Application which can be found [HERE!](https://github.com/damiannolan/mnist-ngclient) 

The Flask App provides one end-point `/uploads` in which a function is called to make a prediction of the image passed in the request object and return to that prediction to the client.

## MNIST Data Set

The MNIST data set of handwritten digits is a subset of a larger set available from [NIST](https://www.nist.gov/). MNIST contains a training set of 60,000 samples and test set of 10,000 samples. The digits have been size-normailised and centered in a fixed-size image. This application employs the MNIST data set in order to train, evaluate and predict using a [Keras](https://keras.io) Neural Network Model. 

## Prerequistes

As this is a Python based application, Python is a must and can be downloaded from the [Anaconda](https://www.anaconda.com/download/) open distribution which includes all of the . If you are on OSX you can simply install Python using [Homebrew](https://brew.sh/) and install dependencies such as SciPy and Pillow as needed using the pip package manager.

```
brew install python3
```

```
pip3 install scipy
```

```
pip3 install Pillow
```

Follow the instructions for installing the following dependcies.

- [Tensorflow](https://www.tensorflow.org/)

- [Keras](https://keras.io)

- [Flask](http://flask.pocoo.org/)

## Getting Started

1. Clone this repository

```
git clone https://github.com/damiannolan/mnist-neural-network.git
```

2. Start the server application

```
python3 app.py
```