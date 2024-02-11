import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils
import time
import sys


from .project_directory import imageTransform
from .imageFilter import imageFilter
from .edgeDetection import edgeDetection
from .dataAugmentation import dataAugmentation

class Pros(imageTransform, edgeDetection, imageFilter, dataAugmentation):
    def __init__(self):
        pass

    def update_progress(self, progress):
        barLength = 10
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "error: progress var must be float\r\n"
        if progress < 0:
            progress = 0
            status = "Halt...\r\n"
        if progress >= 1:
            progress = 1
            status = "Done...\r\n"
        block = int(round(barLength * progress))
        text = "\rprePros: [{0}] {1}% {2}".format("=" * block + ">" + "-" * (barLength - block), progress * 100,
                                                   status)
        sys.stdout.write(text)
        sys.stdout.flush()

    def imtransform(self, impath, oplist):
        res = []
        wholeList = ["log", "power", "histogram", "negative", "rgb2gb", "rgb2rb", "rgb2rg"]
        for i in oplist:
            if i not in wholeList:
                print("No filter found with name " + i)
                opt = None
            elif i == "log":
                opt = self.log_transform(impath)
            elif i == "power":
                opt = self.power_law_transform(impath)
            elif i == "histogram":
                opt = self.histogram_equalization(impath)
            elif i == "negative":
                opt = self.negative_image(impath)
            else:
                print("Not Found")
            res.append(opt)
        return res

    def edgeDetect(self, impath, name):
        if name == "cannyedge":
            opt = self.Canny_detector(impath)
        else:
            print("No detector found with name " + name)
        return opt

    def filter(self, datapath, targetpath, filters):
        progress = 0
        for j in filters:
            if j == "median":
                self.median(datapath, targetpath)
            elif j == "laplacian":
                self.laplacian(datapath, targetpath)
            elif j == "gaussian":
                self.gaussian(datapath, targetpath)
            elif j == "bilateral":
                self.bilateral(datapath, targetpath)
            else:
                print("Not found")
            progress = progress + (100 / len(filters))

            self.update_progress(progress / 100.0)

    def augment(self, datadir, targetdir, arguments):
        progress = 0
        for j in arguments:
            if j == "flip-H":
                self.flip(0, datadir, targetdir)
            elif j == "flip-V":
                self.flip(1, datadir, targetdir)
            elif j[0:6] == "rotate":
                self.rotate(int(j[6:]), datadir, targetdir)
            elif j == "shear":
                pass
            elif j == "crop":
                pass
            elif j == "zoomin":
                pass
            elif j == "zoomout":
                pass
            elif j == "in-brighten":
                self.in_brighten(datadir, targetdir)
            elif j == "de-brighten":
                self.de_brighten(datadir, targetdir)
            else:
                print("Not Found")
            progress = progress + (100 / len(arguments))
            self.update_progress(progress / 100.0)
