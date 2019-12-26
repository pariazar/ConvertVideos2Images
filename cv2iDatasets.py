# This Tool design by Hamed Pariazar 2019
#https://github.com/hamedpa
import cv2
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import uuid
from PIL import Image

# Default inputs
hasImageCompress = "n"
vQuality = 100
frameR = 10
seconds = 10

# Get Inputs from user 
videoFormat = input("format of your video (Example: mp4) : ")
imagesFormat = input("format of your images (Example: jpg) : ")
path = input("please enter a path that your videos exist there : ")
imagesPath = input("please enter directory path that you want images save there : ")
frameR = input("please enter frame Rate : ")
seconds = input("Please enter seconds for the video to start : ")

if imagesFormat=="jpg" or imagesFormat=="jpeg":
    hasImageCompress = input("do you need to resize images (n/y) : ")
    if hasImageCompress == "y":
        sw = input("enter width (Example: 200) : ")
        sh = input("enter hight (Example: 200) : ")
        vQuality = input("enter quality (Example: 90) : ")
    





def getFrameWithResize(sec,file):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        fileName = "images/"+file+str(uuid.uuid1())+str(count)+"."+imagesFormat
        cv2.imwrite(fileName, image)     # save frame as JPG file
        im = Image.open(fileName)
        f, e = os.path.splitext(fileName)
        imResize = im.resize((int(sw),int(sh)), Image.ANTIALIAS)
        imResize.save("images/"+file+'_resized'+str(uuid.uuid1())+str(count)+"."+imagesFormat, 'JPEG', quality=int(vQuality))
        if os.path.exists(fileName):
              os.remove(fileName)
    return hasFrames    

def getFrame(sec,file):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        fileName = "images/"+file+str(uuid.uuid1())+str(count)+"."+imagesFormat
        cv2.imwrite(fileName, image)     # save frame as JPG file
        im = Image.open(fileName)
    return hasFrames   

path = path + "/"

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith("."+videoFormat):
                        vidcap = cv2.VideoCapture(path+file)
                        sec = int(seconds)
                        frameRate = int(frameR) #//it will capture image in each 0.5 second
                        count=1
                        if hasImageCompress == "y":
                            success = getFrameWithResize(sec,file)
                        else:
                            success = getFrame(sec,file)
                            
                        while success:
                            count = count + 1
                            sec = sec + frameRate
                            sec = round(sec, 2)
                            success = getFrame(sec,file)


print(videoFormat)