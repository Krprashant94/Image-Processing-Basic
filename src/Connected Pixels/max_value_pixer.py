# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:32:53 2018

@IDE: Spyder

@author: Prashant
"""

import cv2
import numpy as np
from numpy import max
from random import randint


class Image:
    """
    @class
    """
    def __init__(self, file=None, image=None):
        if file:
            self.image = cv2.imread(file)
        else:
            self.image = image
        self.border_image = self.image.copy()
        
#       Convert grayscale
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
#       threshold the image to binary
        self.binary_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
#       Inverted binary image
        self.binary_img_inv = cv2.bitwise_not(self.binary_img)
        
#       Find the connected component
        self.connectedPixelList = cv2.connectedComponentsWithStats(self.binary_img_inv,2, cv2.CV_32S)[1]
        
#       Dimension of image
        self.__height, self.__width = image.shape
        
    def noOfSegment(self):
        """@return (int) : no of deffrent/disconnected image"""
        return max(self.connectedPixelList)
    
    def getComponent(self, component):
        """
        @component (int) : component number 
        
        @return (cv2.image): cropped image
        """
        tmp = self.binary_img.copy()
        
#        color = (randint(0, 255),randint(0, 255),randint(0, 255))
        color = (0,255,0)
        for i in range(self.__height):
            for j in range(self.__width):                
                if self.connectedPixelList[i][j] != component:
                    tmp[i][j] = 255
        return tmp

    def getMaxIndex(self):
        pixel_list = []
        for i in range(1, img.noOfSegment()+1):
            crop = img.getComponent(i)
            pixel_list.append(len(np.where(crop == 0)[0]))

        print(pixel_list)
        max_index = np.argmax(pixel_list)
        return max_index+1
    def getMaxComponent(self):
        pass


img = Image(image=cv2.imread("dot.jpg"))

index = img.getMaxIndex()
crop = img.getComponent(index)

cv2.imwrite("output.jpg", crop)
print("done")