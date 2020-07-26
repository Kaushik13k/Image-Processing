#TO get an REAL, GREY, B/W image

import cv2

kkk = cv2.imread('abc.jpg')
grey = cv2.cvtColor(kkk, cv2.COLOR_BGR2GRAY) #To convert an colour image to GREY image

(thresh, BW) = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY) #HERE we use Grey image to convert to B/W image coz of thershold value...
                                                                    #127 is minimum threshhold value; 255 is max thershold value...
cv2.imshow('Black white image', BW)
cv2.imshow('Original image', kkk)
cv2.imshow('Gray image', grey)

cv2.waitKey(0)
cv2.destroyAllWindows()