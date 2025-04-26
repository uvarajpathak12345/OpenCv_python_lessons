import cv2 as cv


img = cv.imread("./data/homw.jpg")
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

edge = cv.Canny(img , 125 , 175)


cv.imshow("edge" , edge)

cv.waitKey(0)