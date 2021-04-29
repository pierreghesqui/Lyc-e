from fonctionsTP2 import *

images, labels = importationDesImagesEtLabels() 
monImage = images[0]    # monImage est l'image 0. Modifier le chiffre pour prendre une autre image.
monLabel = labels[0]    # monLabel est le label 0. Modifier le chiffre pour regarder un autre label.

monImageListe = transformeImageEnListe(monImage)

montre2Caracteristiques (images,labels,11,13,[0,1])