import cv2
import numpy as np
import sys

facePath = "opencv-master/data/haarcascades/haarcascade_frontalface_default.xml"
smilePath = "opencv-master/data/haarcascades/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)
eye_cascade = cv2.CascadeClassifier('opencv-master/data/haarcascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05
cam = cv2.VideoCapture(0)
while True:

    ret, img = cam.read() # Capture img-by-img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    # ---- Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale( 
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25),
        )
        for (sx, sy, sw, sh) in smile:
            print ("Found", len(smile), "smiles!")
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 1)
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            print ("Found", len(eyes), "eyes!")
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    cv2.imshow('my webcam', img)
    if cv2.waitKey(1) == 27:
        break
cam.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()