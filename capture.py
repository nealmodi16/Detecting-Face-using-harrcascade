import cv2
import time
import numpy as np
cap= cv2.VideoCapture(1)
face_Cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml')
kernel = np.array([[-1,-1,-1], 
                   [-1, 10,-1],
                   [-1,-1,-1]])
import os
while True:
     ret,frame = cap.read()
     
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
     #gray1=cv2.equalizeHist(gray)
     
     #gray2 = cv2.filter2D(gray, -10, gray)
     #cv2.imshow('frame',gray2)
     #cv2.waitKey(1)
     hell = face_Cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
     for (x,y,w,h) in hell :
         #roi_gray = gray[y:y+h+100,x:x+w+10]
         roi_color=frame[y:y+h,x:x+w]
         #imgsc=cv2.resize(roi_color,(900,900),interpolation=cv2.INTER_CUBIC)
         #img=cv2.resize(imgsc,None,fx=0.75,fy=0.75)
         #cv2.imwrite('pic'+str(count)+'.png', roi_gray)
         #count =count + 1
         color = (0,0,255)
         stroke =3
         endx= x+w
         endy=y+h
         cv2.rectangle(roi_color,(x,y),(endx,endy),color,stroke)
         cv2.imshow('frame3',frame)
         cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
