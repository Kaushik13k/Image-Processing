import cv2

img = cv2.imread('abc.jpg', 1)
print(img)

cv2.imshow('image', img)
cv2.waitKey(5000)

rotate90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('image', rotate90)
cv2.waitKey(5000)
cv2.rotate()
rotate9 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('image', rotate9)
cv2.waitKey(5000)


rotate180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('image', rotate180)
cv2.waitKey(5000)
cv2.destroyAllWindows()