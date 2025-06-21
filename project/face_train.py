import os
import cv2 as cv
import numpy as np

people = ["prajesh" , "yubaraj" , "rabin"]
DIR = r"F:\python cv2\project\face"
haar_cascade = cv.CascadeClassifier("face.xml")
features = []
labels = []

def Train_data():
    for person in people:
        path = os.path.join(DIR , person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path , img)
            photo = cv.imread(img_path)
            grey = cv.cvtColor(photo , cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(grey , scaleFactor=1.1 , minNeighbors=2)

            for (x,y,w,h) in face_rect:
                img_roi = grey[y:y+h , x:x+w]
                features.append(img_roi)
                labels.append(label)
Train_data()
print("Tranning Data success ------------------------>")
features = np.array(features , dtype="object")
labels = np.array(labels ,dtype="int")

Reconize = cv.face.LBPHFaceRecognizer_create()
Reconize.train(features , labels)
Reconize.save("face_detect.yml")
print("heek")
np.save("features.npy" , features)
np.save("labels.npy" , labels)


