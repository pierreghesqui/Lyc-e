import keyboard
import time

cpt = 0

for i in [3,2,1]:
    print(i)
    time.sleep(1)
print('top !')


montemps=time.time()
unPressOk = True
t = montemps
maxTime = 5 +montemps

while time.time()<maxTime:  
    
    if keyboard.is_pressed('ctrl') & unPressOk:   
        cpt = cpt + 1
        
        unPressOk = False
    
    if not keyboard.is_pressed('ctrl'):
        unPressOk = True
        
    
    if time.time()-t>1:
        #print(round(maxTime - time.time())) 
        t = time.time()

        
print('STOP !')
print('You pressed ctrl ', cpt, ' times.')
