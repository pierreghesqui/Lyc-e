import numpy as np
import cv2
import keyboard
import random
import time

img=np.ones((500,500,3))

listeTombeLigne = []   #TombeLigne = 0
listeTombeColonne = [] #TombeColonne=random.randint(50,440)
listeObjetAuHazard = []
t0 = time.time()

while not keyboard.is_pressed('ctrl'):
    
    cv2.imshow('objetstombent',img)
    cv2.waitKey(100)
    
    cupcake=cv2.imread("macron.jfif")
    cupcake2=cv2.resize(cupcake,(50,50))/255

    rainbow=cv2.imread("licorne2.png")
    rainbow2=cv2.resize(rainbow,(50,50))/255

    poop=cv2.imread("Licorne.jpg")
    poop2=cv2.resize(poop,(50,50))/255
    
    ObjetTombeString=[cupcake2,rainbow2,poop2]
    t = time.time() - t0
    if t>10:
        #AJOUTER UN ELEMENT DANS LES LISTES
        listeTombeLigne.append(0)
        listeTombeColonne.append(random.randint(50,440))
        #....
    for #each emlement des listes
        #executer les commandes pour le ième élément de la liste
    
    
    
    
    
    
    
    
    
    if t%5<0.2:
        listeTombeLigne.append(0)
        listeTombeColonne.append(random.randint(50,440))
        listeObjetAuHazard.append(ObjetTombeString[random.randint(0,2)])
        
    nbObjetQuiTombent = len(listeTombeLigne)   
    
    for i in range(nbObjetQuiTombent):
        TombeLigne_i = listeTombeLigne[i]
        TombeColonne_i = listeTombeColonne[i]
        ObjetAuHazard_i = listeObjetAuHazard[i]
       
        if TombeLigne_i<500:#ERREUR ICI! 
            img[TombeLigne_i:TombeLigne_i+50,TombeColonne_i:TombeColonne_i+50] = 1
            TombeLigne_i = TombeLigne_i+1
            img[TombeLigne_i:TombeLigne_i+50,TombeColonne_i:TombeColonne_i+50] = ObjetAuHazard_i
        
        listeTombeLigne[i] = TombeLigne_i
            
        
    cv2.waitKey(100)
   
cv2.destroyWindow('objetstombent')