import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils

class ImageFilter:
    def __init__(self):
        pass

    def median(self, datadir, targetdir):
        """
        Apply median filter to images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the filtered images will be saved.
        """
        try:
            if not os.path.exists(os.path.join(targetdir, "median")):
                os.mkdir(os.path.join(targetdir, "median"))
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    median = cv2.medianBlur(img, 5)
                    plt.imsave(os.path.join(targetdir, "median", "median-" + image),
                               cv2.cvtColor(median, cv2.COLOR_RGB2BGR))
                except Exception as e:
                    print("Error occurred in Median filter:", e, "for image:", image)

    def laplacian(self, datadir, targetdir):
        """
        Apply Laplacian filter to images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the filtered images will be saved.
        """
        try:
            if not os.path.exists(os.path.join(targetdir, "laplacian")):
                os.mkdir(os.path.join(targetdir, "laplacian"))
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    lap = cv2.Laplacian(img, cv2.CV_64F)
                    cv2.imwrite(os.path.join(targetdir, "laplacian", "laplacian-" + image), lap)
                except Exception as e:
                    print("Error occurred in Laplacian filter:", e, "for image:", image)

    def gaussian(self, datadir, targetdir):
        """
        Apply Gaussian filter to images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the filtered images will be saved.
        """
        try:
            if not os.path.exists(os.path.join(targetdir, "gaussian")):
                os.mkdir(os.path.join(targetdir, "gaussian"))
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    gb = cv2.GaussianBlur(img, (3, 3), 1, 1)
                    cv2.imwrite(os.path.join(targetdir, "gaussian", "gaussian-" + image), gb)
                except Exception as e:
                    print("Error occurred in Gaussian filter:", e, "for image:", image)

    def bilateral(self, datadir, targetdir):
        """
        Apply bilateral filter to images.

        Args:
            datadir (str): Path to the directory containing the input images.
            targetdir (str): Path to the directory where the filtered images will be saved.
        """
        try:
            if not os.path.exists(os.path.join(targetdir, "bilateral")):
                os.mkdir(os.path.join(targetdir, "bilateral"))
        except Exception as err:
            print("Error occurred while creating folder")

        for image in os.listdir(datadir):
            img = cv2.imread(os.path.join(datadir, image))
            if img is not None:
                try:
                    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
                    plt.imsave(os.path.join(targetdir, "bilateral", "bilateral-" + image), bilateral)
                except Exception as e:
                    print("Error occurred in Bilateral filter:", e, "for image:", image)
