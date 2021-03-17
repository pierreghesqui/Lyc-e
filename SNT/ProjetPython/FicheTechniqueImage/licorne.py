import cv2
import numpy as np

path = 'Licorne.jpg'
imLicorne = cv2.imread(path)/255

licorneLargeur = imLicorne.shape[1]
licorneHauteur = imLicorne.shape[0]
licorneLigne = 0
licorneColonne = 100 

fenetre = np.zeros((1000,1000,3))
fenetre[licorneLigne:licorneLigne+licorneHauteur, licorneColonne:licorneColonne+licorneLargeur]=imLicorne

cv2.imshow('image',fenetre)


