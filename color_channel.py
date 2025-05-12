import cv2 as cv

def resize(frame):
    width =  int(frame.shape[1] * 0.5)
    height = int(frame.shape[0] * 0.5)

    dimension : tuple = (width , height)

    return cv.resize(frame ,dimension , interpolation=cv.INTER_AREA)

img = cv.imread("./data/homw.jpg")
resizing = resize(img)
cv.imshow("fimg",resizing)

cv.waitKey(0)