#Task 5 - Image Maths
#Transformation Notes
#Code written by Laura Whelan on 12/10/2020

#==========================================
#This code sclaes two images and adds them together to get a composite image
#==========================================

#import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#1. Open image 
Io = cv2.imread("Orange.png")
Iw = cv2.imread("Water.jpg")

#Scale each image to 50 % by multiplying each by 0.5;
ho,wo,do =Io.shape
print ("The height of the orange image is ", ho)
print ("The width of the orange image is ", wo)
#Ios=cv2.resize(Io,dsize=(0.5*wo,0.5*ho))
Ios=cv2.resize(Io,dsize=(int(wo/2),int(ho/2)))

hw,ww,dw =Iw.shape
print ("The height of the water image is ", hw)
print ("The width of the water image is ", ww)
#Iws=cv2.resize(Iw,dsize=(0.5*ww,0.5*hw))
Iws=cv2.resize(Iw,dsize=(int(ww/2),int(hw/2)))

#3.Add the two scaled images to get a composite image;
Added =cv2.add(Io,Iw) 
#4.Adjust the scaling to give a nicer output
Added2=Added*0.5
Added2=Added2.astype('uint8') #When you multiply by a scalar value that is not an integer, you need to set the image back to uint8 format


#Advanced task: investigate the addWeighted function to achieve the same
Orange_weight=.7
Water_weight = (1.0 - Orange_weight)
gamma = 0 #the higher this value the more white-washed the image
Added_scaled_weighted = cv2.addWeighted(Io, Orange_weight, Iw, Water_weight, gamma)

cv2.imshow("Orange",Ios)
cv2.imshow("Water",Iws)
cv2.imshow("Watery Orange Added",Added)
cv2.imshow("Watery Orange Added and scaled",Added2)
cv2.imshow("Watery Orange Weighted",Added_scaled_weighted)
key =cv2.waitKey(0)



#S =cv2.subtract(Ios,Iws) #testing out subtraction
#M =cv2.multiply(Ios,Iws,scale =0.01) #testing out multiplication
#D =cv2.divide(Ios,Iws,scale =100) #testing out division