# Importation de plusieurs librairies : 
from functionImage import showImage
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np

plt.close('all')

imageTrumpBiden = io.imread('imTrumpBiden.png')

teteBiden=imageTrumpBiden[51:200,148:270]
imageTrumpBiden[10:159,615:615+122] = teteBiden

'''
nbLignes = np.shape(teteBiden)[0]
nbColonnes = np.shape(teteBiden)[1]

coinHautGaucheLigne = 10
coinHautGaucheColonne = 615

for i in range(0,nbLignes):
    for j in range(0,nbColonnes):
        imageTrumpBiden[coinHautGaucheLigne+i,coinHautGaucheColonne+j] = teteBiden[i,j]
'''

showImage(imageTrumpBiden)
showImage(teteBiden)


