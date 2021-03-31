from fonction import vecteurDeplacement, monJeu

M0M1 = vecteurDeplacement(0,12)
M1M2 = vecteurDeplacement(4,2)
M2M3 = vecteurDeplacement(6,0)
M3M4 = vecteurDeplacement(4,-2)
M4M5 = vecteurDeplacement(0,-6)
M5M6 = vecteurDeplacement(-6,-6)

monJeu([M0M1,M1M2,M2M3,M3M4,M4M5,M5M6])


