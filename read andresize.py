import cv2 as cv
capture = cv.VideoCapture(0)

def resize(frame , size = 0.5):
    width: int = int(frame.shape[1] * size)
    height : int = int(frame.shape[0] * size)
    dimension: tuple = (width , height)

    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

while True:
    isTrue , frame = capture.read()
    reframe = resize(frame)

    cv.imshow("video" , frame)
    cv.imshow("Re Video" , reframe)
 
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
