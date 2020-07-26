#To draw the shape in an image

import numpy as np
import cv2

img = cv2.imread('lena.jpg', 0)
#img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 10) #(0,0) = STARTING POINT ; (255,255) = ENDING POINT ; (255,0,0) = BGR(BLUE, GREEN, RED) ; 10= THICKNESS
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)
img = cv2.rectangle(img, (380,0), (510,210), (255,0,0), 10)
img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

font = cv2.FONT_ITALIC #Font style
img = cv2.putText(img, 'hello kau', (10,500), font,4, (255,255,255), 5, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(5000)

cv2.destroyAllWindows()


