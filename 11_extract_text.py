
#Before trying this programme DO INSTALL THE SOFTWARE CALLED "TESSERACT"
#GOOGLE TESSERACT AND YOUR ARE GOOD TO GO!!

import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' #The LOCATION where the TESSERACT.EXE is available!
from PIL import Image
import cv2

im = cv2.imread('abc.jpg', 1)
img = Image.open('abc.jpg') #Here the image is read using the command PIL
text = tess.image_to_string(img) #To extract the text form image
print(text)

cv2.imshow('abc.jpg', im)
cv2.waitKey(5000)

cv2.destroyAllWindows()