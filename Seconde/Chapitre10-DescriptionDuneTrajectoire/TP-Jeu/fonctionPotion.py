import numpy as np
import cv2
import time
import pygame.mixer
import keyboard

def vecteurDeplacement(x,y):
    a= np.array([x,y])
    return a

          
    

def listeVecteurDeplacement(listV,potion=0,factorMultiplier=1) : 
    cv2.destroyWindow('Jeu de chat')   #Destruction de la fenêtre précédente si elle existe 
    win=0 #variable qui dit si le chat a gagné ou pas
    potionMagique=0 #variable qui dit si le chat a bu la potion
    enDehorsDeLaRoute =0
    cptMiParcourt=0
    laisserLaPositionDuCrocoAmiParcourt=0
    crocoAvant=0
    vitesse = 4
    listLCroco = np.loadtxt("listLCroco.txt", dtype=int) #Liste des positions du croco (lignes)
    listCCroco=np.loadtxt("listCCroco.txt", dtype=int) #Liste des positions du croco (Colonnes)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #Création des coordonnées des vecteurs entrée par l'élève
    x=[]
    y=[]
    for i in range(len(listV)):
        vi = listV[i]
        x.append(vi[0])
        y.append(vi[1])
        
    #Creation de l'image
    img0 = cv2.imread('img.png')/255    
    pygame.mixer.init()     
    pygame.mixer.music.load("musicMario.mp3")   # chargement de la musique
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    cpt = 0
    img2 = np.ones((900,300,3))  
    img = np.concatenate((img0, img2), axis=1)
    imgInit3 = np.sum(img,2)
    
    #Positionnement du chat
    objetLigne    = 775 #position Initiale du chat
    objetColonne  = 75  #position Initiale du chat
    objetLigneExact   = objetLigne
    objetColonneExact = objetColonne
    objetLargeur  = 50 #Largeur du chat
    listObjetLigne=[]  #Liste des positions du chat
    listObjetColonne=[]#Liste des positions du chat
    listeTemps = [0] #Liste des temps pour les points M0, M1, M2, ...
    listObjetLigne.append(objetLigne)
    listObjetColonne.append(objetColonne)
    objetDemiLargeur  =  int(objetLargeur/2)
    objetQuartLargeur =  int(objetLargeur/4)
    
    
    #Chargement des images
    chaton = cv2.imread('chaton.png')
    chaton = cv2.resize(chaton,(objetLargeur,objetLargeur))/255
    croco  = cv2.imread('croco2.png')
    croco = cv2.resize(croco,(objetLargeur,objetLargeur))/255
    drapeaudarrive = cv2.imread('drapeau.jpg')
    drapeaudarrive = cv2.resize(drapeaudarrive,(objetLargeur,objetLargeur))/255
    img[775:825,475:525] = drapeaudarrive 
    if potion==0:
        potionIm = cv2.imread('drapeauInt.png')
        potionIm = cv2.resize(potionIm,(50,50))/255
    else:
        potionIm = cv2.imread('potion.png')
        potionIm = cv2.resize(potionIm,(50,50))/255
        
    #Creation de la fenêtre
    cv2.namedWindow('Jeu du chat',cv2.WINDOW_NORMAL) #Pour que l'image apparaisse correctement sur les ordinateurs du lycée
    #cv2.resizeWindow('Jeu du chat',1200,900)
    
    #Liste des coordonnées pour tracer les points sous forme de croix
    c1=[objetColonne+objetQuartLargeur]
    c2=[objetLigne+objetQuartLargeur]
    c3=[objetColonne+objetQuartLargeur+objetDemiLargeur]
    c4=[objetLigne+objetQuartLargeur+objetDemiLargeur]
    c5=[objetColonne+objetQuartLargeur]
    c6=[objetLigne+objetQuartLargeur+objetDemiLargeur]
    c7=[objetColonne+objetQuartLargeur+objetDemiLargeur]
    c8=[objetLigne+objetQuartLargeur]
    c9=[objetColonne+objetDemiLargeur-7]
    c10=[objetLigne+10]
    
    t0 =time.time()
    cv2.putText(img,"M0"+" : t0"+" = 0.00 "  +" s",(910,75), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)    
    
    ############  MOUVEMENT CHAT ET CROCO#########################
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        li = -yi #*50
        ci = xi  #*50
        objetLfinal = objetLigne+li
        objetCfinal = objetColonne+ci
        nbDeplacement = int(np.round((li**2+ci**2)**0.5/vitesse)) #5 pixels de distance à chaque itération
        if nbDeplacement==0:
            continue
        
        deplacementLigne = li/nbDeplacement
        deplacementColonne = ci/nbDeplacement
        for k in range(nbDeplacement):
            
            if cpt+1<=len(listLCroco)-1:#Si le crocodile peut encore bouger
                if laisserLaPositionDuCrocoAmiParcourt==1:
                    crocoGrey = np.dstack((croco[:,:,0],croco[:,:,0],croco[:,:,0]))
                    img[listLCroco[cptMiParcourt]:listLCroco[cptMiParcourt]+objetLargeur,listCCroco[cptMiParcourt]:listCCroco[cptMiParcourt]+objetLargeur]=crocoGrey
                if potionMagique ==0:
                    img[75:125,425:475] = potionIm
                img[listLCroco[cpt]:listLCroco[cpt]+objetLargeur,listCCroco[cpt]:listCCroco[cpt]+objetLargeur]=0/255
                cpt = cpt+1
                t = np.round(100*(time.time()-t0))/100
                img[0:26,900:1800]=1
                cv2.putText(img,"Chrono : "+str(t)+" s",(910,25), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
                #print(imgInit3[objetLigne+2,objetColonne+2])
                if imgInit3[objetLigne+2,objetColonne+2]==0.4:
                    enDehorsDeLaRoute = 1
                img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=0/255
                #img[objetLigne+objetQuartLargeur:objetLigne+3*objetQuartLargeur,objetColonne+objetQuartLargeur:objetColonne+3*objetQuartLargeur,1:3]=0/255
                objetLigneExact = objetLigneExact+deplacementLigne
                objetColonneExact = objetColonneExact+deplacementColonne
                objetLigne = int(np.round(objetLigneExact))
                objetColonne = int(np.round(objetColonneExact))
                
                                    
                listObjetLigne.append(objetLigne)
                listObjetColonne.append(objetColonne)
                img[listLCroco[cpt]:listLCroco[cpt]+objetLargeur,listCCroco[cpt]:listCCroco[cpt]+objetLargeur]=croco
                img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=chaton
                cv2.imshow('Jeu du chat',img)
                cv2.waitKey(1)
                
            #DETECTION POTION
            if 65<objetLigne and objetLigne<80 and 420<objetColonne and objetColonne<430 and potionMagique==0:
                if potion ==0 :
                    laisserLaPositionDuCrocoAmiParcourt = 1
                    cptMiParcourt=cpt
                else:
                    potionMagique =1
                    #cv2.putText(img,"Position du crocodile lorsque le chat boit la potion : x =  "+ str(listCCroco[cpt]+25)+" y = "+str(listLCroco[cpt]+25),(910,750), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
                    sonGameOver= pygame.mixer.Sound('bonusMario.mp3')
                    sonGameOver.play()   
                    vitesse = vitesse*factorMultiplier
            #Si le chat est arrivé à la fin du parcours
            if 773<objetLigne and objetLigne< 780 and 470<objetColonne and objetColonne<480 and win==0:
                win = 1
            #Si le croco est arrivé avant le chat
            if 773<listLCroco[cpt] and listLCroco[cpt]< 780 and 470<listCCroco[cpt] and listCCroco[cpt]<480 and win==0:
                crocoAvant=1
        #        
        if cpt+1<=len(listLCroco)-1:        
            cv2.putText(img,"M"+str(i+1)+" : t"+str(i+1)+" = "  +str(t)+" s",(910,25+50*(i+2)), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
            c1.append(objetColonne+objetQuartLargeur)
            c2.append(objetLigne+objetQuartLargeur)
            c3.append(objetColonne+objetQuartLargeur+objetDemiLargeur)
            c4.append(objetLigne+objetQuartLargeur+objetDemiLargeur)
            c5.append(objetColonne+objetQuartLargeur)
            c6.append(objetLigne+objetQuartLargeur+objetDemiLargeur)
            c7.append(objetColonne+objetQuartLargeur+objetDemiLargeur)
            c8.append(objetLigne+objetQuartLargeur)
            c9.append(objetColonne+objetDemiLargeur-7)
            c10.append(objetLigne+10)
        
        listeTemps.append(t)
    
    #Tant que le crocodile peut encore bouger, il bouge
    while cpt+1<=len(listLCroco)-1:
        if laisserLaPositionDuCrocoAmiParcourt==1:
            crocoGrey = np.dstack((croco[:,:,0],croco[:,:,0],croco[:,:,0]))
            img[listLCroco[cptMiParcourt]:listLCroco[cptMiParcourt]+objetLargeur,listCCroco[cptMiParcourt]:listCCroco[cptMiParcourt]+objetLargeur]=crocoGrey
            cv2.putText(img,"x = " + str(listCCroco[cptMiParcourt]+25)+ ", y = " + str(listLCroco[cptMiParcourt]+25) , (listCCroco[cptMiParcourt]-40,listLCroco[cptMiParcourt]+70),font, 0.5,(0,0.4,0.4),2,cv2.LINE_AA)
        if potionMagique ==0:
            img[75:125,425:475] = potionIm
        
        img[listLCroco[cpt]:listLCroco[cpt]+objetLargeur,listCCroco[cpt]:listCCroco[cpt]+objetLargeur]=0/255
        cpt = cpt+1
        img[listLCroco[cpt]:listLCroco[cpt]+objetLargeur,listCCroco[cpt]:listCCroco[cpt]+objetLargeur]=croco
        img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=chaton
        cv2.imshow('Jeu du chat',img)
        cv2.waitKey(1)
        #Chronometre
        t = np.round(100*(time.time()-t0))/100
        img[0:26,900:1800]=1
        cv2.putText(img,"Chrono : "+str(t)+" s",(910,25), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
        
    tempsCroco = np.round(100*(time.time()-t0))/100
    cv2.putText(img,"Le crocodile a mis " + str(tempsCroco)+ " s pour finir la course.",(75,850), font, 1,(1,1,0.5),2,cv2.LINE_AA)
    
    #Dessiner les croix            
    for l in range(len(c1)):
        cv2.line(img,(c1[l],c2[l]),(c3[l],c4[l]),(0,50/255,150/255),3)
        cv2.line(img,(c5[l],c6[l]),(c7[l],c8[l]),(0,50/255,150/255),3)
        cv2.putText(img,"M"+str(l),(c9[l],c10[l]), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
        
    pygame.mixer.music.stop() 
                
    if win==0 or crocoAvant==1 or enDehorsDeLaRoute==1 :
        sonGameOver= pygame.mixer.Sound('gameOver.mp3')
        sonGameOver.play()   
        cv2.putText(img,"Game Over :(  ",(200,300), font, 3,(1,50/255,1),2,cv2.LINE_AA)
     
    elif win ==1 and enDehorsDeLaRoute==0 and crocoAvant==0:
        sonWin= pygame.mixer.Sound('win.mp3')
        sonWin.play()
        cv2.putText(img,"Bravo !! :) ",(200,300), font, 3,(1,50/255,1),2,cv2.LINE_AA)
    cv2.imshow('Jeu du chat',img)
    cv2.waitKey(1)
    #cv2.imwrite('img2.png',img[0:900,0:900]*255)
    v1 = 600/(listeTemps[1]-listeTemps[0])
    v2 = 300/(listeTemps[-2]-listeTemps[-3])
    print(v1)
    print(v2)
    print(v2/v1)
    while not keyboard.is_pressed('ctrl'): 
        cv2.putText(img,"Appuie sur CTRL pour quitter",(200,450), font, 1,(100,100,100),2,cv2.LINE_AA)
        cv2.imshow('Jeu du chat',img)
        cv2.waitKey(1)
        
    pygame.mixer.stop()
    pygame.mixer.quit()
    cv2.destroyWindow('Jeu du chat')
    
    
