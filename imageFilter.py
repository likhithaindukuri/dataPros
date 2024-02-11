import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class imageFilter:
    def __init__(self):
        pass
    def median(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/median"):
            os.mkdir(targetdir+"/median")
        except Exception as err:
            print("Error occurred while creating folder")
        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              median = cv2.medianBlur(img, 5)
              plt.imsave(targetdir+"/median/median-"+image, cv2.cvtColor(median, cv2.COLOR_RGB2BGR))
            except Exception as e:
              print("Error occured in Median filter")
    def laplacian(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/laplacian"):
            os.mkdir(targetdir+"/laplacian")
        except Exception as err:
            print("Error occurred while creating folder")
        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              lap = cv2.Laplacian(img,cv2.CV_64F)
              cv2.imwrite(targetdir+"/laplacian/laplacian-"+image,lap)
            except Exception as e:
              print("Error occured in laplacian filter")
        return
    def gaussian(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/gaussian"):
            os.mkdir(targetdir+"/gaussian")
        except Exception as err:
            print("Error occurred while creating folder")
        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              gb = cv2.GaussianBlur(img, (3, 3), 1, 1)
              cv2.imwrite(targetdir+ "/gaussian/gaussian-" + image, gb)
            except Exception as e:
              print("Error occured in gaussian filter")
        return
    def bilateral(self,datadir,targetdir):
        try:
          if not os.path.exists(targetdir+"/bilateral"):
            os.mkdir(targetdir+"/bilateral")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in list(os.listdir(datadir)):
          img = cv2.imread(datadir+"/"+image)
          if img is not None:
            try:
              bilateral = cv2.bilateralFilter(img, 9, 75, 75)
              plt.imsave(targetdir+"/bilateral//bilateral-"+image,bilateral)
            except Exception as e:
              print("Error occured in bilateral filter")
        return