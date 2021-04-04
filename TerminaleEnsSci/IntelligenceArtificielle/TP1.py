from function2 import *
import numpy as np

images, labels = importationDesImagesEtLabels()

image0 = images[0]
label0 = labels[0]
#montreLimage(image0)
imagesAplaties = aplatirImages(images)
representation2D(imagesAplaties[0:1000,:],labels[0:100],27,28,[0,1])

