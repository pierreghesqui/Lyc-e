# Importation de plusieurs librairies : 
from functionImage import showImage
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

plt.close('all')

imageTrumpBiden = io.imread('imTrumpBiden.png') #Chargement de
                                                #l'image


for line in range(25,157,1):
    for column in range (600,700,1):
        imageTrumpBiden[line, column]=0   #Mise à 0 des pixels

showImage(imageTrumpBiden)                #Affichage de l'image


