#Anoter waw to read an image
import cv2

img = cv2.imread('lena.jpg', 0)
print(img)

cv2.imshow('image', img)

k=cv2.waitKey(0)

if k ==27: #27==esc key
    cv2.destroyAllWindows()
elif k == ord('s'): #"ord" is to give any "key"...like ive given "s"
    cv2.imwrite('lena_p.jpg', img)
    cv2.destroyAllWindows()
