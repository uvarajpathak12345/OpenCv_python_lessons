import cv2 as cv

img = cv.imread('./data/homw.jpg')
cv.imshow("img" , img)

grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#simple threshold--->it converts the image into binary and compare its pixel value to its thres vale which is 150.
#if pixel is greater then 150 then it is set to 255 which is white
#if pixel is lesser then 150 then it is set to 0 which is black

threshold , thres = cv.threshold(grey, 150 , 255 , cv.THRESH_BINARY)
cv.imshow("Threshold" , thres)

threshold , thres_inv = cv.threshold(grey , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow("Threshold inv",thres_inv)

#adaptive threshold
absolute = cv.adaptiveThreshold(grey , 255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 15 , 10)
cv.imshow("Adaptive thres" , absolute)

#in adaptive threshold if the mean value (i.e mean value of 10 pixel of image ) is greater then 15 then it becomes 255, if not
#then it becomes 0

#(cv.AADAPTIVE_THRESH_GAUSSIAN_C)in gaussian blur methode it make the window of 10 and calculate the its pixel, therefore if the value is greater then 15 it becomes 25, if
# no then it gives  0




cv.waitKey(0)