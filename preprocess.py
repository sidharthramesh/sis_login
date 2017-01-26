import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import scipy.misc
import cv2

def threshold(array):
    """Converts colour image array to thresholded binary"""
    img=array
    hdv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0,50,50])
    upper_blue = np.array([257,255,255])
    mask=cv2.inRange(hdv,lower_blue,upper_blue)
    res = cv2.bitwise_and(img,img,mask=mask)
    res[np.where((res == [0,0,0]).all(axis = 2))] = [255,255,255]
    blur = cv2.GaussianBlur(res,(5,5),0)
    bw=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    ret3,th3 = cv2.threshold(bw,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thr = cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return thr
def split_image(thr):
    return np.array([thr[:,34*i:34*(i+1)] for i in range(5)])
def process(img_path):
    thr=threshold(img_path)
    thr= split_image(thr)/255
    resize = np.array([cv2.resize(x, (28, 28)).astype(np.float32) for x in thr])
    return resize
