# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:05:55 2018

@IDE: Spyder

@author: Prashant
"""
import cv2
    
class Image:
    """
    @class
    """
    def __init__(self, image):
        
        self.image = cv2.imread(image)
        self.edit_image = self.image.copy()
        
#       Convert grayscale
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
#       threshold the image to binary
        self.binary_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
#       Inverted binary image
        self.binary_img_inv = cv2.bitwise_not(self.binary_img)
        
#       Dimension of image
        self.__height, self.__width = image.shape
        
        self.lines = []
        
    def show(self, image):
        """@view: show the image"""
        
        cv2.namedWindow('Component', cv2.WINDOW_NORMAL)
        cv2.imshow('Component', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def lineSegment(self):
        line_start = False
        val = 0
        for i in range(self.__height-1):
            freq = 0
            for j in range(self.__width-1):
                if self.binary_img[i][j] == 0:
                    freq+=1
            if freq > 5:
                if not line_start:
                    val = i
                    line_start = True
            else:
                if line_start:
                    self.lines.append((val,i))
                line_start = False
        return self.lines
    def drawLine(self):
        for cord in self.lines:
            cv2.line(self.edit_image,(0,cord[0]-2),(self.__width,cord[0]-2),(255,0,0),1)
            cv2.line(self.edit_image,(0,cord[1]+2),(self.__width,cord[1]+2),(255,0,0),1)
    def getLine(self, cord):
        y = cord[0]
        y1= cord[1]
        w = self.__width
        crop_img = self.binary_img[y-1:y1+1, 0:w]
        return crop_img

    def wordSegment(self, cord):
        line_start = False
        val = 0
        words = []
        for j in range(self.__width):
            freq = 0
            for i in range(cord[0], cord[1]):
                if self.binary_img[i][j] == 0:
                    freq +=1
            if freq > 1:
                if not line_start:
                    val = j
                    line_start = True
            else:
                if line_start:
                    words.append((val,j))
                line_start = False
        return words
    
img = Image("inv.jpg")
line_cords = img.lineSegment()
#img.drawLine()
#img.getLine(line_cords[1])
for line_cord in line_cords:
    word_cords = img.wordSegment(line_cord)
    for word_cord in word_cords:
        cv2.rectangle(img.edit_image, (word_cord[0], line_cord[0]), (word_cord[1], line_cord[1]), (0,255,0),1)
#for word in word_cords:
img.show(img.image)
cv2.imwrite("output.png",img.edit_image)
#    [line_cords[1][0]:line_cords[1][1], word[0]:word[1]]