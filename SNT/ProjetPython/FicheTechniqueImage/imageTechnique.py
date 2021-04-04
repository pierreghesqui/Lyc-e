import cv2
import numpy as np


img = np.zeros((1000,1000,3))#creation image de 1000 lignes, 1000 colonnes et 3 canaux

# IMPORTATION D'UNE IMAGE D'EMMANUEL MACRON
macron = cv2.imread("macron.jfif")#importer l'image macron.jfif  .jpg .png .tiff
macronResized = cv2.resize(macron,(200,200))/255 #Changer la taille de l'image pour
                                            #qu'elle fasse 50 lignes et 50 colonnes


#JE PLACE L'IMAGE d'EMMANUEL MACRON DANS LE JEU
img[500:700,700:900] = macronResized        #Je place l'image dans le jeu
cv2.imshow("maFenetre",img)             #J'affiche l'image




