import numpy as np
import cv2
import keyboard
import time
img = np.zeros((600,500))
# Dinosaure
DinoLigne = 300
DinoColonne = 30
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
    cv2.waitKey(6)
    if keyboard.is_pressed('space'):
            DinoLigne = DinoLigne +50
            img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 1
            cv2.imshow('image1',img)
            cv2.waitKey(6)
            time.sleep(0.5) # Sleep for 0.5 seconds
            DinoLigne = DinoLigne -50
            img[DinoLigne:DinoLigne+DinoHauteur, DinoColonne:DinoColonne+DinoLargeur] = 0
cv2.destroyWindow('image1')

acver.fr/tutodino