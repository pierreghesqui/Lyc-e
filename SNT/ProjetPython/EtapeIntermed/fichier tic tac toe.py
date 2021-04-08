import numpy as np
import cv2
import  keyboard

img= np.zeros ((500,500))

while not keyboard.is_pressed('ctrl'):
    cv2.imshow('tic tac toe',img ) 
    cv2.waitKey(100)  
  
img = np.zeros((500,500))

monObjetLigne=10
monObjetColonne=300
monObjetHauteur = 50
monObjetLargeur = 75

img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1

while not keyboard.is_pressed('ctrl'):
    cv2.imshow('tic tac toe',img)
    cv2.waitKey(100)

#player1 chooses 'rond or croix'
# 'player 2' starts 'tic tac toe'
#for every 'rond' played a 'croix' has to be played
#for every 'croix' played a 'rond' has to be played 

img = np.zeros((500,500))

img[:,0:10]=1
    
img[:,160:170]=1

img[:,315:325]=1

img[:,490:500]=1

img[:,10:0]=1

img[160:170,:]=1

img[315:325,:]=1

img[490:500,:]=1
    
while not keyboard.is_pressed('ctrl'): 
    cv2.imshow('tic tac toe',img)
    cv2.waitKey(1) 


'''
var [i = 10*(0)]
    print (1)
    1 [0] [0]=1
    print (1) 
    1[0] [1] =print(1)

import numpy as np
import cv2
import keyboard

monObjectligne= 100
monObjectcolonne= 300
monObjectauteur=  50
monObjectlargeur= 75
img[monObjetLigne:monObjetLigne+monObjetHauteur ,monObjetColonne: monObjetColonne+monObjetLargeur] = 1

while not keyboard.is_pressed('ctrl'): 

    cv2.inshow('image1',img)
    cv2.waitkey(1) 
 
    img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:moObjetColonne+monObjetLargeur+1] = 0
    monObjetColonne = monObjetColonne-10
    img[monObjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetcolonne+monObjetLargeur+1] = 1

import numpy as np
import cv2
import keyboard

img = np.zeroes((500))
monObjetLigne = 100
monObjetColonne = 300
monObjetHauteur = 50
monObjetLargeur = 75
img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1

while not keyboard.is_pressed('ctrl'):
    
cv2.imshow('image1',img)
cv2.waitkey(100)
    
if keyboard.is_pressed('left'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetColonne = monObjetColonne-10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
elif keyboard.is_pressed('right'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetColonne = monObjetColonne+10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
elif keyboard.is_pressed('up'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetLigne = monObjetColonne+10
elif keyboard.is_pressed('down'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 0
        monObjetLigne = monObjetColonne-10
elif keyboard.is_pressed('up right'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetColonne = monObjetColonne+10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetLigne =monObjetligne+10
elif keyboard.is_pressed('up left'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetColonne = monObjetColonne+10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetLigne =monObjetligne-10
elif keyboard.is_pressed('down right'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetColonne = monObjetColonne+10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetLigne =monObjetligne-10
elif keybaord.is_pressed('down left'):
        img[monobjetLigne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetColonne = monObjetColonne-10
        img[monObjetligne:monObjetLigne+monObjetHauteur+1,monObjetColonne:monObjetColonne+monObjetLargeur+1] = 1
        monObjetLigne =monObjetligne-10
    

def diagonaleGagnante (x) :
    tableau = {"a":1, "b":2, "c":3 } #coordonnées cases diagonales
    if "a":1=1 "b":2=1 "c":3=1 : #1=0
        print("player 1 win")
    elif"a":1=2 "b":2=2 "c"3=2 : #2=x
        print("player 2 win")
    else :
        print("c'est à votre tour de jouer")
 '''