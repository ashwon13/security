import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')


vid = cv2.VideoCapture(0)

while(True):
      
    
    ret, frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    # cv2.line(frame,(0,0),(100,100),(0,255,0),10)
    # cv2.line(frame,(0,0),(511,511),(255,0,0),5)
    # font=cv2.FONT_HERSHEY_COMPLEX
    # cv2.putText(frame,"Ashwin",(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()