
#This code is for extracting colour and masking!!

import cv2
import numpy as np
import imutils
from skimage.io import imread, imshow


img = cv2.imread('lena_p.jpg')
kau = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #converting RGB to HSV
                                            #Because RGB canr split colours and HSV can convert colours

LR = np.array([0, 100, 100]) #LowerRange or "hsv"code
UR = np.array([5,255,255]) #UpperRange or "rgb"code
#Above code is for colourRED....

crop = cv2.inRange(kau, LR, UR) #To mask the Red colour from rest

cv2.imshow('image', img)
cv2.imshow('mask', crop)
cv2.waitKey(0)

#while(True):
   #k = cv2.waitKey(5) & 0xFF
   #if k == 27:
      #break
cv2.destroyAllWindows()
