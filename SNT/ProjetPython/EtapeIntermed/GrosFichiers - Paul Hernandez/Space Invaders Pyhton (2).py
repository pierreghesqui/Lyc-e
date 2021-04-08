import numpy as np
import cv2
import keyboard 


img = np.zeros((600,500))






# Ennemi1

ennemi1Ligne = 200
ennemi1Colonne = 100
ennemi1Hauteur = 50
ennemi1Largeur = 50
img[ennemi1Ligne:ennemi1Ligne+ennemi1Hauteur+1, ennemi1Colonne:ennemi1Colonne+ennemi1Largeur+1] = 1


# vaisseau

monObjetLigne = 500
monObjetColonne = 220
monObjetHauteur = 31
monobjetLargeur = 55
img[monObjetLigne:monObjetLigne+monObjetHauteur+1, monObjetColonne:monObjetColonne+monobjetLargeur+1] = 1

# Bordure Gauche

BGLigne = 1
BGColonne = 1
BGHauteur = 600
BGLargeur = 3
img[BGLigne:BGLigne+BGHauteur+1, BGColonne:BGColonne+BGLargeur+1] = 0

# Bordure Droite

BDLigne = 1
BDColonne = 495
BDHauteur = 600
BDLargeur = 3
img[BDLigne:BDLigne+BDHauteur+1, BDColonne:BDColonne+BDLargeur+1] = 0

# Bordure Haute

BHLigne = 0
BHColonne = 0
BHHauteur = 1
BHLargeur = 500
img[BHLigne:BHLigne+BHHauteur+1, BHColonne:BHColonne+BHLargeur+1] = 1

# balle du vaisseau

balleLigne = 600
balleColonne = 500
balleHauteur = 10
balleLargeur = 2
img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 1






while not keyboard.is_pressed('ctrl'):
    
    cv2.imshow('image1',img)
    cv2.waitKey(100)
     
 # Déplacement du vaisseau    
    
    if keyboard.is_pressed('left'):
        if monObjetColonne < BGColonne:
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
            monObjetColonne = 445
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
        else:
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
            monObjetColonne -= 10
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
       
    if keyboard.is_pressed('right'):
        if monObjetColonne+60 > BDColonne:
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
            monObjetColonne = 0
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
        
        else:
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
            monObjetColonne += 10
            img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
      
# Systeme de tire        
      
    if keyboard.is_pressed('space'):
        balleColonne = monObjetColonne+27
        balleLigne = monObjetLigne-11
        while balleLigne > BHLigne:
            img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
            balleLigne -= 1
            img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 1
            cv2.waitKey(1)
    
         
        
       
        
cv2.destroyWindow('image1')











