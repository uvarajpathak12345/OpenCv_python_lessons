import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./data/homw.jpg")


# plt.imshow(img)
# plt.show()




# #bgr to grey
# grey  = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# #bgr to hsv
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("hsb" , hsv)

# #bgr to lAB
# lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)

# cv.waitKey(0)

#bgr to rgb
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.show()

