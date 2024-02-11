import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class edgeDetection:
    def __init__(self):
        pass
    def Canny_detector(self,impath):
        """To be Implemented in future"""
        image = cv2.imread(impath,0)
        edge_image = cv2.Canny(image,100,200)
        return edge_image
    def Marr_Hilderth(self):
        """To be done in future"""
        pass