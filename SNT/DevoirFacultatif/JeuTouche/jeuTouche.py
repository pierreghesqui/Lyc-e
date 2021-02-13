# IMPORTATION DES LIBRAIRIES DE FONCTIONS 
import keyboard
import time
#----------------------------------------  

cpt = 0  #compteur du nombre de fois où on appuie sur la touche "CTRL"
tempsInitial = time.time() #temps initial 
tempsFinal = tempsInitial +5 #Le jeu dure 5 secondes 

while  time.time()<tempsFinal :
    if keyboard.is_pressed('ctrl')==True:
        cpt = cpt+1
    #MODIFIER ET COMPLETER LE CODE
  

print('Vous avez appuyé ', cpt, 'fois sur la touche CTRL')
