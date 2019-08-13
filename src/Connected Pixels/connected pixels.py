# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:32:53 2018

@IDE: Spyder

@author: Prashant
"""

import cv2
from numpy import max
from random import randint


class Image:
    """
    @class
    """
    def __init__(self, image):
        
        self.image = cv2.imread(image)
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
            
    def show(self, image):
        """@view: show the image"""
        
        cv2.namedWindow('Component', cv2.WINDOW_NORMAL)
        cv2.imshow('Component', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def noOfSegment(self):
        """@return (int) : no of deffrent/disconnected image"""
        return max(self.connectedPixelList)
    
    def getComponent(self, component):
        """
        @component (int) : component number 
        
        @return (cv2.image): cropped image
        """
        tmp = self.image.copy()
        
#        color = (randint(0, 255),randint(0, 255),randint(0, 255))
        color = (0,255,0)
        for i in range(self.__height-1):
            for j in range(self.__width-1):
#               Edge marking 
                try:
                    if self.connectedPixelList[i-1][j] != component and self.connectedPixelList[i][j] == component:
                        self.border_image[i-1, j] =  color
                    elif self.connectedPixelList[i+1][j] != component and self.connectedPixelList[i][j] == component:
                        self.border_image[i+1, j] =  color
                    elif self.connectedPixelList[i][j-1] != component and self.connectedPixelList[i][j] == component:
                        self.border_image[i, j-1] =  color
                    elif self.connectedPixelList[i][j+1] != component and self.connectedPixelList[i][j] == component:
                        self.border_image[i, j+1] =  color  
                except:
                    pass
                
                if self.connectedPixelList[i][j] != component:
                    tmp[i][j] = 255
        return tmp
                

img = Image("dot.jpg")

print("Total Disconnected Pixel Found : "+ str(img.noOfSegment()))

for i in range(1, img.noOfSegment()+1):
#    This function also creates a border in the image reflected at self.border_image
    crop = img.getComponent(i)
    #img.show(crop)
img.show(img.border_image)
cv2.imwrite( "s.jpg", img.border_image)