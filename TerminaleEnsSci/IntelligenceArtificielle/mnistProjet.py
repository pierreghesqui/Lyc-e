from scipy.io import loadmat
import matplotlib.pyplot as plt
import cv2
import numpy as np
dataset = loadmat('mnist-original.mat')

#--------------------------------------
num=31000
X = dataset["data"]
Y = dataset["label"]
x = X[:,num]
img = np.zeros((28,28))
print(Y[0,num])
cpt = 0

for l in range(28):
    for c in range(28):
        img[l,c] = x[cpt]
        cpt = cpt+1

plt.imshow(img,cmap='gray')
        
        