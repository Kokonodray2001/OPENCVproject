  2import cv2 as cv
#import time
vid = cv.VideoCapture(0)#object of videocap
while True:
    check,frame  = vid.read()#create a frame obj
    print(check)
    cv.imshow('press x to exit and c to capture',frame)#create the frame
    k = cv.waitKey(1)
    print(frame)#real time image matrix
    if(k==ord('c')):
        cv.imwrite('a.jpeg',frame)m,,m
    if k == ord('x'):
        break
vid.release()
cv.destroyAllWindows()
#stop the cam
import numpy as np 
img  = cv.imread('a.jpeg')
#img.shape
Z = img.reshape((-1,3))
Z = np.float32(Z) 
criteria = (cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,10,1.0) 
K=6
ret,label,center = cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
center  = np.uint8(center)
result  =  center[label.flatten()]
result = result.reshape(img.shape)
result= cv.resize(result,(650,650))
img = cv.resize(img,(650,650))
cv.imshow('res',img)
cv.waitKey(0)
cv.imshow('res1',result)
cv.waitKey(0)
cv.destroyAllWindows()
