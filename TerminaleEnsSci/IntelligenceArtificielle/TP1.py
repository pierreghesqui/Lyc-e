from function2 import *
import numpy as np


#------------TRAVAIL 1 --------------------------------------------------
images, labels = importationDesImagesEtLabels()
image = images[1]
label = labels[1]
montreLimage(image)
imagesAplaties = aplatirImages(images)

#-----------TRAVAIL 2 ---------------------------------------------------
representation2D(imagesAplaties[0:1000,:],labels[0:1000],27,28,[0,1,2])

