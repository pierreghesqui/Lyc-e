from fonctionsTP2 import *

plt.close('all')
images, labels = importationDesImagesEtLabels() 
monImage = images[0]    # monImage est l'image 0. Modifier le chiffre pour prendre une autre image.
monLabel = labels[0]    # monLabel est le label 0. Modifier le chiffre pour regarder un autre label.
#montreLimage(monImage)  # J'affiche l'image "monImage"

monImageEnListe = transformeLimageEnListe(monImage)



