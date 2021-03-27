import numpy as np
import cv2
import keyboard

img = np.zeros((500,500))
monObjetLigne   = 100
monObjetColonne = 300
monObjetHauteur = 50
monObjetLargeur = 75
img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1

while not keyboard.is_pressed('ctrl'):
    
    cv2.imshow('image1',img)
    cv2.waitKey(100)
    
    if keyboard.is_pressed('left'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetColonne = monObjetColonne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
    
    elif keyboard.is_pressed('right'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetColonne = monObjetColonne+10
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0

    
    elif keyboard.is_pressed('up'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetColonne = monObjetColonne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1

    
cv2.destroyWindow("image1")





