import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

plt.close('all')

nbPeriode = 5.2
nbPointParPeriode = 100
npPointTot = round(nbPointParPeriode*nbPeriode)
f = 440 #Hz
f2 = 440

tsec = np.linspace(0,nbPeriode/f,npPointTot )
tsec2 = tsec+0.135*1/f
tmil = tsec*1000

sonFlute   = 10*(2*np.cos(2*np.pi*f*tsec2+1)+0.7*np.cos(4*np.pi*f*tsec2+2)+0.5*np.cos(8*np.pi*f*tsec2+3) +\
0.4*np.cos(16*np.pi*f*tsec2+5))

sonGuitare =0.5*( np.cos(2*np.pi*f2*tsec2+2.5) + 0.5*np.cos(4*np.pi*f2*tsec2+3) + 0.5*np.cos(8*np.pi*f2*tsec2+3.8) + \
0.4*np.cos(16*np.pi*f2*tsec2+5) + 0.4*np.cos(32*np.pi*f2*tsec2+6))
    
sonDiapason = 2*np.cos(2*np.pi*f2*tsec2+2.9)

tmin = round(min(tmil))
tmax = round(max(tmil))
# COURBE 1

fig1,ax1 = plt.subplots()
ax1.plot(tmil, sonFlute,color="black", linewidth = 2.5, linestyle="-")
ax1.grid(True)
ax1.set_xlabel('Temps (ms)', fontsize=20)
ax1.set_ylabel('Flute',fontsize=20)

ax1.xaxis.set_major_locator(MultipleLocator(1))

ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

ax1.set_xticks(np.arange(tmin, tmax+1, 1))
ax1.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)
ax1.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax1.set_yticks(np.arange(round(min(sonFlute)), round(max(sonFlute))+2,5))
ax1.set_yticklabels(np.arange(round(min(sonFlute)), round(max(sonFlute))+2, 5),fontsize=15)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.show()

# COURBE 2
fig2,ax2 = plt.subplots()

ax2.plot(tmil, sonGuitare,color="black", linewidth = 2.5, linestyle="-")
ax2.grid(True)
ax2.set_xlabel('Temps (ms)', fontsize=20)
ax2.set_ylabel('Guitare',fontsize=20)
ax2.xaxis.set_major_locator(MultipleLocator(1))

ax2.xaxis.set_minor_locator(MultipleLocator(0.5))

ax2.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax2.set_xticks(np.arange(tmin, tmax+1, 1))
ax2.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)
ax2.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax2.set_yticks(np.arange(round(min(sonGuitare)), round(max(sonGuitare))+0.5,1))
ax2.set_yticklabels(np.arange(round(min(sonGuitare)), round(max(sonGuitare))+0.5, 1),fontsize=15)
ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()

# COURBE 3
fig3,ax3 = plt.subplots()

ax3.plot(tmil, sonDiapason,color="black", linewidth = 2.5, linestyle="-")
ax3.grid(True)
ax3.set_xlabel('Temps (ms)', fontsize=20)
ax3.set_ylabel('Diapason',fontsize=20)
ax3.xaxis.set_major_locator(MultipleLocator(1))

ax3.xaxis.set_minor_locator(MultipleLocator(0.5))

ax3.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax3.set_xticks(np.arange(tmin, tmax+1, 1))
ax3.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)
ax3.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax3.set_yticks(np.arange(round(min(sonGuitare)), round(max(sonGuitare))+0.5,1))
ax3.set_yticklabels(np.arange(round(min(sonGuitare)), round(max(sonGuitare))+0.5, 1),fontsize=15)
ax3.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()