import cv2 as cv
import numpy as np


window = np.zeros((500,500, 3) , dtype="uint8")
# cv.imshow("blank" , window)
#3 means it takes the 3 color which is BRG


# window[200:300 , 300:400] = 0,255,0
# cv.imshow("green" , window)

# creating an rectngle
# cv.rectangle(window , (50,50) , (window.shape[1] //2 , window.shape[0] //2) , (0,250,250) , thickness=-1)
# cv.imshow("rectagle" , window)


#creating a circle
# cv.circle(window , (window.shape[1] //2 , window.shape[0] //2) ,100 , (0,255,200) , thickness=-1 )
# cv.imshow("circle" , window)

#drawing a line

# cv.line(window , (0,0) , (window.shape[1] //2 , window.shape[0] //2) , (255,255,255) , thickness=3)
# cv.imshow("line" , window)


cv.putText(window, "hello! world" , (200 , 255) , cv.FONT_HERSHEY_TRIPLEX , 1 , (0,255,0) , thickness=1)
cv.imshow("line" , window)

cv.waitKey(0)