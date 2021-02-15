import numpy as np
import cv2
import keyboard
import time
import random

def updateMobilePosition (mobile,direction):
    l1 = (mobile[0,0]-25)%1000
    l2 = (mobile[0,0] +25)%1000
    c1 = (mobile[1,0]-25)%1000
    c2 = (mobile[1,0] + 25)%1000
    img[l1:l2,c1:c2,0] = 0
 
    if direction == 'up':
        mobile[0,0] = mobile[0,0]-pas
    elif direction == 'down':
        mobile[0,0] = mobile[0,0] +pas
    elif direction == 'left':
        mobile[1,0] = mobile[1,0] -pas
    elif direction == 'right':
        mobile[1,0] = mobile[1,0] +pas
        
    l1 = (mobile[0,0]-25)%1000
    l2 = (mobile[0,0] +25)%1000
    c1 = (mobile[1,0]-25)%1000
    c2 = (mobile[1,0] + 25)%1000
    
    img[l1:l2,c1:c2,0] = 255

def putSugar():
    img[sugar[0,0]-10:sugar[0,0]+10,sugar[1,0]-10:sugar[1,0]+10,2] = 0
    l = random.randint(10,990)
    c = random.randint(10,990)
    sugar[0,0]=l
    sugar[1,0]=c
    img[l-10:l+10,c-10:c+10,2] = 255
    
def updateSugar():
    if (mobile[0,0]+25)%1000>sugar[0,0] and (mobile[0,0]-25)%1000<sugar[0,0] and (mobile[1,0]+25)%1000>sugar[1,0]and  (mobile[1,0]-25)%1000<sugar[1,0]:
        putSugar()

    
def getFrame(direction):
    updateSugar()
    updateMobilePosition(mobile,direction)
    


def setDirection(direction):
    if keyboard.is_pressed("left"):
        direction = 'left'
    elif keyboard.is_pressed("right"):
        direction = 'right'
    elif keyboard.is_pressed("up"):
        direction = 'up'
    elif keyboard.is_pressed("down"):
        direction = 'down'        
    return direction

mobile = np.zeros((2,1),dtype = int)
sugar = np.zeros((2,1),dtype = int)
direction = 'right'
pas = 5
img = np.zeros((1000,1000,3),dtype = np.uint8)
putSugar()
cpt=0


while not keyboard.is_pressed('a'):
    t1 = time.time()
    direction = setDirection(direction)
    getFrame(direction)        
    cv2.imshow('image',img)
    cv2.waitKey(30)
    t2 = time.time()
    print(t2-t1)