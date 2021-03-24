listeDeNomConnu = ["Batman", "Spyderman", "Licorne", "Marie"]
nomDeLutilisateur = input("Comment tu t'apelles ?" )
jeConnaisTonNom = 0

for i in range(0,4):
    nom_i = listeDeNomConnu[i]
    if nom_i == nomDeLutilisateur : 
        print("Je connais ton nom ! ")
