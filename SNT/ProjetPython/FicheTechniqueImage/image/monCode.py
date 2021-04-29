import cv2
import numpy as np

imLicorne = cv2.imread('belleLicorne.png') #importation de l'image
imLicorne = imLicorne/255   #je divise tous les pixels par 255 
                             #pour que les valeurs soient entre 0 et 1       
 
imLicorneResized = cv2.resize(imLicorne,(200,250)) #Je redimensionne l'image pour 
                                        #pour qu'elle fasse 200 pixels de large
                                        #et 250 pixels de haut

licorneLargeur = 200 #Creation des variables de largeur et hauteur                                    
licorneHauteur = 250 


fenetre = np.zeros((500,500,3)) #grande fenêtre du jeu
                            #hauteur:500, largeur : 500, profondeur : 3
                            #Rappel : la profondeur permet de coder les couleurs
                            
#Plaçons la licorne dans la fenêtre du jeu à la ligne 0 et la colonne 200                          
fenetre[0:0+licorneHauteur, 200:200+licorneLargeur]=imLicorneResized

cv2.imshow('monJeu',fenetre) #j'affiche l'image


