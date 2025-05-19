'''
Histograms allows you to visualize the pixel intensity in an image wheather its grey image, or rgb image
'''

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("./data/homw.jpg")
blank = np.zeros((img.shape[0] , img.shape[1]) , dtype='uint8')
cv.imshow("img" , img)

#grey scale Image
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("grey" , grey)

#masking the image to find the histogram from maskig image
circle = cv.circle(blank.copy() , (img.shape[1]//2 ,img.shape[0] //2) , img.shape[0] //2  , 255 , -1)
cv.imshow("circle" , circle)

mask = cv.bitwise_and(grey , grey , mask=circle)
cv.imshow("mask" , mask)


#histogram of grey scale image (o is used in the place of channel because it indicates the grey color)
grey_hist = cv.calcHist([grey] , [0] , mask  , [256] , [0,256] )

# plt.figure()
# plt.title("Grey Scale histogram")
# plt.xlabel("Bins")
# plt.ylabel("Number of pixels")
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram

color = ("b" , "g" , "r")


plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixel")
for i,col in enumerate(color):
    histo = cv.calcHist([img] , [i] , None , [256] , [0,256])
    plt.plot(histo , color = col)
    plt.xlim([0 , 256])
    
plt.show()






cv.waitKey(0)