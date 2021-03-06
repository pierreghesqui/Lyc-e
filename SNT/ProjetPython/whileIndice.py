hauteurTourEffel = 324
epaisseurPapier = 0.0001
nbDeFoisPliage = 0

#Tant que l'épaisseur de papier est inférieure à la hauteur de la tour effel
    #Je  plie la feuille de papier (cad je multiplie par 2 son epaisseur)
    #Je compte le nombre de fois que je plie
    
while epaisseurPapier<hauteurTourEffel:
    epaisseurPapier= epaisseurPapier*2
    print(epaisseurPapier)
    nbDeFoisPliage = nbDeFoisPliage+1

print(nbDeFoisPliage)