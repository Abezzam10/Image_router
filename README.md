# Image_router
A simple web application to classify images into categories described.

This is an interactive convolutional neural network on a website. The aim of this project is to feed in an image and run it through a CNN at the backend to display the best possible classification for the uploaded image.

The web app is segregated into 2 parts: Front-end and Back-end. Front-end runs on a microservice with routes on Flask and the backend runs on Tensorflow and Keras.

The application runs on Flask as the primary web interface and the CNN's are implemented on a Tensorflow backend. Bokeh is used to give a visual description of the classification. 

Setup:

I am using a virtual environment to manage my dependancies.

`$ mkdir ~/venvs/`
`$ virtualenv ~/venvs/appname`
... # some output messages

`$ source ~/venvs/das/bin/appname`
`(das) $ which pip
/home/das/venvs/bin/pip`

Then,
pip3 install these dependancies,
1. hdf5
2. imageio
3. flask
4. Bokeh
5. TensorFlow
6. Keras


Once, all the dependancies are installed and cloned, run `FLASK_APP=server.py flask run`

The sample dataset I have used to get the images and train them are on sample aws s3 buckets. I imported them locally and trained the models on it.

Project status until I resolve deployment:

![HomePage](https://github.com/Abezzam10/Image_router/blob/master/Imgs/Home.png)


After uploading your image, simply click on Submit to predict the image.

![Predict](https://github.com/Abezzam10/Image_router/blob/master/Imgs/example.png)
