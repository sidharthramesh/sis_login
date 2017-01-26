import requests
import numpy as np
import cv2
from bs4 import BeautifulSoup
from skimage import io
def get_cap_url():
    """returns captcha url"""
    sis='https://sis.manipal.edu/'
    page=requests.get('https://sis.manipal.edu/studlogin.aspx')
    pagetext=page.text
    soup=BeautifulSoup(pagetext,"lxml")
    cap=soup.findAll('img')[2]
    cap=cap['src']
    url=sis+cap
    return url
def get_captcha(url):
    """Returns array of the captcha image"""
    img=io.imread(url)
    return img
