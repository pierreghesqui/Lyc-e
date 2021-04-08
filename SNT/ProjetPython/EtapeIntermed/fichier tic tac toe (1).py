
import numpy as np
import cv2
import  keyboard

img= np.zeros ((500,500))

while not keyboard.is_pressed('ctrl'):
    cv2.imshow('tic tac toe',img ) 
    cv2.waitKey(100)  
    
cv2.destroyWindow ('tic tac toe') 

cv2.waitKey(1000)  

img = np.zeros((500.500))

monObjetLigne=10
monObjetColonne=300
monObjetHauteur = 50
monObjetLargeur = 75

img[monObjetLigne:monObjetLigne+monObjetHauteur,monObjetColonne:monObjetColonne+monObjetLargeur] = 1


while not keyboard.is_pressed('ctrl'):
    cv2.imshow('tic tac toe',img)
    cv2.waitKey(100)

cv2.destroyWindow('tic tac toe')
cv2.waitKey(1000)  

#player1 chooses 'rond or croix'
# 'player 2' starts 'tic tac toe'
#for every 'rond' played a 'croix' has to be played
#for every 'croix' played a 'rond' has to be played 



img = np.zeros((500,500))

img[:,0:10]=1
    

img[:,160:170]=1


img[:,315:325]=1


img[:,490:501]=1



img[:,10:0]=1



img[160:170,:]=1

img[315:325,:]=1

img[490:501,:]=1
    
while not keyboard.is_pressed('ctrl'): 
    cv2.imshow('tic tac toe',img)
    cv2.waitKey(1) 

cv2.waitKey(1000)  

cv2.destroyWindow("tic tac toe")

