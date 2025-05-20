import cv2 as cv

img = cv.imread("./data/male.jpg")

grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)


haar_cascade = cv.CascadeClassifier("face.xml")

face_rec = haar_cascade.detectMultiScale(grey , scaleFactor=1.1 , minNeighbors= 3)


for x,y,w,h in face_rec:
    cv.rectangle(img , (x,y) , (x+w,y + h) , (0,255,0) , thickness=3)
cv.imshow("face_detect", img)

cv.waitKey(0)