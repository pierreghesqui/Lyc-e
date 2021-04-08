import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

def montreLimage(image,label='label non indiqué'):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.imshow(image,cmap='gray', vmin=np.min(image), vmax=np.max(image))
    plt.title(str(label))
    ax.plot()
    
def importationDesImagesEtLabels():
    digits = datasets.load_digits()
    images = digits.images
    Y = digits.target
    return images, Y

def nearestNeighbour(x,X_train,y_train):
    minimalDistance = 10*100
    y = -1
    for i in range(len(X_train)):
        x_train_i = X_train[i]  
        dist = np.linalg.norm(x-x_train_i)
        if dist<minimalDistance:
            minimalDistance = dist
            y=y_train[i]
    return y

def aplatirImages(images):
    
    if len(images.shape)>2:
        s1,s2,s3 = images.shape
        imagesAplaties = np.zeros((s1,s2*s3))
        for i in range(s1):
            imagesAplaties[i,:] = np.resize(images[i],(1,64))
    else:
        imagesAplaties = np.resize(images,(1,64))
    return imagesAplaties

def representation2D (imagesAplaties,labels,carac1,carac2,possibleLabels=[0,1,2,3,4,5,6,7,8,9]):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    plt.xlim([0, 20])
    plt.ylim([0, 20])
    colors = ['black','blue','orange','red','green','mediumpurple', 'lightslategrey','sandybrown','chartreuse','aquamarine']
    for label_i in possibleLabels:
        ind_label_i = labels==label_i
        image_label = imagesAplaties[ind_label_i,:]
        for k in range(len(image_label)):
            #print(image_label[k,carac1],image_label[k,carac2])
            plt.annotate(str(label_i),
                         (image_label[k,carac1],image_label[k,carac2]),
                         horizontalalignment='center',
                         verticalalignment='center',
                         size=11,
                         color=colors[label_i])
    ax.plot()
           
        
            
    
'''
n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
Y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, shuffle=False)

cpt = 0
listFalse =[]
resultFalse=[]
for k in range(len(X_test)):
    y = nearestNeighbour(X_test[k],X_train,y_train)
    test = y==y_test[k]
    if test:
        cpt=cpt+1
    else: 
        listFalse.append(k) 
        resultFalse.append(y)
precision = cpt/len(X_test)

plt.imshow(digits.images[195], cmap=plt.cm.gray_r, interpolation='nearest')
'''