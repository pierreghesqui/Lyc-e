import numpy as np
import cv2

img = np.zeros((900,900,3))
img[:,:,1:3]=0.2
cpt = 0

while cpt<900:
    img[cpt,:]= 0
    img[:,cpt]= 0
    cpt = cpt+100

cv2.imshow('test',img)    
cv2.imwrite('imgTest.png',img*255)