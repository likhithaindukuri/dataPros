import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class dataAugmenation:
    def __init__(self):
        pass
    def flip(self,num,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/flip"):
            os.mkdir(targetdir+"/flip")
        except Exception as err:
            print("Error occurred while creating folder")
        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              flip = cv2.flip(img,num)
              plt.imsave(targetdir+"/flip/flip-"+image,flip)
            except Exception as e:
              print("Error occured in Flipping")
        return
    def rotate(self,angle,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/rotate"):
            os.mkdir(targetdir+"/rotate")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              rotated = imutils.rotate(img,angle)
              plt.imsave(targetdir+"/rotate/rotate-"+image,rotated)
            except Exception as e:
              print("Error occured in Rotating")
        return
    def brightInc(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/inbrighten"):
            os.mkdir(targetdir+"/inbrighten")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              bright = np.ones(img.shape,dtype= "uint8")*70
              bright_add = cv2.add(img,bright)
              plt.imsave(targetdir+"/inbrighten/inbrighten-"+image,bright_add)
            except Exception as e:
              print("Error occured in brighten")
        return
    def brightDec(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/debrighten"):
            os.mkdir(targetdir+"/debrighten")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              bright = np.ones(img.shape,dtype= "uint8")*70
              bright_sub = cv2.subtract(img,bright)
              plt.imsave(targetdir+"/debrighten/debrighten-"+image,bright_sub)
            except Exception as e:
              print("Error occured in brighten")
        return
    def zoomin(self):
      """To be done in Future"""
      pass
    def zoomout(self):
      """To be done in Future"""
      pass
    def crop(self):
      """To be done in Future"""
      pass
    def shear(self):
      """To be done in Future"""
      pass