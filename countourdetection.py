import cv2 as cv
import numpy as np


img = cv.imread("./data/homw.jpg")
grey = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape , dtype="uint8")



# blur = cv.GaussianBlur(img , (5,5) , cv.BORDER_DEFAULT)
# edge = cv.Canny(blur , 125 , 175)

#if i dont want to use blur and egde then i can use the threshold method os opencv which works as the same of blue and egde
#it is used to reduce the number the edage which is minor and unwanted





threshold , thresh = cv.threshold(grey , 125 ,255 , cv.THRESH_BINARY)
#255 is the max value of threshold function
cv.imshow("thresh" , thresh)
'''
threshold remove the very minor compare to blur and canny
threshold acutlly binarize the image so cv.thres_binary is used to detect the pixel and compare between pixel and threshold value

125 is threshold value
if the pixel value of the image is less then 125 then it set the value 0 of black which is black itself but if the pixel value is more then 125
then it set the value of black to 255 which is white

like this it reduce the unwanted and minor edge
'''








contours , hierarchies = cv.findContours(thresh , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)
'''
RETR_LIST:
   Retrieves all contours without creating any parent-child relationships. All contours are at the same hierarchy level.
RETR_EXTERNAL:
   Retrieves only the outermost contours, ignoring any nested contours.
RETR_CCOMP:
   Organizes contours into a two-level hierarchy. The top level consists of the outer boundaries of the objects, while the second level consists of the boundaries of the holes inside.
RETR_TREE:
   Retrieves all contours and reconstructs a full hierarchy tree, including nested contours.

Hierarchies allow you to:
    Distinguish nested objects: Identify which contours are inside others.
    Process objects with holes: Separate the outer boundary of an object from its inner holes.
    Filter contours: Select specific contours based on their hierarchical level or relationship to other contours.

chain_approx_none is used because it gives all the contours and hierarchical value like it's coordinate including childs and parent
chain_approx_simple is used because it gives countours and hierarchical value of start point and end point

for example if line is drawn then and i used chain_approx_none is used then i get all the edge coordinate but if i use the chan_approx_simple
then i only get the start pont and end point

'''
#contours variable get all the x y coordinate of the edge whaich are in the image


#drawing contours on the black screen
cv.drawContours(blank , contours , -1 , (0 , 0 , 255) , 1)
# -1 indicates all the index to be drawn 
cv.imshow("bankCountours", blank)




print(f'{len(contours)} found!')


cv.waitKey(0)