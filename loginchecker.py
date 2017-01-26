import robobrowser
import requests
import shutil
from PIL import Image
def open_page():
    """Opens up the sis page and returns browser object"""
    br = robobrowser.RoboBrowser()
    br.open('https://sis.manipal.edu/studlogin.aspx')
    return br
def login(uname = '150101312',passw = '08/09/1997'):
    """Attempts login"""
    print("[+] Opening Page...")
    br = open_page()
    form = br.get_forms()[0] #Supress warning
    images = br.find_all('img')
    cap =images[2]['src']
    url = 'https://sis.manipal.edu/'
    cap_url = url + cap
    print("[+] Fetching Captcha")
    write_file(cap_url,'captcha.jpg')
    captcha_ans = manual_captcha()
    #captcha_ans = ocr('captcha.jpg')
    form['txtroll'] = uname
    form['txtdob'] = passw
    form['txtCaptcha'] = captcha_ans
    form.serialize()
    print("[+] Attempting login")
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
        print("[-]")
    else:
        print("[+] Recorded login!")
        for i in value:
            print(i)

#if __name__=='__main__':
#    main()
