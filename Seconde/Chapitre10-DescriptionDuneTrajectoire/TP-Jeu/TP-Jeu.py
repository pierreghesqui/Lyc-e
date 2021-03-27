from fonction import vecteurDeplacement, listeVecteurDeplacement

M0M1 = vecteurDeplacement(0,600)
bonus = vecteurDeplacement(0,100)
M1M2 = vecteurDeplacement(200,100)
M2M3 = vecteurDeplacement(200,0)
M3M4 = vecteurDeplacement(0,-150)
M4M5 = vecteurDeplacement(0,+150)
M5M6 = vecteurDeplacement(100,0)
M6M7 = vecteurDeplacement(200,-100)
M7M8 = vecteurDeplacement(0,-300)
M8M9 = vecteurDeplacement(-300,-300)


vd1 = vecteurDeplacement(400,0)
vd2 = vecteurDeplacement(200,200)
listeVecteurDeplacement([M0M1, M1M2,M2M3,M3M4,M4M5,M5M6,M6M7,M7M8])
#[M0M1, M1M2,M2M3,M3M4,M4M5,M5M6,M6M7,M7M8,M8M9]

#