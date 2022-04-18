
from selenium import webdriver
import threading
import time
class openprofile:
    def __init__(self) -> None:
        print("Tool design by Tai Nguyen - Code tool theo y/c zalo 0387865006")
        with open('data/listprofile.txt') as file2:
            self.profile = file2.read().splitlines()
    def too(self):
        def main(a):
            try:
                chrome_options2 = webdriver.ChromeOptions()
                chrome_options2.add_argument("--user-data-dir=C://Users//Administrator//AppData//Local//Google//Chrome//User Data//") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
                chrome_options2.add_argument('--profile-directory=Profile ' + str(a)) #e.g. Profile 3
                chrome_options2.add_extension('Extensions/1.5_0.crx')
                driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options2)
                while True:
                    pass
            except:
                while 1==1:
                    pass
        for a in self.profile:
            threading.Thread(target=main,args=(a,)).start()
            time.sleep(1)

openprofile().too()