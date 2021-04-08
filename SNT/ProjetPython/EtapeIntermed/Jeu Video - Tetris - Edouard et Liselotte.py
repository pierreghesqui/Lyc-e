import numpy as np
import cv2
import keyboard

img = np.zeros((500,275))

listeObjetLigne = [0,0,0,0]
listeObjetColonne = [175,25,100,130]
listeObjetLargeur =[75,50,50,300]
listeObjetHauteur = [50,50,100,200]

'''
objetligne = 0
objetcolonne = 175
objetlargeur = 75
objethauteur = 50

objetligne2 = 0
objetcolonne2 = 25
objetlargeur2 = 50
objethauteur2 = 50

objetligne3 = 0
objetcolonne3 = 100
objetlargeur3 = 50
objethauteur3 = 100

img[objetligne:objetligne+objethauteur,objetcolonne:objetcolonne+objetlargeur] = 1
img[objetligne2:objetligne2+objethauteur2,objetcolonne2:objetcolonne2+objetlargeur2] = 1
img[objetligne3:objetligne3+objethauteur3,objetcolonne3:objetcolonne3+objetlargeur3] = 1

Image = img[objetligne:objetligne+objethauteur,objetcolonne:objetcolonne+objetlargeur]
'''
numeroDeLobjet = 0
objetLigneEnCours   =  listeObjetLigne[numeroDeLobjet]
objetHauteurEnCours = listeObjetHauteur[numeroDeLobjet]
objetColonneEnCours        = listeObjetColonne[numeroDeLobjet]
objetLargeurEncours        =  listeObjetLargeur[numeroDeLobjet]

while not keyboard.is_pressed('ctrl'):           
    cv2.imshow('tetris',img)
    cv2.waitKey(200)      
    img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 0
    objetLigneEnCours = objetLigneEnCours+10
    img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 1
    if keyboard.is_pressed('left'):
         img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 0
         objetColonneEnCours = objetColonneEnCours-10
         img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 1
    elif keyboard.is_pressed('right'):
          img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 0
          objetColonneEnCours = objetColonneEnCours+10
          img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 1
    elif keyboard.is_pressed('down'):
         img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 0
         objetLargeurEncours,objetHauteurEnCours = objetHauteurEnCours,objetLargeurEncours
         img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 1
    elif keyboard.is_pressed('up'):
          img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 0
          objetLargeurEncours,objetHauteurEnCours = objetHauteurEnCours,objetLargeurEncours
          img[objetLigneEnCours:objetLigneEnCours+objetHauteurEnCours,objetColonneEnCours:objetColonneEnCours+objetLargeurEncours] = 1
    
    if objetLigneEnCours == 450:
        numeroDeLobjet = numeroDeLobjet+1
        objetLigneEnCours   =  listeObjetLigne[numeroDeLobjet]
        objetHauteurEnCours = listeObjetHauteur[numeroDeLobjet]
        objetColonneEnCours        = listeObjetColonne[numeroDeLobjet]
        objetLargeurEncours        =  listeObjetLargeur[numeroDeLobjet]

cv2.destroyWindow('tetris')
