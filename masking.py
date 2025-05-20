import cv2 as cv
import numpy as np


img = cv.imread("./data/homw.jpg")
cv.imshow("img", img)

#for creating masking it should be the same size of the real image which is going to be masking
blank = np.zeros((img.shape[0] , img.shape[1]) , dtype='uint8')


#creating a circle and other object to maske on the circle
circle = cv.circle(blank.copy() , (img.shape[1] //2 , img.shape[0] //2) , img.shape[0] //2 , 255 , -1)
cv.imshow("circle" , circle)


rectangle = cv.rectangle(blank.copy() , (100 , 100) , (img.shape[1] - 100 , img.shape[0] - 100) , 255 , -1)
cv.imshow("rectangle",rectangle)


#combining rectangle and circle and displaying the intersecting
circle_rectnagle = cv.bitwise_and(rectangle ,circle)
cv.imshow("intersect" , circle_rectnagle)


#masking
biwise_and = cv.bitwise_and(img , img , mask=circle)
cv.imshow("masking ", biwise_and)


#masking in the intersect part
intersect_mask = cv.bitwise_and(img , img , mask=circle_rectnagle)
cv.imshow("intersect_mask" , intersect_mask)


'''
for example i want to mask the img in rectangle then in bitwise oprator i should use the img, img two source image same 
as given above and mask = (add the those item ,img is going to be masked)
 
'''
cv.waitKey(0)