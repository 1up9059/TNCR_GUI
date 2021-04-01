import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt


import pdb

class img_analisys():

    def __init__(self, img_name, img):

        self.dotslist = []
        self.img_name = img_name
        self.img = img
        self.img_oricopy = img.copy()
        self.drawing = False
        self.thickness_contour = 10
        
    def show_image(self):
        cv2.imshow(self.img_name, self.img)
        
    def image_in_memory(self):
        self.dotslist = []

    def draw_dots(self, event1, x, y, flags, param):
        #dibuja un punto al dar click
        if event1 == cv2.EVENT_LBUTTONDOWN: #and event2 == cv2.EVENT_FLAG_SHIFTKEY:
            self.drawing = True
            self.ix = x
            self.iy = y
            dot = [x,y]
            self.dotslist.append(dot)
        
        elif event1 == cv2.EVENT_MOUSEMOVE: #and event2 == cv2.EVENT_FLAG_SHIFTKEY:
            
            if self.drawing == True:
                cv2.line(self.img, (x,y), (x,y), (0,255,0), self.thickness_contour)
                x = x
                y = y 
                dot = [x, y]
                self.dotslist.append(dot)

        elif event1 == cv2.EVENT_LBUTTONUP:
            self.drawing = False 
            cv2.line(self.img, (x,y), (x,y), (0,255,0), self.thickness_contour)

        elif event1 == cv2.EVENT_RBUTTONDOWN:
            self.dotlist = []
        
        return self.dotslist

    def Croped(self):
            
        rect = cv2.boundingRect(np.asarray(self.dotslist))#encontramos los limites maximos del contorno
        (x,y,w,h) = rect#Tomamos los limites maximos y los capturamos en x, y, w, h
        croped_rect = self.img[y:y+h, x:x+w].copy()#Cortmaos la seccion rectangular de la imagen con las dimensiones maximas del contorno
        
        self.dotslist = self.dotslist - self.dotslist.min(axis=0)#reajustamos el dolist, a partir del min para que no se pegue en la esquina de la image
        mask_contour = np.zeros(croped_rect[:2], dtype = np.uint8)#Cremaos la plantilla para pegar la image recortada
        cv2.drawContours(mask_contour, [self.dotslist], -1, (225,255,255), -1, cv2.LINE_AA)#se dibuja el contorno
        dts = cv2.bitwise_and(croped_rect, croped_rect, mask = mask_contour)#se corta el sector 

        return [dts, mask_contour, croped_rect, self.dotslist]

    def image_histogram(self, mask):
        
        return cv2.calcHist([self.img], [0], mask, [256], [0,256])

    def listing(self, y):
        
        y1 = []
        for i in range(len(y)):
            y1.append(y[i][0]) 
        return y1
    
    def img_writer(self, save_img_path):

        cv2.imwrite(save_img_path, self.img)
