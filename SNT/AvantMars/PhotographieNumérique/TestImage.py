# Importation de plusieurs librairies : 
from functionImage import showImage
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

image = np.zeros((3,3)) #Création d'une image avec que des zéros
                        #Définition: 1 ligne et 6 colonnes (=6 pixels)

image[(0,0)] = 0                        
image[(0,1)] = 100                      
image[(0,2)] = 200


image[(1,0)] = 250
image[(1,1)] = 200
image[(1,2)] = 150


image[(2,0)] = 250
image[(2,1)] = 0
image[(2,2)] = 250


showImage(image)

