# MNIST Neural Network - A Python Flask Server Application

## Overview

An Artificial Neural Network written using Keras / Tensorflow for prediction of handwritten digits. The Neural Network is based on and has been trained and evaluated using the [MNIST Data Set of Handwritten Digits](http://yann.lecun.com/exdb/mnist/).

This repository contains a [Flask Python](http://flask.pocoo.org/) Application which is intended to serve as a Back-End Server API used in conjunction with an Angular Client Application which can be found [HERE!](https://github.com/damiannolan/mnist-ngclient) 

The Flask App provides one end-point `/uploads` in which a function is called to make a prediction of the image passed in the request object and return that prediction to the client. The application employs [Pillow](https://pypi.python.org/pypi/Pillow/2.2.1) and [Numpy](http://www.numpy.org/) in order to manipulate the image converting it to grayscale, resizing and transforming to an array of pixels in prepartion for passing it to the Model for prediction.

## MNIST Data Set

The MNIST data set of handwritten digits is a subset of a larger set available from [NIST](https://www.nist.gov/). MNIST contains a training set of 60,000 samples and test set of 10,000 samples. The digits have been size-normailised and centered in a fixed-size image. This application employs the MNIST data set in order to train, evaluate and predict using a [Keras](https://keras.io) Neural Network Model.

## Neural Networks

A more detailed tutorial on Neural Networks can be found in another one of my repositories that is located [HERE!](https://github.com/damiannolan/iris-neural-network) The repository contains a Jupyter Notebook in which an artifical neural network is used to train a model for predicting species of Iris Flower. The same logic is applied in this application as it also deals with categorical data.

## Prerequistes

As this is a Python based application, Python is a must and can be downloaded from the [Anaconda](https://www.anaconda.com/download/) open distribution which includes all of the . If you are on OSX you can simply install Python using [Homebrew](https://brew.sh/).
```
brew install python3
```

And install additional dependencies such as SciPy and Pillow as needed using the pip package manager.

```
pip3 install scipy
```

```
pip3 install Pillow
```

In order to use the Model file `minst-neural.h5` that is included in this repository you may also need to install [h5py](http://docs.h5py.org/en/latest/build.html) for dealing with the file format of the Model.

```
pip3 install h5py
```

Follow the instructions at the following URLs for installing these dependcies.

- [Tensorflow](https://www.tensorflow.org/install)

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

## Building the Model

This repository already includes a h5 Model file - `mnist-neural.h5`. However should you want to rebuild the model using the associated Keras script please run `python3 keras-mnist.py`. For the purpose of speed and effiency the model is loaded using `load_model` in the `app.py` Flask script. Building a new Model everytime the server is started is unnecessary and will slow down the application starting.
