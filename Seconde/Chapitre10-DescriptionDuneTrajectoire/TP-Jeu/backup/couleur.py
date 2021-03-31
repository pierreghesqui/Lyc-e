import cv2
import numpy as np

img = np.zeros((1000,1000,3)) #J'ai ajouté un 3 pour qu'il y ait 3 canaux

img[20:40,20:40,0] = 1 #Le 0 indique que l'on remplit le canal bleu
img[40:60,40:60,1] = 1 #Le 1 indique que l'on remplit le canal vert
img[60:80,60:80,2] = 1 #Le 2 indique que l'on remplit le canal rouge


img[80:100,80:100,[0,2]] = 1 # bleu + rouge = violet-rose  


cv2.imshow('fenetre',img)
