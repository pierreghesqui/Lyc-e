import numpy as np
import cv2
import random
import keyboard



img = np.zeros((502,502,3))

cL=0
cC=0
cH=502
cLa=502
img[0:1,] = 1

monObjetLigne=480
monObjetColonne=250
monObjetHauteur = 20
monObjetLargeur = 100

ligneCarreRouge=0
colonneCarreRouge=401
k = 100
m = 100
img[n:n+m,f:f+m,2] = 1

l=0
c=301
h = 100
la = 100
img[l:l+h,c:c+la,0] = 1

L=0
C=201
H = 100
La = 100
img[L:L+H,C:C+La,1] = 1

oL=0
oC=101
oH = 100
oLa = 100
img[oL:oL+oH,oC:oC+oLa,2] = 1

objetL=0
objetC=1
objetH = 100
objetLa = 100

img[objetL:objetL+objetH,objetC:objetC+objetLa,1] = 1

img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur,1] = 1

while not keyboard.is_pressed('ctrl'):
    cv2.imshow('oscar',img)
    cv2.waitKey(100)
    
    if keyboard.is_pressed('left'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 0
        monObjetColonne =  monObjetColonne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1
        
    elif keyboard.is_pressed('right'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 0
        monObjetColonne =  monObjetColonne+10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1
        
    elif keyboard.is_pressed('up'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 0
        monObjetLigne = monObjetLigne-10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1
        
    elif keyboard.is_pressed('down'):
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 0
        monObjetLigne = monObjetLigne+10
        img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1
        
    img[objetL:objetL+objetH,objetC:objetC+objetLa] = 1
    img[oL:oL+oH,oC:oC+oLa,2] = 1
    img[L:L+H,C:C+La,1] = 1
    img[l:l+h,c:c+la,0] = 1
    
    img[n:n+m,f:f+m,2] = 1
    img[oL:oL+oH,oC:oC+oLa,2] = 1    
    img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur,1] = 1
    
cv2.destroyWindow('oscar')    
    
    