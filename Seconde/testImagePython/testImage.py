import matplotlib.pyplot as plt #Librairie qui affiche les images
import numpy as np #Librairie pour manipuler les matrices
from skimage import (io) #Librairie pour charger et lire les images

path = 'https://www.tendanceouest.com/photos/maxi/266197.jpg'
image = io.imread(path)
image[212:242,382:420,0] = 255
image[212:242,382:420,1] = 0
image[212:242,382:420,2] = 0



# Drapeau francais

drapeauFrancais = np.zeros((100,300,3))
drapeauFrancais[:,0:100,2]   = 255  #bleu
drapeauFrancais[:,100:200,:] = 255 #blanc
drapeauFrancais[:,200:300,0] = 255 #rouge

plt.figure(1)
plt.imshow(drapeauFrancais)
plt.show()

#Drapeau Italien

 
drapeauItalien = np.zeros((100,300,3))
drapeauItalien[:,0:100,1] = 255 #vert
drapeauItalien[:,100:200,:] = 255 #blanc
drapeauItalien[:,200:300,0] = 255 #rouge

plt.figure(2)
plt.imshow(drapeauItalien)
plt.show()