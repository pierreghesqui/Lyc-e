# Le sysyteme de 'Game Over' et le déplacement des ennemies n'est pas encore terminé.



import numpy as np
import cv2
import keyboard 
import random


img = np.zeros((600,500))

Score = 0

bestScore = 0




pression = True




ennemi1Toucher = False
ennemi2Toucher = False
ennemi3Toucher = False
ennemi4Toucher = False
ennemi5Toucher = False

menuPrincipal = True


# Menu Principal textVariables
#__________________________________________


police = cv2.FONT_HERSHEY_SIMPLEX

emplacementDuTexte1 = (70,150)
policeTaille1 = 1.5
policeCouleur1_1 = (255,255,255)
policeCouleur1_0 = (0,0,0)
epaisseur1 = 2

emplacementDuTexte2 = (125,300)
policeTaille2 = 1
policeCouleur2_1 = (255,255,255)
policeCouleur2_0 = (0,0,0)
epaisseur2 = 2


#__________________________________________


# Ennemi

class Ennemi:
    
    def __init__(self, ligne, colonne, hauteur, largeur,img):
        self.ligne = ligne
        self.colonne = colonne
        self.hauteur = hauteur
        self.largeur = largeur
        self.img = img
    def get_ligne(self):
        return self.ligne
    
    def get_colonne(self):
        return self.colonne
    
    def get_hauteur(self):
        return self.hauteur
    
    def get_largeur(self):
        return self.largeur
    
    def move_colonne(self, C_value):
        self.colonne += C_value 
        
    def move_ligne(self, L_value):
        self.ligne += L_value
        
    def disappear(self):
        img = self.img
        img[self.get_ligne():self.get_ligne()+self.get_hauteur()+1, self.get_colonne():self.get_colonne()+self.get_largeur()+1] = 0
    
    def display(self):
        img = self.img
        img[self.get_ligne():self.get_ligne()+self.get_hauteur()+1, self.get_colonne():self.get_colonne()+self.get_largeur()+1] = 1
   

ennemi1 = Ennemi(75, 50, 30, 30,img)

ennemi2 = Ennemi(75, 144, 30, 30,img)

ennemi3 = Ennemi(75, 236, 30, 30,img)

ennemi4 = Ennemi(75, 328, 30, 30,img)

ennemi5 = Ennemi(75, 420, 30, 30,img)





# Bordure

class Bordure:
    
    def __init__(self, ligne, colonne, hauteur, largeur):
        self.ligne = ligne
        self.colonne = colonne
        self.hauteur = hauteur
        self.largeur = largeur
        self.img = img
        
    def get_ligne(self):
        return self.ligne
    
    def get_colonne(self):
        return self.colonne
    
    def get_hauteur(self):
        return self.hauteur
    
    def get_largeur(self):
        return self.largeur
    
        
    
BG = Bordure(1, 1, 600, 3)
    
BD = Bordure(1, 495, 600, 3)

BH = Bordure(1, 0, 1, 500)
    
# vaisseau

monObjetLigne = 500
monObjetColonne = 220
monObjetHauteur = 31
monobjetLargeur = 55


# balle du vaisseau

listeBalleLigne = []
listeBalleColonne = []
balleHauteur = 10
balleLargeur = 2


while not keyboard.is_pressed('ctrl'):
    cv2.imshow('image1',img)
    cv2.waitKey(100)
    
# Condition pour Switch entre menu principale et écran de jeu
    if keyboard.is_pressed('a'):
        menuPrincipal = False
    if keyboard.is_pressed('z'):
        menuPrincipal = True
        
