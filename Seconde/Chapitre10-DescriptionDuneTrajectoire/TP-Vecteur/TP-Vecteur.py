import numpy as np
import cv2
import keyboard 



x = [0,4,-4,6,0,5,+2,-4,8]
y = [4,0,+6,2,4,0,-4,-4,0]

img = np.zeros((900,900,3))
img[:,:,1:3] = 51/255
objetLigne    = 850
objetColonne  = 0
objetLargeur  = 50
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
cv2.imshow('image1',img)
cv2.waitKey(10)
vitesse = 10


for i in range(len(x)):
    xi = x[i]
    yi = y[i]
    li = -yi *50
    ci = xi  *50
    objetLfinal = objetLigne+li
    objetCfinal = objetColonne+ci
    nbDeplacement = int(np.round((li**2+ci**2)**0.5/5)) #5 pixels de distance à chaque itération
    if nbDeplacement==0:
        continue
    
    deplacementLigne = li/nbDeplacement
    deplacementColonne = ci/nbDeplacement
    for k in range(nbDeplacement):
        img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=1
        objetLigneExact = objetLigneExact+deplacementLigne
        objetColonneExact = objetColonneExact+deplacementColonne
        objetLigne = int(np.round(objetLigneExact))
        objetColonne = int(np.round(objetColonneExact))
        img[objetLigne:objetLigne+objetLargeur,objetColonne:objetColonne+objetLargeur]=chaton
        cv2.imshow('image1',img)
        cv2.waitKey(25)
        print(str(objetColonne) +"vs" + str(objetLfinal))
    #img[objetLigne+objetQuartLargeur:objetLigne+objetQuartLargeur+objetDemiLargeur,objetColonne+objetQuartLargeur:objetColonne+objetQuartLargeur+objetDemiLargeur,0]=1
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
    
for i in range(len(c1)):
    cv2.line(img,(c1[i],c2[i]),(c3[i],c4[i]),(0,50/255,150/255),3)
    cv2.line(img,(c5[i],c6[i]),(c7[i],c8[i]),(0,50/255,150/255),3)
    cv2.putText(img,str(i),(c9[i],c10[i]), font, 0.75,(0,50/255,150/255),2,cv2.LINE_AA)
    

cv2.imshow('image1',img)
cv2.waitKey(25)
#cv2.destroyWindow('image1')    



