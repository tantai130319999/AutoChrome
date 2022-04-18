# import autoit
# import time
# print("Tool design by Tai Nguyen - Code tool theo y/c zalo 0387865006 \n")
# print('Path to HMA VPN.exe')
# path = input()
# print("Time to auto (minute)")
# timeout = float(input()) * 60
# print("Do you want Turn on HMA now ? (yes/no)")
# yesno = input()
# if yesno == 'yes':
#     autoit.run(path,work_dir="",show_flag=5)
#     time.sleep(5)
#     autoit.control_click("[CLASS:AvastCefWindow]", "Chrome_RenderWidgetHostHWND1",x=380,y=288)
#     time.sleep(10)
#     autoit.win_close("[CLASS:AvastCefWindow]")
# while True:
#     time.sleep(timeout)
#     autoit.run(path,work_dir="",show_flag=5)
#     time.sleep(5)
#     autoit.control_click("[CLASS:AvastCefWindow]", "Chrome_RenderWidgetHostHWND1",x=380,y=288)
#     time.sleep(4)
#     autoit.control_click("[CLASS:AvastCefWindow]", "Chrome_RenderWidgetHostHWND1",x=380,y=288)
#     time.sleep(10)
#     autoit.win_close("[CLASS:AvastCefWindow]")


from ctypes.wintypes import HANDLE
from turtle import title
import pywinauto
from pywinauto import Desktop,Application
from pywinauto import keyboard , mouse
from tkinter import *
import time
import threading
import ctypes
import autoit
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import desired_capabilities
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import multiprocessing as mp
def gui():
        window = Tk()

        window.title("AUTO HMA")

        window.geometry('750x300')

        lbl = Label(window, text="DESIGN BY DEVELOPER TÀI NGUYỄN", font=("Arial Bold", 20), width=55, pady=10, bg="black" , fg="white",borderwidth=2, relief="raised")

        lh = Label(window, text="NHẬN CODE TOOL & THIẾT KẾ WEBSITE THEO YÊU CẦU - ZALO/SDT 0387865006", font=("Arial Bold", 12), width=93,pady=1 , fg="red",borderwidth=2, relief="raised")

        lbl.pack(fill=X)

        lh.pack(fill=X)  

        fame = Frame(window)

        fame.pack(fill=X,pady=15,padx=10)

        lbl1 = Label(fame, text= 'HMA FOLDER :', font=("Arial", 11))  
        lbl1.grid(column=0,row=0,padx=5,pady=5)
        path = Entry(fame,width=50)
        path.grid(column=1,row=0,padx=15,pady=5,sticky='w')

        lbl1 = Label(fame, text= 'Time click (s) :', font=("Arial", 11))  
        lbl1.grid(column=0,row=1,padx=5,pady=5)
        timeclick = Spinbox(fame,from_=1, to=999)
        timeclick.grid(column=1,row=1,padx=15,pady=5,sticky='w')

        lbl1 = Label(fame, text= 'Time to loop auto (minute) :', font=("Arial", 11))  
        lbl1.grid(column=0,row=2,padx=5,pady=5)
        timeloop = Spinbox(fame,from_=1, to=999)
        timeloop.grid(column=1,row=2,padx=15,pady=5,sticky='w')
        threads = []
        def start():
            runmain = threading.Thread(target=test,args=(path.get(),)) # ,timeclick.get(),timeloop.get()
            threads.append(runmain)
            runmain.start()
        def stop():
            for t in threads:
                thread_id = t.native_id
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                    ctypes.py_object(SystemExit))
                if res > 1:
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)

        Button(fame,text='START',command=start).grid(column=0,row=20,padx=10,pady=10)
        Button(fame,text='STOP',command=stop).grid(column=1,row=20,padx=10,pady=10)

        window.mainloop()
def main(path,timeclick,timeloop):
    while True:
        time.sleep(int(timeloop)*60)
        vpn_app = Application(backend="uia").start(path)
        dialog=Desktop(backend="uia").HMA
        panel0=dialog.Pane
        # Command to connect / disconnect the VPN: connect_button.click()
        connect_button=panel0.ConnectButton
        # Command to change the IP address: changeIP.click()
        changeIP=panel0.Button5
        # Check VPN state:
        # 0 if disconnected
        # 1 if connected

        # Command to connect / disconnect the VPN: connect_button.click()
        connect_button=panel0.ConnectButton
        connect_button.click()

        # Command to change the IP address: changeIP.click()
        changeIP=panel0.Button5
        changeIP.click()
        time.sleep(int(timeclick))
        # Check VPN state:
        # 0 if disconnected
        # 1 if connected