# Menu Principal
    if menuPrincipal == True:
        
        #img[ennemi1.get_ligne():ennemi1.get_ligne()+ennemi1.get_hauteur()+1, ennemi1.get_colonne():ennemi1.get_colonne()+ennemi1.get_largeur()+1] = 0
        #img[ennemi2.get_ligne():ennemi2.get_ligne()+ennemi2.get_hauteur()+1, ennemi2.get_colonne():ennemi2.get_colonne()+ennemi2.get_largeur()+1] = 0
        img[ennemi3.get_ligne():ennemi3.get_ligne()+ennemi3.get_hauteur()+1, ennemi3.get_colonne():ennemi3.get_colonne()+ennemi3.get_largeur()+1] = 0
        img[ennemi4.get_ligne():ennemi4.get_ligne()+ennemi4.get_hauteur()+1, ennemi4.get_colonne():ennemi4.get_colonne()+ennemi4.get_largeur()+1] = 0
        img[ennemi5.get_ligne():ennemi5.get_ligne()+ennemi5.get_hauteur()+1, ennemi5.get_colonne():ennemi5.get_colonne()+ennemi5.get_largeur()+1] = 0
        
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1, monObjetColonne:monObjetColonne+monobjetLargeur+1] = 0
        cv2.putText(img,"Space Invaders",emplacementDuTexte1,police,policeTaille1,policeCouleur1_1,epaisseur1)
        cv2.putText(img,"press A to play",emplacementDuTexte2,police,policeTaille2,policeCouleur2_1,epaisseur2)

# écran de jeu 
    if menuPrincipal == False:
        cv2.putText(img,"Space Invaders",emplacementDuTexte1,police,policeTaille1,policeCouleur1_0,epaisseur1)
        cv2.putText(img,"press A to play",emplacementDuTexte2,police,policeTaille2,policeCouleur2_0,epaisseur2)
        
# Affichage des assets
        img[ennemi1.get_ligne():ennemi1.get_ligne()+ennemi1.get_hauteur()+1, ennemi1.get_colonne():ennemi1.get_colonne()+ennemi1.get_largeur()+1] = 1
        img[ennemi2.get_ligne():ennemi2.get_ligne()+ennemi2.get_hauteur()+1, ennemi2.get_colonne():ennemi2.get_colonne()+ennemi2.get_largeur()+1] = 1
        img[ennemi3.get_ligne():ennemi3.get_ligne()+ennemi3.get_hauteur()+1, ennemi3.get_colonne():ennemi3.get_colonne()+ennemi3.get_largeur()+1] = 1
        img[ennemi4.get_ligne():ennemi4.get_ligne()+ennemi4.get_hauteur()+1, ennemi4.get_colonne():ennemi4.get_colonne()+ennemi4.get_largeur()+1] = 1
        img[ennemi5.get_ligne():ennemi5.get_ligne()+ennemi5.get_hauteur()+1, ennemi5.get_colonne():ennemi5.get_colonne()+ennemi5.get_largeur()+1] = 1
        img[monObjetLigne:monObjetLigne+monObjetHauteur+1, monObjetColonne:monObjetColonne+monobjetLargeur+1] = 1
        img[BG.get_ligne():BG.get_ligne()+BG.get_hauteur()+1, BG.get_colonne():BG.get_colonne()+BG.get_largeur()+1] = 0
        img[BD.get_ligne():BD.get_ligne()+BD.get_hauteur()+1, BD.get_colonne():BD.get_colonne()+BD.get_largeur()+1] = 0
        img[BH.get_ligne():BH.get_ligne()+BH.get_hauteur()+1, BH.get_colonne():BH.get_colonne()+BH.get_largeur()+1] = 0
        
# Déplacement du vaisseau    
        
        if keyboard.is_pressed('left'):
            if monObjetColonne < BG.get_colonne():
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
                monObjetColonne = 445
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
            else:
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
                monObjetColonne -= 10
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
           
        if keyboard.is_pressed('right'):
            if monObjetColonne+60 > BD.get_colonne():
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
                monObjetColonne = 0
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
            
            else:
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 0
                monObjetColonne += 10
                img[monObjetLigne:monObjetLigne+monObjetHauteur + 1, monObjetColonne:monObjetColonne+monobjetLargeur + 1] = 1
          
# déplacement des ennemis
          
        if ennemi1Toucher == False:
            ennemi1.disappear()
            ennemi1.move_ligne(4)
            ennemi1.display()
            
        if ennemi2Toucher == False:
            ennemi2.disappear()
            ennemi2.move_colonne(2)
            ennemi2.move_ligne(4)
            ennemi2.display()

            
            
            
            
            
            
            
            
            
            
            
            
        # Systeme de tire        
          
        if keyboard.is_pressed('space'):
            if pression == True:
                
                listeBalleColonne.append(monObjetColonne+27)
                listeBalleLigne.append(monObjetLigne-11)
                pression = False
        else:
            pression = True
                
                
        for i in range (len(listeBalleLigne)):
            
            balleLigne = listeBalleLigne[i]
            balleColonne = listeBalleColonne[i]
            if balleLigne > BH.get_ligne():
                img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                balleLigne -= 15
                listeBalleLigne[i] = balleLigne
                img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 1 
                
            else:
              img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0  
                
