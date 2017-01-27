import threading
from pandas import date_range
import time
def gen(daterange = [1997,1998], rollrange = [150101001,150101600]):
    [dstart,dstop] = daterange
    [rstart,rstop] = rollrange
    dates = date_range(str(dstart),str(dstop))
    dates = list(dates.strftime("%d/%m/%Y"))
    roll_nos = [str(roll) for roll in range(rstart,rstop)]
    return (dates,roll_nos)

class thread(threading.Thread):
    def __init__(self,rollno,dob):
        threading.Thread.__init__(self)
        self.rollno = rollno
        self.dob = dob
    def run(self):
        print("[+] Starting thread "+"{} {}".format(self.rollno,self.dob))
        #login(self.rollno,self.dob)
        print("Login mock...")
        time.sleep(5)
        print("[-] Exiting thread  "+"{} {}".format(self.rollno,self.dob))

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

dates, rolls = gen()

date_chunks = list(chunks(dates,10))

for roll in rolls:
    for i,date_chunk in enumerate(date_chunks):
        main_thread = i+1
        main_q = []
        for date in date_chunk:
            t = thread(roll,date)
            t.start()
            main_q.append(t)
        for q in main_q:
            q.join()   
