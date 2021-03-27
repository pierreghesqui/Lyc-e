import numpy as np
import cv2
import time
import pygame.mixer

def vecteurDeplacement(x,y):
    a= np.array([x,y])
    return a

def listeVecteurDeplacement(listV) : 
    win=0
    listLCroco = np.loadtxt("listLCroco.txt", dtype=int)
    listCCroco=np.loadtxt("listCCroco.txt", dtype=int)
    
    listObjetLigne=[]
    listObjetColonne=[]
    x=[]
    y=[]
    for i in range(len(listV)):
        vi = listV[i]
        x.append(vi[0])
        y.append(vi[1])
    img0 = cv2.imread('img.png')/255    
    '''
    img0 = np.zeros((900,900,3))
    img0[:,:,1:3] = 51/255
    l=100
    increm = 100
    while l < 900:
        img0[l,:] = 0
        img0[:,l] = 0
        l = l+increm
    '''
    cv2.destroyWindow('Jeu de chat')    
    pygame.mixer.init()     
    pygame.mixer.music.load("musicMario.mp3")   # chargement de la musique
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    cpt = 0
    img2 = np.ones((900,900,3))  
    img = np.concatenate((img0, img2), axis=1)
    img[100:300,475:525] = 0/255
    imgInit3 = np.sum(img,2)
    #cv2.imwrite('imgInit.png',img[0:900,0:900]*255)
    objetLigne    = 775
    objetColonne  = 75
    objetLargeur  = 50
    listObjetLigne.append(objetLigne)
    listObjetColonne.append(objetColonne)
    objetDemiLargeur  =  int(objetLargeur/2)
    objetQuartLargeur =  int(objetLargeur/4)
    objetLigneExact   = objetLigne
    objetColonneExact = objetColonne
    font = cv2.FONT_HERSHEY_SIMPLEX
    chaton = cv2.imread('chaton.png')
    chaton = cv2.resize(chaton,(objetLargeur,objetLargeur))/255
    ourson = cv2.imread('Ourson.png')
    ourson = cv2.resize(ourson,(objetLargeur,objetLargeur))/255
    croco  = cv2.imread('croco.png')
    croco = cv2.resize(croco,(objetLargeur,objetLargeur))/255
    drapeau = cv2.imread('drapeau.jpg')
    drapeau = cv2.resize(drapeau,(objetLargeur,objetLargeur))/255
    potion = cv2.imread('potion.png')
    potion = cv2.resize(potion,(objetLargeur,objetLargeur))/255
    img[675:725,575:625] =drapeau 
    img[175:225,475:525]= potion
    enDehorsDeLaRoute =0
    crocoAvant=0
    
    img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=1
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
    vitesse = 4
    
    t0 =time.time()
    listeTemps = []
    cv2.putText(img,"M0"+" : t0"+" = 0.00 "  +" s",(1250,75), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)    
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
            if cpt+1<=len(listLCroco)-1:
                img[listLCroco[cpt]:listLCroco[cpt]+objetLargeur,listCCroco[cpt]:listCCroco[cpt]+objetLargeur]=0/255
                cpt = cpt+1
                t = np.round(100*(time.time()-t0))/100
                img[0:26,900:1800]=1
                cv2.putText(img,"Chrono : "+str(t)+" s",(1000,25), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
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
            if objetLigne==175 and objetColonne== 475:
                sonGameOver= pygame.mixer.Sound('bonusMario.mp3')
                sonGameOver.play()   
                vitesse = 13
            
            if 670<objetLigne and objetLigne< 680 and 570<objetColonne and objetColonne<580 :
                win = 1
            if 670<listLCroco[cpt] and listLCroco[cpt]< 680 and 570<listCCroco[cpt] and listCCroco[cpt]<580 and win==0:
                crocoAvant=1
                
        if cpt+1<=len(listLCroco)-1:        
            cv2.putText(img,"M"+str(i+1)+" : t"+str(i+1)+" = "  +str(t)+" s",(1250,25+50*(i+2)), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
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

    for i in range(len(c1)):
        cv2.line(img,(c1[i],c2[i]),(c3[i],c4[i]),(0,50/255,150/255),3)
        cv2.line(img,(c5[i],c6[i]),(c7[i],c8[i]),(0,50/255,150/255),3)
        cv2.putText(img,"M"+str(i),(c9[i],c10[i]), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
    
    
    pygame.mixer.music.stop() 
                
    if win==0 or crocoAvant==1 or enDehorsDeLaRoute==1 :
        sonGameOver= pygame.mixer.Sound('gameOver.mp3')
        sonGameOver.play()   
        cv2.putText(img,"You loose :(  ",(1100,800), font, 3,(1,50/255,1),2,cv2.LINE_AA)
     
    elif win ==1 and enDehorsDeLaRoute==0 and crocoAvant==0:
        sonWin= pygame.mixer.Sound('win.mp3')
        sonWin.play()
        cv2.putText(img,"You Win !! :) ",(1100,800), font, 3,(1,50/255,1),2,cv2.LINE_AA)
    cv2.imshow('Jeu du chat',img)
    cv2.waitKey(1)
    #cv2.imwrite('img2.png',img[0:900,0:900]*255)
    cv2.waitKey(10000)
    pygame.mixer.stop()
    pygame.mixer.quit()

    
    
