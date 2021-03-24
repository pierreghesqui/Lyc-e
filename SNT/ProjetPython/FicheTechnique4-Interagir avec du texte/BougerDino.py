import numpy as np
import cv2
import keyboard 


img = np.zeros((600,500))

# Ennemi1
DinoLigne = 300
DinoColonne = 100
DinoHauteur = 50
DinoLargeur = 50
img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 1

#IndicateurTrajectoireDino
dinoJump = 0
dinoUp = 1
ligneLimiteUp = 100
ligneLimiteDown = 300

while not keyboard.is_pressed('ctrl'):

    cv2.imshow('image1',img)
    cv2.waitKey(10)
    
    if keyboard.is_pressed('space'):
        dinoJump = 1
    
    #DinoMove
    if dinoJump == 1 and dinoUp==1 :
        img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 0
        DinoLigne = DinoLigne-10
        img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 1
        if DinoLigne<ligneLimiteUp : 
            dinoUp=0
        
    elif dinoJump == 1 and dinoUp==0:
        img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 0
        DinoLigne = DinoLigne+10
        img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 1
        if DinoLigne>ligneLimiteDown : 
            dinoJump = 0
            dinoUp = 1
        
cv2.destroyWindow('image1')













