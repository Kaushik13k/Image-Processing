import cv2

img = cv2.imread('abc.jpg', 1)
rows, col, ht = img.shape

matrix = cv2.getRotationMatrix2D((rows/2, col/2),0,0.5)
new_img = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img)
cv2.imwrite('image.jpg',  new_img)
cv2.waitKey(2000)

matrix = cv2.getRotationMatrix2D((rows/2, col/2),30,0.5)
new_img1 = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img1)
cv2.imwrite('image.jpg',  new_img1)
cv2.waitKey(2000)

matrix = cv2.getRotationMatrix2D((rows/2, col/2),45,0.5)
new_img2 = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img2)
cv2.imwrite('image.jpg',  new_img2)
cv2.waitKey(2000)

matrix = cv2.getRotationMatrix2D((rows/2, col/2),90,0.5)
new_img3 = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img3)
cv2.imwrite('image.jpg',  new_img3)
cv2.waitKey(2000)

matrix = cv2.getRotationMatrix2D((rows/2, col/2),125,0.5)
new_img4 = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img4)
cv2.imwrite('image.jpg',  new_img4)
cv2.waitKey(2000)

matrix = cv2.getRotationMatrix2D((rows/2, col/2),180,0.5)
new_img5 = cv2.warpAffine(img, matrix, (col,rows))

cv2.imshow('output', new_img5)
cv2.imwrite('image.jpg',  new_img5)
cv2.waitKey(2000)




cv2.destroyAllWindows()