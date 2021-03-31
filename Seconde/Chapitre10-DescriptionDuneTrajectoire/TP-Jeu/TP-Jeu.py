from fonctionPotion import vecteurDeplacement, trajectoire

M0M1 = vecteurDeplacement(0,600)
M1M2 = vecteurDeplacement(200,100)
M2M3 = vecteurDeplacement(150,0)


M6M7 = vecteurDeplacement(200,-100)
M7M8 = vecteurDeplacement(0,-300)
M8M9 = vecteurDeplacement(-300,-300)

trajectoire([M0M1,M1M2,M2M3])

