import cv2 as cv
import numpy as np


def resize(frame):
    width =  int(frame.shape[1] * 0.5)
    height = int(frame.shape[0] * 0.5)

    dimension : tuple = (width , height)

    return cv.resize(frame ,dimension , interpolation=cv.INTER_AREA)


img = cv.imread("./data/homw.jpg")
resizing = resize(img)
blank = np.zeros(resizing.shape[:2] , dtype="uint8")


#to split the bgr color we use split methode in openCv

b,g,r = cv.split(resizing)

blue = cv.merge([b,blank , blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


#display the b,g,r color photo
cv.imshow("blue" , blue)
cv.imshow("red" , red)
cv.imshow("green" , green)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

marge = cv.merge([b,g,r])
cv.imshow("merge", marge)

#merge the b,g,r color, use merge methode in openCv



cv.imshow("fimg",resizing)
cv.waitKey(0)