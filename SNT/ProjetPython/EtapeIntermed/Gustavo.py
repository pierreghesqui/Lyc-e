import numpy as np
import cv2
import keyboard


cpt=0

img=np.zeros((505,500))
monobjetligne=2
monobjetcolonne=250
monobjethauteur=25
monobjetlargeur=25
img[monobjetligne:monobjetligne+monobjethauteur+1,monobjetcolonne:monobjetcolonne+monobjetlargeur+1]=1

moncubeligne=1
moncubecolonne=400
moncubehauteur=499
moncubelargeur=1
img[moncubeligne:moncubeligne+moncubehauteur+1,moncubecolonne:moncubecolonne+moncubelargeur+1]=1


moncube1ligne=1
moncube1colonne=100
moncube1hauteur=499
moncube1largeur=1
img[moncube1ligne:moncube1ligne+moncube1hauteur+1,moncube1colonne:moncube1colonne+moncube1largeur+1]=1

moncube2ligne=500
moncube2colonne=100
moncube2hauteur=1
moncube2largeur=300
img[moncube2ligne:moncube2ligne+moncube2hauteur+1,moncube2colonne:moncube2colonne+moncube2largeur+1]=1

moncube3ligne=0
moncube3colonne=100
moncube3hauteur=1
moncube3largeur=301
img[moncube3ligne:moncube3ligne+moncube3hauteur+1,moncube3colonne:moncube3colonne+moncube3largeur+1]=1
  
    
while not keyboard.is_pressed('ctrl'):
    
    cv2.imshow('image1',img)
    cv2.waitKey(100)
    img[monobjetligne:monobjetligne+monobjethauteur+1,monobjetcolonne:monobjetcolonne+monobjetlargeur+1]=0
    monobjetligne=monobjetligne+5
    if keyboard.is_pressed('left'):
        if monobjetcolonne<106:
            monobjetcolonne=374
        else:
           monobjetcolonne-=5
    
    if keyboard.is_pressed('right'):
        if monobjetcolonne>365:
            monobjetcolonne=102
        else:
           monobjetcolonne+=5
        
    if keyboard.is_pressed('down'):
        if monobjetligne>464:
            monobjetligne=469
        else:
           monobjetligne+=5
    if monobjetligne>464:
            monobjetligne=469
   
    if keyboard.is_pressed('a'):#touche cachée permettant de monter pour les tests
           monobjetligne-=5
     
    img[monobjetligne:monobjetligne+monobjethauteur+1,monobjetcolonne:monobjetcolonne+monobjetlargeur+1]=1            

cv2.destroyWindow('image1')
