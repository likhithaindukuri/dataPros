import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class imageTransform:
    def log_transform(self, impath):
      c = 35
      inp = cv2.imread(impath,0)
      opt = np.zeros((inp.shape[0], inp.shape[1]))
      for m in range(0, inp.shape[0]):
          for n in range(0, inp.shape[1]):
              opt[m, n] = c * np.log(1 + inp[m, n])
      return opt
    def power_law_transform(self,impath):
      gama = 1.3
      constant = 1
      inp = cv2.imread(impath,0)
      opt = np.zeros((inp.shape[0], inp.shape[1]))
      for m in range(0, inp.shape[0]):
          for n in range(0, inp.shape[1]):
              opt[m, n] = constant * np.power(inp[m, n], gama)
      return opt
    def histogram_equalization(self,impath):
        inp = cv2.imread(impath,0)
        opt = np.zeros((inp.shape[0], inp.shape[1]))
        hist_vals = np.zeros([1,256])
        for m in range(0,inp.shape[0]):
            for n in range(0,inp.shape[1]):
                hist_vals[0][inp[m,n]] +=1
        normalized_hist = hist_vals/(inp.shape[0]*inp.shape[1])
        for m in range(0,inp.shape[0]):
            for n in range(0,inp.shape[1]):
                 indices = np.arange(inp[m,n])
                 cdf = normalized_hist[0][indices].sum()
                 opt[m,n] = 255*cdf
        return opt
    def negative_image(self,impath):
        inp = cv2.imread(impath,0)
        L = 256
        opt = np.zeros((inp.shape[0], inp.shape[1]));
        for m in range(0, inp.shape[0]):
            for n in range(0, inp.shape[1]):
                opt[m, n] = L - 1 - inp[m, n]
        return opt