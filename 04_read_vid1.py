#READ, WRITE, SHOW video
import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID') #fourcc code fourcc.org/codecs.php
out = cv2.VideoWriter('ootput.avi', fourcc, 20.0, (640,480))#fourcc is 4 bite code used to specify video coddec ,
                                                                # "20.0" is frames per sec

#capture from main cam is"0"
print(cap.isOpened()) #to check if it exist

while(cap.isOpened()):
    ret,frame = cap.read() #ret will store true or false

    if ret == True:
        cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        out.write(frame)

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# convert video into grey
        cv2.imshow('frame', grey)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()