# ObjectDetection
A program that let users to detect faces and eyes upon an image.

## This is how it looks like:
![Looks](https://github.com/Stetcha/images/mainpage.png)

### This program only detects faces and eyes on both static and live image.
![Results](https://github.com/Stetcha/images/elliot.png)

It has a graphic interface for a user to be able to change from one image to another image.
It has a button to browse an image in which you would like to detect objects from. If you know your image location, you can
simply enter it on the field-box and hit "View".

# Note:

### For static image:
* It only detect human faces on a frontal view.
* It may not detect eyes of other humans as the classifier used, detect an eye according to a visible eyeball.
* But one can work around ScaleFactor and minNeighbors to suit their preference.
* And to close the window hit any key (Except the power key).
 
### For live image:
* Just make sure you theres light around you for the classifier to be able to detect objects
* To close the window make sure to hit 'q' as other keys won't be able to.
 
### Library used are: opencv and tkinter and make sure to install them.
### If you are using python2 just do:
*For opencv: pip install opencv-python 
*For tkinter: pip install tk

### If you are using python3 just do:
*For opencv: pip3 install opencv-python 
*For tkinter: pip3 install tk

##To start the program: just run startup.py

