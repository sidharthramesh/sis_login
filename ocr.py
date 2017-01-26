import preprocess
import cv2
import pytesseract
import PIL

def write_preprocess(image_path,result='temp.jpeg'):
    """thresholds and writes that image to disk"""
    thr=preprocess.threshold(image_path)
    cv2.imwrite(result,thr)
    return PIL.Image.open(result)
def tess(pil_image_file):
    file=pil_image_file
    return pytesseract.image_to_string(file)
def refine(string):
    stlist=[]
    for letter in string:
        letter=letter.upper()
        if letter.isalnum():
            stlist.append(letter)
    return ''.join(stlist)
def verify(string):
    if len(string)==5:
        return True
    else:
        return False

def ocr(image_path):
    pil_file=write_preprocess(image_path)
    ocr_string=tess(pil_file)
    ocr_string=refine(ocr_string)
    if verify(ocr_string)==False:
        raise Exception('Not 5 letters')
    else:
        return ocr_string
