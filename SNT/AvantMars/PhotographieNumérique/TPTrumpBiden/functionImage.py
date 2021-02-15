import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor

def showImage(image,fonts=15):
    sha=np.shape(image)
    pas = 1
    if max(sha)>50:
        pas = 50 
    if np.shape(sha)[0]==2:
         fig, ax = plt.subplots()
         ax.imshow(image,cmap='gray', vmin=0,vmax=255)
         ax.set_xticks(np.arange(0, sha[1], pas))
         ax.set_xticklabels(np.arange(0, sha[1], pas),rotation = 90,fontsize=fonts)
         
         ax.set_yticks(np.arange(0, sha[0], pas))
         ax.set_yticklabels(np.arange(0, sha[0], pas),fontsize=fonts)
         
         mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'),
                         formatter='ligne, colonne = {i}, {j}\nintensite = {z:.0f}'.format)
         mng = plt.get_current_fig_manager()
         mng.window.showMaximized()
         plt.show()
         
         