def mainit():
    # time.sleep(5)
    window = pywinauto.findwindows.find_elements(title='Thẻ mới - Google Chrome')
    app = Application(backend="uia").connect(handle = window[0].handle)
    win = app.window(handle = window[0].handle)
    print(window)
    
    win.child_window(title="Tiện ích", control_type="MenuItem").invoke()
    time.sleep(3)
    window = pywinauto.findwindows.find_elements(title='Thẻ mới - Google Chrome')
    app = Application(backend="uia").connect(handle = window[0].handle)
    win = app.window(handle = window[0].handle)
    win.dump_tree()
    app = Application(backend="win32").connect(handle = window[0].handle)
    win = app.window(handle = window[0].handle)
    for a in range(5):
        keyboard.send_keys('{RIGHT}')
        time.sleep(5)
    keyboard.send_keys('{ENTER}')
    # win.child_window(title="Auto Refresh Plus", control_type="MenuItem").invoke()
def test():

        # try:
        #     window = pywinauto.findwindows.find_elements(title='HMA VPN')

        #     app = Application(backend="uia").connect(handle = window[0].handle)
        #     win = app.window(handle = window[0].handle)
        #     win.set_focus()
        #     win.dump_tree()
        #     win.child_window(title="Connect", auto_id="dashboard_switch", control_type="Button").click()
        #     win.child_window(title="Change IP Address", auto_id="ip_change", control_type="Button").click()
        #     time.sleep(10)
        #     win.child_window(title="Disconnect", auto_id="dashboard_switch", control_type="Button").click()
        #     win.child_window(title="Change IP Address", auto_id="ip_change", control_type="Button").click()
        # except:

            window = pywinauto.findwindows.find_elements(title='MetaMask Notification')
            app = Application(backend="win32").connect(handle =window[0].handle)
            win = app.window(handle =window[0].handle)
            win.dump_tree()
            time.sleep(3)
            for a in range(5):
                keyboard.send_keys('{RIGHT}')
                time.sleep(1)
            keyboard.send_keys('{ENTER}')
            time.sleep(3)
            window = pywinauto.findwindows.find_elements(title='')
            for a in window:
                if a.class_name == 'Chrome_WidgetWin_1':
                    app = Application(backend="win32").connect(handle=a.handle)
                    win = app.window(handle=a.handle)
                    win.click(coords=(370, 455))

    # win.child_window(title="Tiện ích", control_type="MenuItem").invoke()
    # time.sleep(3)
    # window = pywinauto.findwindows.find_elements(title='Thẻ mới - Google Chrome')
    # for a  in window:
    #     if a.class_name == 'Chrome_WidgetWin_1':
    #         app = Application(backend="win32").connect(handle=a.handle)
    #         win = app.window(handle=a.handle)
    # win.dump_tree()
    # win.click(coords=(1783, 176))
    # win.click(coords=(110, 263))
    # win.click(coords=(110, 263))
    # win.click(coords=(219, 261))
    # win.click(coords=(219, 261))
    # autoit.win_activate_by_handle(0x00050910)
    # autoit.control_click_by_handle(0x00050910,0x00040906,x=394,y=281)
    # autoit.control_click("[CLASS:Chrome_WidgetWin_1]", 0x000D0766,x=53,y=327)
def test_chrome(chr):
    chrome_options2 = webdriver.ChromeOptions()
    chrome_options2.add_argument("--user-data-dir=C://Users//Admin//AppData//Local//Google//Chrome//User Data//") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
    chrome_options2.add_argument('--profile-directory=Profile ' + str(chr)) #e.g. Profile 3
    chrome_options2.add_argument('--lang=vie')
    chrome_options2.add_argument('--remote-debugging-port=92' + str(chr))
    driver = webdriver.Chrome(options=chrome_options2)
    time.sleep(300)
def test_remote(chr):
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_experimental_option("debuggerAddress", 'localhost:92'  + str(chr))
    driver2 = webdriver.Chrome(options=chrome_options)
    driver2.get('https://www.popop.world/GameSelect/adventure?fbclid=IwAR3N4ZDR3fJ75nID4LTEjqD2SWNcnOlCrJET-f8kwtIHET8oOpbnEXuKN14')
    print("Da mo")
# if __name__ == '__main__':
#     mp.freeze_support()
    # for a in range(10,20):
    #     threading.Thread(target=test_chrome,args=(a,)).start()
    #     time.sleep(3)
    #     threading.Thread(target=test_remote,args=(a,)).start()

    # threading.Thread(target=test_remote,args=(22,)).start()
        
# mainit('"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 12"','1','1')
test()