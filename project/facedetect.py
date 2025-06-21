import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
people = ["prajesh" , "yubaraj" , "rabin"]

reconize = cv.face.LBPHFaceRecognizer_create()
reconize.read("face_detect.yml")

haar_cascade = cv.CascadeClassifier("face.xml")


while True:
    isTrue , frame = capture.read()
    grey = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    img_rect = haar_cascade.detectMultiScale(grey , scaleFactor=1.1 , minNeighbors=2)

    for (x,y,w,h) in img_rect:
        img_roi = grey[y:y+h , x:x+h]
        label , prediction = reconize.predict(img_roi)
        print(f" we found the image of {people[label]} with the prediction of {prediction}")

        cv.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , thickness=3)
        cv.putText(frame , str(people[label]) , (30,30) , cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , thickness=1)

    cv.imshow("img" , frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv.destroyAllWindows()