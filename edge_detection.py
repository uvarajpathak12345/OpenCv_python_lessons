import cv2 as cv
import numpy as np

img =cv.imread("./data/homw.jpg")

grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#laplacian -->(this methode calculate the mean of grey image which will be both negative and positive value )
#but the pixel of the image is always positive so we use absolute to make the -ve mean and canverted into image
lap = cv.Laplacian(grey , cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)



#sobel gradient magnitude representation
#sobel computes the gradient into two direction which is X and Y

sobelX= cv.Sobel(grey , cv.CV_64F , 1,0)
sobelY = cv.Sobel(grey , cv.CV_64F , 0  , 1)
cv.imshow("sobelx" , sobelX)
cv.imshow("shobely" , sobelY)


#combining the sobelX and SobelY
Combined = cv.bitwise_or(sobelX , sobelY)
cv.imshow("combined sobel" , Combined)

#canny
canny = cv.Canny(grey , 125 , 175)
cv.imshow("canny" , canny)

cv.waitKey(0)