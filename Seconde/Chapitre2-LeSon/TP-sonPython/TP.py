from functionTp6 import entendreLeSon, note,assemblerLesNotes,voirLeSignal
import numpy as np


sol_392_1 = note(392,0.05,0.5)
sol_392_2 = note(392,0.1,0.5)
sol_392_3 = note(392,1,0.5)
mi_311 = note(311,10,1.5)
fa_349_1 = note(349,0.05,0.5)
fa_349_2 = note(349,0.1,0.5)
fa_349_3 = note(349,1,0.5)
re_294 = note(294,10,1.5)
'''
sol_392_1 = note(392,1,0.5)
sol_392_2 = note(392,1,0.5)
sol_392_3 = note(392,1,0.5)
mi_311 = note(311,1,1.5)
fa_349_1 = note(349,1,0.5)
fa_349_2 = note(349,1,0.5)
fa_349_3 = note(349,1,0.5)
re_294 = note(294,1,1.5)
'''
signal1 = assemblerLesNotes( (sol_392_1,sol_392_2,sol_392_3,mi_311,fa_349_1,fa_349_2,fa_349_3,re_294 ) )


'''
sol_392_1 = note(392/2,0.05,0.5)
sol_392_2 = note(392/2,0.1,0.5)
sol_392_3 = note(392/2,1,0.5)
mi_311 = note(311/2,10,1.5)
fa_349_1 = note(349/2,0.05,0.5)
fa_349_2 = note(349/2,0.1,0.5)
fa_349_3 = note(349/2,1,0.5)
re_294 = note(294/2,10,1.5)


signal2 = assemblerLesNotes( (sol_392_1,sol_392_2,sol_392_3,mi_311,fa_349_1,fa_349_2,fa_349_3,re_294 ) )

signal3 = signal1+signal2/3
'''
entendreLeSon(signal1)
voirLeSignal(signal1)


'''
fe = 44100 
te = 1/fe 
duration = 1
freq1 = 440
freq2 = 880

t1 = np.arange(0,duration,te) 
y1 = np.sin(2 * np.pi* freq1 * t1)

t2 = np.arange(0,duration,te) 
y2 = np.sin(2 * np.pi* freq2 * t2)

t = np.concatenate((t1, t2+t1[-1]+te))
y = np.concatenate((y1,y2))

entendreLeSon(t, y)
'''