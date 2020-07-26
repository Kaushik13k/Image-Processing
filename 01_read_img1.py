#READ, SHOW, WRITE an image
import cv2

img = cv2.imread('abc.jpg', 1)
#to read image
#0 to read as grey
#-1 unchanged
# 1 read in colour
print(img)

cv2.imshow('image', img)
#to show the image

cv2.waitKey(0)
#to make it stay

cv2.destroyAllWindows()

cv2.imwrite('lena_p.jpg', img) #"lena_p.jpg is the new name"
#to create another image with the changed name