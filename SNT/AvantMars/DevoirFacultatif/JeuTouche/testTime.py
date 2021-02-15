import time #permet d'utiliser la fonction time.time() et time.sleep()

tStart = time.time() #on regarde le temps
time.sleep(3) #on attend 3 secondes
tEnd = time.time()  #on regarde le nouveau temps

duree = tEnd-tStart #On mesure la durée entre les deux temps
print(duree)      
