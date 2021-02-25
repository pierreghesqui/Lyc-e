import numpy as np
import cv2

img = np.zeros((100,100))

cpt = 0

while cpt<100 :  
    img[25,cpt] = 255
    cpt = cpt+1
    cv2.imshow('image',img) # Afficher l'image img
    cv2.waitKey(100)        # Attendre 100ms avant de continuer
    

 