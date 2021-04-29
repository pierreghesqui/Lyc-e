from fonctionsTP3 import *

images, labels = importationDesImagesEtLabels()
imageTest  = importerUneImageTest('image5.png') #modifier 'image5.png' pour 
                                            #importer une image de votre choix 

# Distance entre l'imageTest et l'imgs_entr[0] :
distance = distanceEntre2Images(imageTest,images[0])


#Coder l'algorithme du plus proche voisin
cpt  = 0
cptMin = 0
distanceMin = 100000000000000 

while cpt < 1792:
    distance = distanceEntre2Images(imageTest,images[cpt])
    if distance <distanceMin:
        distanceMin=distance
        labelMin = labels[cpt]
        cptMin = cpt
        
    cpt = cpt+1






