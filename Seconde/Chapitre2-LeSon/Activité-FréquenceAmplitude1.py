import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
'''
params = {'legend.fontsize': 100,
          'legend.handlelength': 2}
plt.rcParams.update(params)

'''
plt.close('all')
nbPeriode = 5.2
nbPointParPeriode = 100
npPointTot = round(nbPointParPeriode*nbPeriode)
f = 262 #Hz
f2 = 698 #Hz
tsec = np.linspace(0,nbPeriode/f,npPointTot )
tsec2 = tsec
tmil = tsec*1000
son1 = np.cos(2*np.pi*f*tsec2)
son2 = 10*np.cos(2*np.pi*f*tsec2)
son3 = np.cos(2*np.pi*f2*tsec2)
tmin = round(min(tmil))
tmax = round(max(tmil))
# COURBE 1

fig1,ax1 = plt.subplots()
ax1.plot(tmil, son1,color="black", linewidth = 2.5, linestyle="-")
ax1.grid(True)
ax1.set_xlabel('Temps (ms)', fontsize=20)
ax1.set_ylabel('Courbe n°1',fontsize=20)

ax1.xaxis.set_major_locator(MultipleLocator(1))

ax1.xaxis.set_minor_locator(MultipleLocator(0.5))
ax1.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

ax1.set_xticks(np.arange(tmin, tmax+1, 1))
ax1.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)
ax1.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax1.set_yticks(np.arange(round(min(son1)), round(max(son1))+0.5,1))
ax1.set_yticklabels(np.arange(round(min(son1)), round(max(son1))+0.5, 1),fontsize=15)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.show()

# COURBE 2
fig2,ax2 = plt.subplots()

ax2.plot(tmil, son2,color="black", linewidth = 2.5, linestyle="-")
ax2.grid(True)
ax2.set_xlabel('Temps (ms)', fontsize=20)
ax2.set_ylabel('Courbe n°2',fontsize=20)
ax2.xaxis.set_major_locator(MultipleLocator(1))

ax2.xaxis.set_minor_locator(MultipleLocator(0.5))

ax2.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax2.set_xticks(np.arange(tmin, tmax+1, 1))
ax2.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)
ax2.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax2.set_yticks(np.arange(round(min(son2)), round(max(son2))+0.5,5))
ax2.set_yticklabels(np.arange(round(min(son2)), round(max(son2))+0.5, 5),fontsize=15)
ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()

# COURBE 3
fig3,ax3 = plt.subplots()

ax3.plot(tmil, son3,color="black", linewidth = 2.5, linestyle="-")
ax3.grid(True)
ax3.set_xlabel('Temps (ms)', fontsize=20)
ax3.set_ylabel('Courbe n°3',fontsize=20)

ax3.xaxis.set_major_locator(MultipleLocator(1))

ax3.xaxis.set_minor_locator(MultipleLocator(0.5))
ax3.grid(which='major', linestyle='-', linewidth='0.75', color='black')
ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

ax3.set_xticks(np.arange(tmin, tmax+1, 1))
ax3.set_xticklabels(np.arange(tmin, tmax+1, 1),fontsize=15)

ax3.xaxis.set_major_formatter(FormatStrFormatter('%d'))

ax3.set_yticks(np.arange(round(min(son3)), round(max(son3))+0.5,1))
ax3.set_yticklabels(np.arange(round(min(son3)), round(max(son3))+0.5, 1),fontsize=15)
ax3.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()

