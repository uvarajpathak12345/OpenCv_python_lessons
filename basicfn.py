import cv2 as cv

img = cv.imread("./data/homw.jpg")

#resize function
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
dimenion = (width , height)
resize = cv.resize(img ,dimenion ,interpolation=cv.INTER_AREA)



#grey function
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#blur
blur = cv.GaussianBlur(img , (3,3), cv.BORDER_DEFAULT)

#EDGE canny (anny lee edge heru detect garna ko lagi use  hunxa) default value vaneko jailey ni  125 rw 175 hunxa aaba depends upon on programme
edge = cv.Canny(blur , 125 , 175)

#cropped
cropped = img[100:300 , 300: 400 ]






cv.imshow("img" , grey)


cv.waitKey(0)