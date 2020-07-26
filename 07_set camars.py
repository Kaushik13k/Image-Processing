# TO set the CAMARA PROPERTIES

import cv2

cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(3, 1208) #3 for height or"cv2.CAP_PROP_FRAME_WIDTH"
cap.set(4, 720) #4 for height or"cv2.CAP_PROP_FRAME_HEIGHT"

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', grey)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()