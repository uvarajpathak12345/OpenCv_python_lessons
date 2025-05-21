import os
import cv2 as cv
import numpy as np

people = []

for i in os.listdir(r'F:\python cv2\train'):
    people.append(i)

DIR = r"F:\python cv2\train"
haar_cascade = cv.CascadeClassifier("face.xml")


features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR , person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path , img)
            img_array = cv.imread(img_path)
            grey = cv.cvtColor(img_array , cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(grey , scaleFactor=1.1 , minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = grey[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Tranning data successfull ------------------>")


features = np.array(features , dtype="object")
labels = np.array(labels , dtype="int")

face_reconizer =  cv.face.LBPHFaceRecognizer_create()
face_reconizer.train(features , labels)
face_reconizer.save("face_reconied_trained.yml")

np.save("features.npy" ,features)
np.save("labels.npy" , labels)

