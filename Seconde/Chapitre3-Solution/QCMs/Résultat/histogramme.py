import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
#plt.close('all')
titre='QCM5.xlsx'
data = pd.read_excel (titre) 
includeZeros = False
score = pd.DataFrame(data, columns= ['Unnamed: 9'])
score = score.to_numpy()
score = score[8:np.shape(score)[0]]
score = np.round(score.astype(np.double))
score = np.concatenate( score, axis=0 )
#Supprimer les 0
if includeZeros : 
    mask = np.ones(np.shape(score), dtype=bool)
else:
    mask = score!=0
score=score[mask]

totalScore = pd.DataFrame(data, columns= ['Unnamed: 8'])
totalScore = totalScore.to_numpy()
totalScore = totalScore[8:np.shape(totalScore)[0]]
totalScore = np.round(totalScore.astype(np.double))
totalScore = np.concatenate( totalScore, axis=0 )
totalScore = totalScore[mask]
#totalScore = 
noteSur20 = np.round(20*np.divide(score,totalScore))
moyenne = np.round(np.mean(noteSur20, 0)*10)/10
ecartType = np.round(np.std(noteSur20, 0)*10)/10
fig1,ax1 = plt.subplots()


ax1.set_xlabel('Note /20' , fontsize=25)
ax1.set_ylabel('Nombre d élèves',fontsize=25)

ax1.hist(noteSur20 , bins = np.arange(-0.25,21, 0.5))

#plt.arrow(4, 4, 2, 0, width = 0.05)
plt.arrow(moyenne, 5, ecartType, 0, width = 0.05)
plt.arrow(moyenne, 5, -ecartType, 0, width = 0.05)
title = titre+"\n Nb : "+str(np.shape(noteSur20)[0])+  " ; Moyenne : "+ str(moyenne) +" ;  Ecart-type : "+str(ecartType)
plt.title(title,fontsize=30)
plt.grid('True')
plt.axvline(x=moyenne,color='k', linestyle='--')

ax1.set_xticks(np.arange(0, 21, 1))
ax1.set_xticklabels(np.arange(0, 21),fontsize=20)
ax1.set_yticklabels(ax1.get_yticks(),fontsize=20)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%d'))

mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.show()
