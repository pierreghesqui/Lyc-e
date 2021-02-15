import keyboard
import time

cpt=0
pression=True

tpsInitial=time.time()
tpsFinal=tpsInitial+5

#____________________________________________________________________

while time.time()<tpsFinal:
    if keyboard.is_pressed('ctrl'):
        if pression==True:
            cpt=cpt+1
            #print('Vous avez appuyé',cpt,'fois la touche CTRL')
            pression=False
    else:
        pression=True
        
print('Vous avez appuyé',cpt,'fois la touche CTRL')      