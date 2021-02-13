import numpy as np
import matplotlib.pyplot as plt
  
x = np.arange(1,10,1)
y = np.sin(x)
img=np.zeros((3,3))
plt.ion()
for i in range(3):
    img[(i,0)]=255
    plt.imshow(img,cmap='gray')
    plt.close()
    plt.pause(0.1)
  
r = input("> Je veux continuer a executer mon programme")

