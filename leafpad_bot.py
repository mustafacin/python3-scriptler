import threading
import pyautogui
import os ,time


def calis():
        os.system("leafpad")



def worker():
        time.sleep(1)
        pyautogui.write('Merhabalar arkadaslar, Bu bir test yazisidir.Adli bilisim Muhendisligi 3. sinif ogrencisi tarafindan yazilmaktadir.', interval=0.05)

#interval kisimini artirarak yazma hizini yavaslatabilirsiniz.

w = threading.Thread(target = calis)
t = threading.Thread(target = worker)

w.start()
t.start()
