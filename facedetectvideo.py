import cv2 as cv

capture = cv.VideoCapture(0)

def resize (frame):
    width = 400
    height = 400
    dimension = (width , height)

    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)


while True:
    isTrue , frame = capture.read()

    haar_cascade = cv.CascadeClassifier("face.xml")
    face_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1 , minNeighbors=3)
    
    for (x,y,w,h) in face_rect:
        cv.rectangle(frame , (x,y) , (x+w , y+h) , (0,255,0) , thickness=4 )

    cv.imshow("video" , frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()

cv.destroyAllWindows()