# Si ennemi1 touché
        
            if ennemi1.get_ligne()<balleLigne and  balleLigne<ennemi1.get_ligne()+ennemi1.get_hauteur():
                if ennemi1.get_colonne()<balleColonne and balleColonne<ennemi1.get_colonne()+ennemi1.get_largeur():
                    img[ennemi1.get_ligne():ennemi1.get_ligne()+ennemi1.get_hauteur()+1, ennemi1.get_colonne():ennemi1.get_colonne()+ennemi1.get_largeur()+1] = 0
                    ennemi1Toucher = True
                    ennemi1 = Ennemi(600, 50, 30, 30,img)
                    Score += 1
                    img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                    listeBalleLigne[i] = -1
                    
# Si ennemi2 touché
                    
            if ennemi2.get_ligne()<balleLigne and  balleLigne<ennemi2.get_ligne()+ennemi2.get_hauteur():
                if ennemi2.get_colonne()<balleColonne and balleColonne<ennemi2.get_colonne()+ennemi2.get_largeur():
                    img[ennemi2.get_ligne():ennemi2.get_ligne()+ennemi2.get_hauteur()+1, ennemi2.get_colonne():ennemi2.get_colonne()+ennemi2.get_largeur()+1] = 0
                    ennemi2Toucher = True
                    ennemi2 = Ennemi(600, 425, 30, 30,img)
                    Score += 1
                    img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                    listeBalleLigne[i] = -1

# Si ennemi3 touché
                    
            if ennemi3.get_ligne()<balleLigne and  balleLigne<ennemi3.get_ligne()+ennemi3.get_hauteur():
                if ennemi3.get_colonne()<balleColonne and balleColonne<ennemi3.get_colonne()+ennemi3.get_largeur():
                    img[ennemi3.get_ligne():ennemi3.get_ligne()+ennemi3.get_hauteur()+1, ennemi3.get_colonne():ennemi3.get_colonne()+ennemi3.get_largeur()+1] = 0
                    ennemi3Toucher = True
                    ennemi3 = Ennemi(600, 425, 30, 30,img)
                    Score += 1
                    img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                    listeBalleLigne[i] = -1
                    
# Si ennemi4 touché
                    
            if ennemi4.get_ligne()<balleLigne and  balleLigne<ennemi4.get_ligne()+ennemi4.get_hauteur():
                if ennemi4.get_colonne()<balleColonne and balleColonne<ennemi4.get_colonne()+ennemi4.get_largeur():
                    img[ennemi4.get_ligne():ennemi4.get_ligne()+ennemi4.get_hauteur()+1, ennemi4.get_colonne():ennemi4.get_colonne()+ennemi4.get_largeur()+1] = 0
                    ennemi4Toucher = True
                    ennemi4 = Ennemi(600, 425, 30, 30,img)
                    Score += 1
                    img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                    listeBalleLigne[i] = -1
                    
# Si ennemi5 touché
                    
            if ennemi5.get_ligne()<balleLigne and  balleLigne<ennemi5.get_ligne()+ennemi5.get_hauteur():
                if ennemi5.get_colonne()<balleColonne and balleColonne<ennemi5.get_colonne()+ennemi5.get_largeur():
                    img[ennemi5.get_ligne():ennemi5.get_ligne()+ennemi5.get_hauteur()+1, ennemi5.get_colonne():ennemi5.get_colonne()+ennemi5.get_largeur()+1] = 0
                    ennemi5Toucher = True
                    ennemi5 = Ennemi(600, 425, 30, 30,img)
                    Score += 1
                    img[balleLigne:balleLigne+balleHauteur+1, balleColonne:balleColonne+balleLargeur+1] = 0
                    listeBalleLigne[i] = -1
                    
                    
# Systeme de Score

        if Score > bestScore:
            Score = bestScore



            
          
        

cv2.destroyWindow('image1')





