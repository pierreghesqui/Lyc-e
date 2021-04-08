from fonctionsTP1 import *


#-----------TRAVAIL 2 ---------------------------------------------------
images, labels = importationDesImagesEtLabels()
imagesAplaties = aplatirImages(images)
representation2D(imagesAplaties[0:1000,:],labels[0:1000],27,28,[0,1])

X_train, X_test, y_train, y_test = train_test_split(
    imagesAplaties, labels, test_size=0.25, shuffle=False)
#X_train =X_train[:,[27,28]]
#X_test = X_test[:,[27,28]]
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
