 
    import numpy as np
    import cv2
    import keyboard
    
    img = np.zeros((500,500))
    
    monObjetLigne = 100
    monObjetColonne = 36
    monObjetHauteur = 10
    monObjetLargeur = 30
    
    monObjet2Ligne = 120
    monObjet2Colonne = 25
    monObjet2Hauteur = 15
    monObjet2Largeur = 200
    
    monObjet3Ligne = 140
    monObjet3Colonne = 98
    monObjet3Hauteur = 20
    monObjet3Largeur = 76
    
    monObjet4Ligne = 140
    monObjet4Colonne = 10
    monObjet4Hauteur = 25
    monObjet4Largeur = 40
    
    monObjet5Ligne = 160
    monObjet5Colonne = 150
    monObjet5Hauteur = 10
    monObjet5Largeur = 30
    
    monObjet6Ligne = 180
    monObjet6Colonne = 150
    monObjet6Hauteur = 10
    monObjet6Largeur = 30
    
    monObjet7Ligne = 200
    monObjet7Colonne = 150
    monObjet7Hauteur = 10
    monObjet7Largeur = 30
    
    monObjet8Ligne = 220
    monObjet8Colonne = 150
    monObjet8Hauteur = 10
    monObjetLargeur = 30
    
    monObjet9Ligne = 240
    monObjet9Colonne = 150
    monObjet9Hauteur = 10
    monObjet9Largeur = 30
    
    monObjet10Ligne = 260
    monObjet10Colonne = 150
    monObjet10Hauteur = 10
    monObjet10Largeur = 30
    
    monObjet11Ligne = 280
    monObjet11Colonne = 150
    monObjet11Hauteur = 10
    monObjet11Largeur = 30
    
    monObjet12Ligne = 380
    monObjet12Colonne = 350
    monObjet12Hauteur = 10
    monObjet12Largeur = 150
    
    monObjet13Ligne = 380
    monObjet13Colonne =0
    monObjet13Hauteur = 10
    monObjet13Largeur = 60
    
    monObjet14Ligne = 380
    monObjet14Colonne = 150
    monObjet14Hauteur = 10
    monObjet14Largeur = 30
    
    monObjet15Ligne = 460
    monObjet15Colonne = 0
    monObjet15Hauteur = 10
    monObjet15Largeur = 70
    
    monObjet16Ligne = 380
    monObjet16Colonne = 180
    monObjet16Hauteur = 90
    monObjet16Largeur = 10
    
    monObjet17Ligne = 420
    monObjet17Colonne =50
    monObjet17Hauteur = 10
    monObjet17Largeur = 75
    
    monObjet18Ligne = 460
    monObjet18Colonne = 150
    monObjet18Hauteur = 10
    monObjet18Largeur = 70
    
    monObjet19Ligne = 420
    monObjet19Colonne = 180
    monObjet19Hauteur = 10
    monObjet19Largeur = 320
    
    monObjet20Ligne = 460
    monObjet20Colonne = 270
    monObjet20Hauteur = 10
    monObjet20Largeur = 150
    
    monObjet21Ligne = 465
    monObjet21Colonne = 340
    monObjet21Hauteur = 35
    monObjet21Largeur = 10
    
    img[monObjetLigne:monObjetLigne+monObjetHauteur, 
    monObjetColonne:monObjetColonne+monObjetLargeur]=1
    
    img[monObjet2Ligne:monObjet2Ligne+monObjetHauteur, 
    monObjet2Colonne:monObjet2Colonne+monObjet2Largeur]=1
    
    img[monObjet3Ligne:monObjet3Ligne+monObjet3Hauteur, 
    monObjet3Colonne:monObjet3Colonne+monObjet3Largeur]=1
    
    img[monObjet4Ligne:monObjet4Ligne+monObjet4Hauteur, 
    monObjet4Colonne:monObjet4Colonne+monObjet4Largeur]=1
    
    img[monObjet5Ligne:monObjet5Ligne+monObjet5Hauteur, 
    monObjet5Colonne:monObjet5Colonne+monObjet5Largeur]=1
    
    img[monObjet6Ligne:monObjet6Ligne+monObjet6Hauteur, 
    monObjet6Colonne:monObjet6Colonne+monObjet6Largeur]=1
    
    img[monObjet7Ligne:monObjet7Ligne+monObjet7Hauteur, 
    monObjet7Colonne:monObjet7Colonne+monObjet7Largeur]=1
    
    img[monObjet8Ligne:monObjet8Ligne+monObjet8Hauteur, 
    monObjet8Colonne:monObjet8Colonne+monObjetLargeur]=1
    
    img[monObjet9Ligne:monObjet9Ligne+monObjet9Hauteur, 
    monObjet9Colonne:monObjet9Colonne+monObjet9Largeur]=1
    
    img[monObjet11Ligne:monObjet11Ligne+monObjet11Hauteur, 
    monObjet11Colonne:monObjet11Colonne+monObjet11Largeur]=1
    
    img[monObjet12Ligne:monObjet12Ligne+monObjet12Hauteur, 
    monObjet12Colonne:monObjet12Colonne+monObjet12Largeur]=1
    
    img[monObjet13Ligne:monObjet13Ligne+monObjet13Hauteur, 
    monObjet13Colonne:monObjet13Colonne+monObjet13Largeur]=1
    
    img[monObjet14Ligne:monObjet14Ligne+monObjet14Hauteur, 
    monObjet14Colonne:monObjet14Colonne+monObjet14Largeur]=1
    
    img[monObjet15Ligne:monObjet15Ligne+monObjet15Hauteur, 
    monObjet15Colonne:monObjet15Colonne+monObjet15Largeur]=1
    
    img[monObjet16Ligne:monObjet16Ligne+monObjet16Hauteur, 
    monObjet16Colonne:monObjet16Colonne+monObjet16Largeur]=1
    
    img[monObjet17Ligne:monObjet17Ligne+monObjet17Hauteur, 
    monObjet17Colonne:monObjet17Colonne+monObjet17Largeur]=1
    
    img[monObjet18Ligne:monObjet18Ligne+monObjet18Hauteur, 
    monObjet18Colonne:monObjet18Colonne+monObjet18Largeur]=1
    
    img[monObjet19Ligne:monObjet19Ligne+monObjet19Hauteur, 
    monObjet19Colonne:monObjet19Colonne+monObjet19Largeur]=1
    
    img[monObjet20Ligne:monObjet20Ligne+monObjet20Hauteur, 
    monObjet20Colonne:monObjet20Colonne+monObjet20Largeur]=1
    
    img[monObjet21Ligne:monObjet21Ligne+monObjet21Hauteur, 
    monObjet21Colonne:monObjet21Colonne+monObjet21Largeur]=1
    
    while not keyboard.is_pressed('ctrl'):
            cv2.imshow('pacman' , img)
            cv2.waitKey(100)
    cv2.destroyWindow('pacman')

