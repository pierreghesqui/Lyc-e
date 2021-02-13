epaisseurFeuille = 0.001
nbDeFoisPlie = 0

while epaisseurFeuille < 324 : #   >= veut dire supérieur ou égal
    epaisseurFeuille = 2*epaisseurFeuille
    nbDeFoisPlie = nbDeFoisPlie + 1
    print(epaisseurFeuille)
    
print(nbDeFoisPlie)

