# Importation de plusieurs librairies : 
from functionImage import showImage
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np

plt.close('all')

imageTrumpBiden = io.imread('imTrumpBiden.png')

teteBiden=imageTrumpBiden[51:200,148:270]
sha = np.shape(teteBiden)

#COMPLETER LE CODE

showImage(imageTrumpBiden)
showImage(teteBiden)


