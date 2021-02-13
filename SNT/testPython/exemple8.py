def masseVolumique (m,v):
    rho = m/v
    return rho

saucisse = 1
while saucisse < 5:
    soupe = masseVolumique(saucisse,-saucisse)
    saucisse = saucisse + 1
    print(soupe)
    
    
    
    
    
