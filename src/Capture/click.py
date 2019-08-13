# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 07:33:05 2018

@author: Prashant
"""



import cv2 
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
print(ret)
print(frame)
cv2.imwrite("sd.jpg", frame)
cam.release()