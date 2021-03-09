import numpy as np
import cv2
import keyboard

img = np.zeros((500,500))

while not keyboard.is_pressed('ctrl'):
    cv2.imshow('pierre',img)
    cv2.waitKey(100)
    
cv2.destroyWindow('pierre')




