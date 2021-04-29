import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import cv2

def montreLimage(image,label='label non indiqué'):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.imshow(image,cmap='gray', vmin=np.min(image), vmax=np.max(image))
    if label !='label non indiqué' :
        plt.title(str(label))
    ax.plot()
    
def importerEnsembleEntrainement():
    plt.close('all')
    np.random.seed(1)
    image,label = importationDesImagesEtLabels()
    nbElement = np.shape(label)[0]
    nbTest = int(0.003*nbElement)
    L1 = np.ones((nbTest))
    L2 = np.zeros((nbElement-nbTest))
    L = np.concatenate((L1,L2))
    np.random.shuffle(L)
    imageTest = image[np.where(L)]
    imageEntrainement = image[np.where(1-L)]
    labelTest = label[np.where(L)]
    labelEntrainement = label[np.where(1-L)]
    
    return imageEntrainement, labelEntrainement

def importerEnsembleTest():
    np.random.seed(1)
    image,label = importationDesImagesEtLabels()
    nbElement = np.shape(label)[0]
    nbTest = int(0.003*nbElement)
    L1 = np.ones((nbTest))
    L2 = np.zeros((nbElement-nbTest))
    L = np.concatenate((L1,L2))
    np.random.shuffle(L)
    imageTest = image[np.where(L)]
    imageEntrainement = image[np.where(1-L)]
    labelTest = label[np.where(L)]
    labelEntrainement = label[np.where(1-L)]
    return imageTest
    
def importationDesImagesEtLabels():
    plt.close('all')
    digits = datasets.load_digits()
    images = digits.images
    Y = digits.target
    return images, Y

def importerUneImageTest(path):
    imgTest = np.sum(255-cv2.imread(path),2)/(255*3)
    imgTest = cv2.resize(imgTest,(8,8),interpolation=cv2.INTER_AREA)>0.015
    imgTest = imgTest*16
    return imgTest

def distanceEntre2Images(img0,img1):
    liste0 = transformeImageEnListe(img0)
    liste1 = transformeImageEnListe(img1)
    distance = distanceEntre2Listes(liste0,liste1)
    return distance

def distanceEntre2Listes(liste0,liste1):
    distance = np.sqrt(np.sum((liste0-liste1)**2))
    return distance

def transformeImageEnListe(images):
    
    if len(images.shape)>2:
        s1,s2,s3 = images.shape
        imagesAplaties = np.zeros((s1,s2*s3))
        for i in range(s1):
            imagesAplaties[i,:] = np.resize(images[i],(1,64))
    else:
        imagesAplaties = np.resize(images,(1,64))
    return imagesAplaties

def montre2Caracteristiques (images,labels,carac1,carac2,possibleLabels=[0,1,2,3,4,5,6,7,8,9]):
    imagesAplaties = transformeImageEnListe(images)

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
    plt.xlabel("Valeur du pixel n° "+str(carac1),fontsize=13)
    plt.ylabel("Valeur du pixel n° "+str(carac2),fontsize=13)
    ax.set_xticks(np.arange(0, 17, 2))
    ax.set_yticks(np.arange(0, 17, 2))
    plt.grid()
    plt.title ("montre2Caracteristiques(images, labels, "+ str(carac1)+", " + str(carac2)+ ", " +str(possibleLabels)+" )", fontsize=13)
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