# Importation de plusieurs librairies : 
from functionImage import showImage
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np

plt.close('all')

imageTrumpBiden = io.imread('imTrumpBiden.png')


for column in range(177,227,1):
    imageTrumpBiden[75,column]=0
        

showImage(imageTrumpBiden)


