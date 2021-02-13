import numpy as np
r = (5/2)*0.01 #cm
p = 2*np.pi*r
nbTour = 120
nbBobine = 6

l = nbTour*nbBobine*p
print(l)