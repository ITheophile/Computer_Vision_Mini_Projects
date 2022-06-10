# Computer_Vision_Mini_Projects  
This repository is a collection of 5 mini projects on computer vision.  All the images used in the projects can be found within the folder `images`.  

**Requirements**  
For running the code, the following packages are needed:  
python == 3.8.13       (all projects)  
open cv == 4.5.5       (all projects)  
matplotlib == 3.5.1    (all projects)  
torchvision == 1.11.0  (handwritten_digits)   
argparse == 1.1         (handwritten_digits)  


## Image annotation
This mini project is about drawing bounding box around objects in an image together with the corresponding label.  


## QR Code reader
The aim of this miniproject is to create a function to read and print out the content of a QR Code, find the area where the code is located on the image and draw a bounding box around it.  

 
  
## Green screen
This project goes through how to remove a green backround from an image and replace it with another background of your choice.  
For illustration of how it works see pictures below:  
[!green_background](images/green_background.png)


## Handwritten digits
This project seeks to recognize handwritten digits. The objective is to load an image containing handwritten digits, recognize those digits and print out a string version of those.  
*NB*: All steps needed to complete the tasks are defined, however the image preprocessing step needs more refinement so that the digits comply with those in the MNIST dataset on which the CNN model has been trained on. 

An example of how to run the script from the command line is:  
* `cd <handwritten_digits>`
* `python recognize_digits.py <'..\images\numbers.jpg'>`

*NB*: Argument in `<...>` depends on your file system structure.  
Also, the script expects 6 digits. Of course, this will be changed to accept any number of sequential digits
