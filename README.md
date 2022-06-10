# Computer_Vision_Mini_Projects  
This repository is a collection of 5 mini projects on computer vision.  All the images used in the projects can be found within the folder `images`.  

**Requirements**
For running the code, the following packages are needed:  
python == 3.8.13  
open cv == 4.5.5  
matplotlib == 3.5.1  
torchvision == 1.11.0


## Image annotation
This mini project is about drawing bounding box around objects in an image together with the corresponding label.  


## QR Code reader
The aim of this miniproject is to create a function to read and print out the content of a QR Code, find the area where the code is located on the image and draw a bounding box around it.  

 
  
## Green screen
This project goes through how to remove a green backround from an image and replace it with another background of your choice. 


## Handwritten digits
This project seeks to recognize handwritten digits. The objective is to load an image containing handwritten digits, recognize those digits and print out a string version of those.  
*NB*: All steps needed to complete the tasks are defined, however the image preprocessing step needs more refinement so that the digits comply with those in the MNIST dataset on which the CNN model has been trained on. 

Steps to run the script in the command line are:  
* `cd <handwritten_digits folder>`
* `python handwritten_recognition.py <path_to_image_with_handwritten_digits>`






 
