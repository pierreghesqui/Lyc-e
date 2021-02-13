# Importation de plusieurs librairies : 
from functionImage import imshow2
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

image = np.zeros((2,6)) #Création d'une image avec que des zéros
                        #Définition: 1 ligne et 6 colonnes (=6 pixels)

image[(0,0)] = 0       #Le pixel de la 1ère ligne et 1ère colonne
                        #a la valeur 10
                        
image[(0,1)] = 50       #Le pixel de la 1ère ligne et 2eme colonne
                        #a la valeur 50
                        
image[(0,2)] = 100
image[(0,3)] = 150
image[(0,4)] = 200
image[(0,5)] = 250

image[(1,0)] = 250
image[(1,1)] = 200
image[(1,2)] = 150
image[(1,3)] = 100
image[(1,4)] = 50
image[(1,5)] = 0

imshow2(image)

