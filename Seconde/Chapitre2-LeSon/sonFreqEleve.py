import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
duration = 10
for fs in [1, 10,15,20,25,30,40,50,70,100,1000,10000,15000,16000,17000,18000,19000,20000,21000,22000,23000,24000,25000,26000]:
    
        if fs<5000:
            samplerate = 44000
        else: 
            samplerate = 10*fs
            
        
        t = np.linspace(0., duration, duration*samplerate)
        #amplitude = np.iinfo(np.int16).max
        data =  np.sin(2. * np.pi * fs * t)
        #plt.plot(t[1:100],data[1:100])
        #plt.show()
        name = "sonFreq_%d.wav"%(fs)
        write(name, samplerate, data)
    
