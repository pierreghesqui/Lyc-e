import cv2
import numpy as np
import keyboard

#afin de faire fonctionner le code vous aurez besoin de : 
# buisson.png : image de buisson (décoration)
# car.png : image de voiture
# fond.jpg : fond du jeux
# gris.png : voiture grise
# hautweels.png : image de voiture
# nissan.png : image de voiture
# poulet.png : personnage principal
# tree.png : image d'arbre (décoration)
# voiturre.png : image de voiture



img = np.zeros((1500,1500,3))

imgRoute = cv2.imread('fond.jpg')
print(np.shape(imgRoute))
imgRoute = cv2.resize(imgRoute,(1500,1000))/255
img[0:1000,0:1500,0:3]=imgRoute

imgTree = cv2.imread('tree.png')
print(np.shape(imgTree))
imgTree = cv2.resize(imgTree,(20,40))/255
img[200:240,110:130,0:3]=imgTree

imgBuisson = cv2.imread('buisson.png')
print(np.shape(imgBuisson))
imgBuisson = cv2.resize(imgBuisson,(290,40))/255
img[380:420,510:800,0:3]=imgBuisson

imgVoitures = cv2.imread('car.png')
print(np.shape(imgVoitures))
imgVoitures = cv2.resize(imgVoitures,(120,100))/255
print(np.shape(imgVoitures))
img[750:850,500:620,0:3]=imgVoitures

imgPoulet = cv2.imread('poulet.png')
print(np.shape(imgPoulet))
imgPoulet = cv2.resize(imgPoulet,(120,130))/255
img[720:850,600:720,0:3]=imgPoulet

imgVoitur = cv2.imread('hautweels.png')
print(np.shape(imgVoitur))
imgVoitur = cv2.resize(imgVoitur,(45,23))/255
print(np.shape(imgVoitures))
img[510:533,500:545,0:3]=imgVoitur

imgVoitur = cv2.imread('hautweels.png')
print(np.shape(imgVoitur))
imgVoitur = cv2.resize(imgVoitur,(45,23))/255
print(np.shape(imgVoitures))
img[10:33,20:65,0:3]=imgVoitur

imgCar = cv2.imread('voiturre.png')
print(np.shape(imgCar))
imgCar = cv2.resize(imgCar,(45,32))/255
print(np.shape(imgCar))
img[388:420,267:312,0:3]=imgCar

imgNissan = cv2.imread('nissan.png')
print(np.shape(imgNissan))
imgNissan = cv2.resize(imgNissan,(75,50))/255
print(np.shape(imgNissan))
img[677:727,5:80,0:3]=imgNissan

imgNissans = cv2.imread('nissan.png')
print(np.shape(imgNissans))
imgNissans = cv2.resize(imgNissans,(54,42))/255
print(np.shape(imgNissans))
img[111:153,234:288,0:3]=imgNissans

imgGray = cv2.imread('gris.png')
print(np.shape(imgGray))
imgGray = cv2.resize(imgGray,(21,31))/255
print(np.shape(imgGray))
img[111:142,234:255,0:3]=imgGray


#poulet
monObjetLigne = 720
monObjetColonne = 600
monObjetHauteur = 130
monObjetLargeur = 120

#imgVoitur
monNbjetLigne = 10
monNbjetColonne = 20
monNbjetHauteur = 23
monNbjetLargeur = 45

#imgVoitur
monKbjetLigne = 510
monKbjetColonne = 500
monKbjetHauteur = 23
monKbjetLargeur = 45

#imgCar
monLbjetLigne = 388
monLbjetColonne = 267
monLbjetHauteur = 32
monLbjetLargeur = 45

#imgNissan
monUbjetLigne = 677
monUbjetColonne = 5
monUbjetHauteur = 50
monUbjetLargeur = 75

#imgVoitures
monSbjetLigne = 500
monSbjetColonne = 750
monSbjetHauteur = 100
monSbjetLargeur = 120

