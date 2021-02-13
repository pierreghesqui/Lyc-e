EnergieEcran = 209 #kWh
EnergieSecheLinge = 103 #kWh
EnergieFour = 86.5 #kWh
EnergieBox = 61.3 #kWh

EnergieReste = 77+59+53+51+50+42+38+27+26+12*20
heureAn = 24*365
EnergieTot = EnergieEcran+EnergieSecheLinge+EnergieFour+EnergieBox
Prix = EnergieTot*0.18

EnergieVeilleFrance= 40e6*EnergieTot


PuissanceEcran =EnergieEcran/heureAn*1000
PuissanceSecheLinge = EnergieSecheLinge/heureAn*1000
PuissanceFour=EnergieFour/heureAn*1000
PuissanceBox = EnergieBox/heureAn*1000
PuissanceTot = PuissanceEcran+PuissanceSecheLinge+PuissanceFour+PuissanceBox
PuiReact = 900e6
PuiTotFrance = PuissanceTot*30e6
nbReac = PuiTotFrance/PuiReact
