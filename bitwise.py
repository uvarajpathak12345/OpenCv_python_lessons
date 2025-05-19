import cv2 as cv
import numpy as np

blank = np.zeros((400,400) , dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30) , (370,370) , (255,255,25) , -1)
cv.imshow("rectnage", rectangle)

circle = cv.circle(blank.copy() , (200,200) , 200 , (255,255,255) , -1)
cv.imshow("circle" , circle)

#bitwise and (it give the image of intersect only)
bitwise_and = cv.bitwise_and(rectangle , circle)
cv.imshow("bitwise_and" , bitwise_and)

#bitwise or (it gives the full image including intersect)
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise_or",bitwise_or)

#bitwise XOR operator ---> (give the Non-intersecting part)
bitwise_xor = cv.bitwise_xor(rectangle , circle)
cv.imshow("bitwise_xor" , bitwise_xor)


#bitwise operator ---> (it give the invert image of the actual image )
rbitwise_not= cv.bitwise_not(rectangle)
cv.imshow("rectangle_not" , rbitwise_not)

cbitwise_not = cv.bitwise_not(circle)
cv.imshow("ciricle_not" , cbitwise_not)


cv.waitKey(0)