#imgGray
monAbjetLigne = 100
monAbjetColonne = 356
monAbjetHauteur = 31
monAbjetLargeur = 21

#imgNissans
monBbjetLigne = 111
monBbjetColonne = 234
monBbjetHauteur = 42
monBbjetLargeur = 54



img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
img[monSbjetLigne:monSbjetLigne+monSbjetHauteur,monSbjetColonne:monSbjetColonne+monSbjetLargeur] = imgVoitures
img[monAbjetLigne:monAbjetLigne+monAbjetHauteur,monAbjetColonne:monAbjetColonne+monAbjetLargeur] = 1
img[monBbjetLigne:monBbjetLigne+monBbjetHauteur,monBbjetColonne:monBbjetColonne+monBbjetLargeur] = 1




while not keyboard.is_pressed('space'):
    cv2.imshow('image',img)
    cv2.waitKey(100)

    
    

    img[monSbjetLigne:monSbjetLigne+monSbjetHauteur,monSbjetColonne:monSbjetColonne+monSbjetLargeur] = 0.35
    monSbjetColonne = monSbjetColonne-1
    img[monSbjetLigne:monSbjetLigne+monSbjetHauteur,monSbjetColonne:monSbjetColonne+monSbjetLargeur] = imgVoitures


    img[monBbjetLigne:monBbjetLigne+monBbjetHauteur,monBbjetColonne:monBbjetColonne+monBbjetLargeur] = 0.35
    monBbjetColonne = monBbjetColonne-1
    img[monBbjetLigne:monBbjetLigne+monBbjetHauteur,monBbjetColonne:monBbjetColonne+monBbjetLargeur] = imgNissans

    img[monAbjetLigne:monAbjetLigne+monAbjetHauteur,monAbjetColonne:monAbjetColonne+monAbjetLargeur] = 0.35
    monAbjetColonne = monAbjetColonne + 2
    img[monAbjetLigne:monAbjetLigne+monAbjetHauteur,monAbjetColonne:monAbjetColonne+monAbjetLargeur] = imgGray

    img[monKbjetLigne:monKbjetLigne+monKbjetHauteur,monKbjetColonne:monKbjetColonne+monKbjetLargeur] = 0.35
    monKbjetColonne = monKbjetColonne + 3
    img[monKbjetLigne:monKbjetLigne+monKbjetHauteur,monKbjetColonne:monKbjetColonne+monKbjetLargeur] = imgVoitur

    img[monUbjetLigne:monUbjetLigne+monUbjetHauteur,monUbjetColonne:monUbjetColonne+monUbjetLargeur] = 0.35
    monUbjetColonne = monUbjetColonne + 2
    img[monUbjetLigne:monUbjetLigne+monUbjetHauteur,monUbjetColonne:monUbjetColonne+monUbjetLargeur] = imgNissan

    img[monLbjetLigne:monLbjetLigne+monLbjetHauteur,monLbjetColonne:monLbjetColonne+monLbjetLargeur] = 1
    monLbjetColonne = monLbjetColonne + 1
    img[monLbjetLigne:monLbjetLigne+monLbjetHauteur,monLbjetColonne:monLbjetColonne+monLbjetLargeur] = imgCar

    img[monNbjetLigne:monNbjetLigne+monNbjetHauteur,monNbjetColonne:monNbjetColonne+monNbjetLargeur] = 1
    monNbjetColonne = monNbjetColonne + 3
    img[monNbjetLigne:monNbjetLigne+monNbjetHauteur,monNbjetColonne:monNbjetColonne+monNbjetLargeur] = imgVoitur
     
    if keyboard.is_pressed('left'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
        monObjetColonne = monObjetColonne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
    
    elif keyboard.is_pressed('right'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
        monObjetColonne = monObjetColonne+10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
    
    elif keyboard.is_pressed('up'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
        monObjetLigne = monObjetLigne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
   
    elif keyboard.is_pressed('down'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
        monObjetLigne = monObjetLigne+10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = imgPoulet
    
cv2.destroyWindow('image')