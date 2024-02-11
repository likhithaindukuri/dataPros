import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class DataAugmentation:
    def __init__(self):
        pass

    def flip(self, num, datadir, targetdir):
        """
        Flip images horizontally or vertically.

        Args:
            num (int): 0 for flipping around the x-axis (vertical flip), positive value for flipping around the y-axis (horizontal flip).
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the flipped images will be saved.
        """
        try:
            if not os.path.exists(targetdir + "/flip"):
                os.mkdir(targetdir + "/flip")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    flip = cv2.flip(img, num)
                    plt.imsave(os.path.join(targetdir, "flip", "flip-" + image), flip)
                except Exception as e:
                    print("Error occurred in flipping:", e, "for image:", image)
        return

    def rotate(self, angle, datadir, targetdir):
        """
        Rotate images by a given angle.

        Args:
            angle (float): Angle by which the images will be rotated clockwise.
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the rotated images will be saved.
        """
        try:
            if not os.path.exists(targetdir + "/rotate"):
                os.mkdir(targetdir + "/rotate")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    rotated = imutils.rotate(img, angle)
                    plt.imsave(os.path.join(targetdir, "rotate", "rotate-" + image), rotated)
                except Exception as e:
                    print("Error occurred in rotating:", e, "for image:", image)
        return

    def brightInc(self, datadir, targetdir):
        """
        Increase brightness of images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the brightened images will be saved.
        """
        try:
            if not os.path.exists(targetdir + "/inbrighten"):
                os.mkdir(targetdir + "/inbrighten")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    bright = np.ones(img.shape, dtype="uint8") * 70
                    bright_add = cv2.add(img, bright)
                    plt.imsave(os.path.join(targetdir, "inbrighten", "inbrighten-" + image), bright_add)
                except Exception as e:
                    print("Error occurred in brightening:", e, "for image:", image)
        return

    def brightDec(self, datadir, targetdir):
        """
        Decrease brightness of images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the darkened images will be saved.
        """
        try:
            if not os.path.exists(targetdir + "/debrighten"):
                os.mkdir(targetdir + "/debrighten")
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    bright = np.ones(img.shape, dtype="uint8") * 70
                    bright_sub = cv2.subtract(img, bright)
                    plt.imsave(os.path.join(targetdir, "debrighten", "debrighten-" + image), bright_sub)
                except Exception as e:
                    print("Error occurred in darkening:", e, "for image:", image)
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
