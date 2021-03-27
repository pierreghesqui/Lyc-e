import numpy as np
import cv2
import keyboard 

img = np.zeros((600,500))

# Dinosaure
DinoLigne = 300
DinoColonne = 0
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
    
    if dinoJump == 1 and dinoUp==1 :
        #TODO : Faire Monter Le Dino de 1 ligne
        #TODO : si le dinosaure dépasse la limite supérieure :
            #TODO : Modifier dinoUp pour que le dino descende
        
    elif dinoJump == 1 and dinoUp==0:
        #TODO : Faire Descendre le dino de 1 ligne
        
        #TODO : si le dinosaure dépasse la limite inférieure : 
            #TODO : Modifier indicateur pour que le dino s'arrète de sauter
        
cv2.destroyWindow('image1')













