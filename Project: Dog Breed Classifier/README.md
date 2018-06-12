# Convolutional Neural Network

[![N|Solid](http://cs231n.github.io/assets/nn1/neural_net2.jpeg)](http://cs231n.github.io/convolutional-networks/)

A ConvNet is made up of Layers. Every Layer has a simple API: It transforms an input 3D volume to an output 3D volume with some differentiable function that may or may not have parameters.


### Project Description

Welcome to the Convolutional Neural Networks (CNN) project! In this project, you will learn how to build a pipeline to process real-world, user-supplied images. Given an image of a dog, your algorithm will identify an estimate of the canine?s breed. If supplied an image of a human, the code will identify the resembling dog breed.

Along with exploring state-of-the-art CNN models for classification, you will make important design decisions about the user experience for your app. Our goal is that by completing this lab, you understand the challenges involved in piecing together a series of models designed to perform various tasks in a data processing pipeline. Each model has its strengths and weaknesses, and engineering a real-world application often involves solving many problems without a perfect answer. Your imperfect solution will nonetheless create a fun user experience!




### Dataset Description
Labeled dog images 
bottleneck features

### About CNNs

A ConvNet architecture is in the simplest case a list of Layers that transform the image volume into an output volume (e.g. holding the class scores)
There are a few distinct types of Layers (e.g. CONV/FC/RELU/POOL are by far the most popular)
Each Layer accepts an input 3D volume and transforms it to an output 3D volume through a differentiable function
Each Layer may or may not have parameters (e.g. CONV/FC do, RELU/POOL don?t)
Each Layer may or may not have additional hyperparameters (e.g. CONV/FC/POOL do, RELU doesn?t)

License
----

MIT


**Thank you!**

