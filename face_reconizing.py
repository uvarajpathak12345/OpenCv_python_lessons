import os
import cv2 as cv
import numpy as np


people = []
for i in os.listdir(r'F:\python cv2\train'):
    people.append(i)

print(people)

haar_cascade = cv.CascadeClassifier("face.xml")
face_reconizer = cv.face.LBPHFaceRecognizer_create()
face_reconizer.read("face_reconied_trained.yml")


img = cv.imread("./val/madonna/5.jpg")
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)


face_rect = haar_cascade.detectMultiScale(grey , scaleFactor=1.1 , minNeighbors=4)

for (x,y,w,h) in face_rect:
    face_img = grey[y:y+h , x: x+w]
    label , confidence = face_reconizer.predict(face_img)
    print(f"people of {people[label]} with the confidence of {confidence}")

    cv.putText(img , str(people[label]) , (30,30) , cv.FONT_HERSHEY_COMPLEX , 1 , (0,255 , 9) , thickness=2)
    cv.rectangle(img , (x,y) , (x+w , y +h) , (0,255,0) , thickness=2)


cv.imshow("img" , img)

cv.waitKey(0)