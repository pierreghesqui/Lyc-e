from functionImage import showImage
import matplotlib.pyplot as plt
import numpy as np

image1 = np.zeros((3,4))

image1[0,1] = 255
image1[1,0] = 150
image1[1,2] = 255
image1[2,3] = 155

showImage(image1,25)


