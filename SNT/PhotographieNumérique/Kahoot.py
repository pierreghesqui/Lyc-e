from functionImage import showImage
import matplotlib.pyplot as plt
import numpy as np

image_24 = np.zeros((4,5))

for alexa in range(1,4):
    for dounia in range(1,3):
        image_24[alexa,dounia] = 255


showImage(image_24)

