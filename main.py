from distutils.log import error
import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import desired_capabilities
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from pywinauto import keyboard
import multiprocessing as mp
from tkinter import *
from tkinter import Frame as Frametk
from tkinter import Button as ButtonTK 
import threading
import pywinauto
from pywinauto import Application
class addchrome:
    def __init__(self) -> None:
        self.listgmail = ''
        self.profile = ''
    def GUI(self):
        self.window = Tk()

        self.window.title("AUTO add chrome")

        self.window.geometry('1000x600')

        self.window.grid_rowconfigure(0, minsize=20, weight=1)

        lbl = Label(self.window, text="DESIGN BY DEVELOPER TÀI NGUYỄN", font=("Arial Bold", 20), width=55, pady=10, bg="black" , fg="white",borderwidth=2, relief="raised")

        lh = Label(self.window, text="NHẬN CODE TOOL & THIẾT KẾ WEBSITE THEO YÊU CẦU - ZALO/SDT 0387865006", font=("Arial Bold", 12), width=93,pady=1 , fg="red",borderwidth=2, relief="raised")

        lbl.pack(fill=X)

        lh.pack(fill=X)

        fame1 = Frametk(self.window)

        fame1.pack(side=TOP,fill=X,pady=20,padx=20)

        lbl1 = Label(fame1, text= 'list gmail :', font=("Time New Roman", 14))

        lbl1.grid(column=0,row=0,padx=5,pady=5,sticky='w')      

        self.lgmail = Text(fame1) 

        self.lgmail.grid(column=0,row=1,padx=5,pady=5,sticky='w') 

        lbl1 = Label(fame1, text= 'list profile :', font=("Time New Roman", 14))

        lbl1.grid(column=1,row=0,padx=5,pady=5,sticky='w') 

        self.lprofile = Text(fame1) 

        self.lprofile.grid(column=1,row=1,padx=5,pady=5,sticky='w') 

        def STARTM():
            self.listgmail =  self.lgmail.get('1.0','end').splitlines()
            self.profile = self.lprofile.get('1.0','end').splitlines()
            threadmain = threading.Thread(target=self.main,args=())
            threadmain.start()

        Button(fame1,command=STARTM,cursor='hand2',text=" START ").grid(column=0,row=2,padx=5,pady=5,sticky='w')
        
        self.window.mainloop()
    def main(self):
        def titletext(name,start):
                    self.lgmail.tag_add(name,start + '.0',start + '.end')
                    self.lgmail.tag_add(name + 'nor',str(int(start) + 1) + '.0',str(int(start) + 1) + '.end')
                    self.lgmail.tag_config(name,foreground='red')
                    self.lgmail.tag_config(name + 'nor',foreground='black')
                    self.lprofile.tag_add(name,start + '.0',start + '.end')
                    self.lprofile.tag_add(name + 'nor',str(int(start) + 1) + '.0',str(int(start) + 1) + '.end')
                    self.lprofile.tag_config(name,foreground='red')
                    self.lprofile.tag_config(name + 'nor',foreground='black')
        if platform == "linux" or platform == "linux2":
            chrome_driver_path = "./chromedriver"
        elif platform == "darwin":
            chrome_driver_path = "./mac/chromedriver"
        elif platform == "win32":
            chrome_driver_path = "chromedriver.exe"

            # capa = desired_capabilities.DesiredCapabilities.CHROME
            # capa["pageLoadStrategy"] = "none"
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument(r"--user-data-dir=C://Users//Admin//AppData//Local//Google//Chrome//User Data//") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
            # chrome_options.add_argument(r'--profile-directory=Profile 11') #e.g. Profile 3
            # unpacked_extension_path = 'Extensions/1.5_0.crx'
            # unpacked_extension_path2 = 'Extensions/1.7.2_0.crx'
            # chrome_options.add_extension(getPlugin('','','',''))
            # chrome_options.add_extension(unpacked_extension_path)
            # chrome_options.add_extension(unpacked_extension_path2)
            # # chrome_options.add_experimental_option("debuggerAddress", '127.0.0.1:9222')
            # driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options,desired_capabilities=capa)
            # action = ActionChains(driver)
            # driver.get('chrome://extensions/')
            # time.sleep(3)
            # action.move_by_offset(102, 80).click().perform()
            # time.sleep(3)
            # driver.save_screenshot("screenshot.png")
            # time.sleep(100)
            # driver.quit()
        for a in range(0,len(self.listgmail)):
            time.sleep(3)
            titletext('bold' + str(a),str(a + 1))
            self.window.update()
            chrome_options2 = uc.ChromeOptions()
            chrome_options2.add_argument("--user-data-dir=C://Users//Administrator//AppData//Local//Google//Chrome//User Data//") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
            chrome_options2.add_argument('--profile-directory=Profile ' + self.profile[a]) #e.g. Profile 3
            chrome_options2.add_argument('--lang=vie')
            driver = uc.Chrome(options=chrome_options2)
            action = ActionChains(driver)
            driver.maximize_window()
            driver.get('https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm/related?fbclid=IwAR02eBi4f1fFgWzYghfglCe8wsE7-004C_0piRrVg3wJH8Mv0caMzKxAkxA')
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//span[text()="Tôi đồng ý"]').click()
                time.sleep(5)
            except:
                pass
            try:
                driver.find_elements_by_xpath('//div[text()="Thêm vào Chrome"]')[0].click()
            except:
                driver.find_elements_by_xpath('//div[text()="Add to Chrome"]')[0].click()
            time.sleep(5)
            window = pywinauto.findwindows.find_elements(title='Auto Refresh Plus | Page Monitor - Cửa hàng Chrome trực tuyến - Google Chrome')
            app = Application(backend="uia").connect(handle = window[0].handle)
            win = app.window(handle = window[0].handle)
            app2 = Application(backend="win32").connect(handle = window[0].handle)
            win2 = app2.window(handle = window[0].handle)
            # print(window)
            # win.dump_tree()
            win.child_window(title="Thêm tiện ích", control_type="Button").click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            driver.get('https://accounts.google.com/')
            # driver.save_screenshot("screenshot.png")
            # action.move_by_offset(1209, 278).click().perform()
            time.sleep(4)
            # driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath("//input[@type='email']").send_keys(self.listgmail[a].split('\t')[0])
            driver.find_element_by_xpath("//span[text()='Tiếp theo']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//input[@type='password']").send_keys(self.listgmail[a].split('\t')[1])
            driver.find_element_by_xpath("//span[text()='Tiếp theo']").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath('//div[text()="Xác nhận email khôi phục của bạn"]').click()
                time.sleep(3)
                driver.find_element_by_xpath('//input[@type="email"]').send_keys(self.listgmail[a].split('\t')[2])
                time.sleep(3)
                driver.find_element_by_xpath("//span[text()='Tiếp theo']").click()
                time.sleep(5)
            except:
                pass
            driver.get('https://www.youtube.com/watch?v=rQtL4tLYGEk')
            time.sleep(5)
            action.move_by_offset(1090, 775).perform()
            driver.find_element_by_xpath('//button[@data-tooltip-target-id="ytp-autonav-toggle-button"]').click()
            time.sleep(1)
            action.move_by_offset(110, 0).click().perform()
            time.sleep(1)
            action.move_by_offset(90, -65).click().perform()
            time.sleep(1)
            action.move_by_offset(-125, -40).click().perform()
            time.sleep(3)
            win2.click(coords=(1864, 53))
            time.sleep(3)
            for a in range(5):
                keyboard.send_keys('{RIGHT}')
                time.sleep(1)
            keyboard.send_keys('{ENTER}')
            time.sleep(3)
            windowf = pywinauto.findwindows.find_elements(title='')
            for a in windowf:
                if a.class_name == 'Chrome_WidgetWin_1':
                    appf = Application(backend="win32").connect(handle=a.handle)
                    winf = appf.window(handle=a.handle)
                    winf.click(coords=(370, 455))
            time.sleep(3)
            driver.quit()
if __name__ == '__main__':
    mp.freeze_support()
    addchrome().GUI()

