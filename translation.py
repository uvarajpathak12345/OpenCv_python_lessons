import cv2 as cv
import numpy as np

img = cv.imread("./data/homw.jpg")
cv.imshow("image" , img)


#transformation
def trans(img , x , y):
    translateM = np.float32([[1,0,x] , [0,1,y]])
    dimension = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , translateM ,dimension  )


#rotation
def rotate(img , angle ,roatePoint = None):
    (width , height) = img.shape[:2]

    if roatePoint is None:
        roatePoint = (width,height)
    
    rotateMat = cv.getRotationMatrix2D(roatePoint , angle , 1.0)
    dimension = (width , height)
    return cv.warpAffine(img , rotateMat , dimension)


#resize
resize = cv.resize(img , (400 , 400) , interpolation=cv.INTER_AREA)
cv.imshow("resize" , resize)


translation = trans(img , 100 ,200)
cv.imshow("translate" , translation)

rotation = rotate(img , 45)
cv.imshow("rotation" , rotation)


cv.waitKey(0)