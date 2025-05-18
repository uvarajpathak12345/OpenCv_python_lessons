import cv2 as cv

def resize(frame):
    width = int(frame.shape[1] * 0.5)
    height = int(frame.shape[0] * 0.5)
    dimension = (width , height)
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

demo = cv.imread('./data/homw.jpg')
img = resize(demo)
cv.imshow("img" , img)

#Actually Blur Methode is used to reduce the Noise From the Image But mainly median blur is used to reduce the noice from the image

#average blur
average = cv.blur(img , (3,3))
cv.imshow("average blur" , average)

#Gaussian Blur (in here we also have to put the value of the sigmaX which is deviation value)
guss = cv.GaussianBlur(img, (3,3) , 0)
cv.imshow("gaussian Blur" , guss)

#Median blur (for median blur we have to use the 3 int value value rather than (3,3))
medain = cv.medianBlur(img , 3)
cv.imshow("Median Blur" , medain)

#biletral blur 
bilteral = cv.bilateralFilter(img , 3 , 15 ,15)
cv.imshow("bileteral Blur" , bilteral)


cv.waitKey(0)