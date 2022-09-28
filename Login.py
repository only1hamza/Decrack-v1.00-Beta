from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
#from fun import *
import time
from tkinter import filedialog as fd
from tkinter import messagebox
import pickle
import os.path
from PIL import ImageTk, Image  
import requests
from bs4 import BeautifulSoup
#from UserVerification import *


window = Tk()
window.title("Login")
window.geometry("400x180")
window.iconbitmap("DekCrack.ico")
window.resizable(False, False)
window.attributes("-topmost", True)


lblsrv = ttk.Label(window, text = 'Server')
lblsrv.place(x=10, y=30)
lbllog = ttk.Label(window, text = 'User')
lbllog.place(x=10, y=60)
lblkey = ttk.Label(window, text = 'Keypass')
lblkey.place(x=10, y=90)

entsrv = ttk.Entry(window, width = 25)
entsrv.place(x=70, y=30)
entlog = ttk.Entry(window, width = 25)
entlog.place(x=70, y=60)
entkey = ttk.Entry(window, width = 25)
entkey.place(x=70, y=90)


lblinf = ttk.Label(window, text = '', foreground ='black', width=30, anchor=CENTER)
#lblinf.config(anchor=CENTER)
lblinf.place(x=50, y=120)



bar1 = tk.Frame(window, bg="#007e41", height=50, width=700)
bar1.place(x=-2 ,y=160)   
txtbar1 = tk.Label(window, text="DekCrack v1.01 - GiegLan Tool", foreground ="white", bg="#007e41", font=("Time New Roman",9))
txtbar1.place(x=113,y=160) 
txtbar1.configure(anchor="center")

canvas = Canvas(window, width = 140, height = 100)      
canvas.place(x=260, y=18)
img = PhotoImage(file="ressources/icons/dekcrack.png")      
canvas.create_image(0, 0, anchor=NW, image=img ) 


btnst = ttk.Button(window, text = 'Connecte', command=lambda:[Click()])
btnst.place(x=270, y=120)
#btnst.bind('<Enter>',lambda event: Click())

#date_login = s[4]
#activation_login = s[5]

Dsrv= "http://147.182.233.221/"
entsrv.insert(0,Dsrv)


def is_cnx_active(timeout):
    try:
        requests.head("http://www.google.com", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False



def Click(): 
    if is_cnx_active(5) is True:
        print("The internet connection is active")
        #break
        r2=requests.get(entsrv.get(), timeout=2)
        print(r2)
        soup = BeautifulSoup(r2.text, 'html.parser')
        b = soup.find('p').get_text()
        s = list(b.split("\n"))
        f = entlog.get() in s
        print(f)
        if f == True :
            i = s.index(entlog.get())
            id_login = s[i-1]
            user_login = s[i]
            key_login = s[i+1]
            date_login = s[i+2]
            activation_login = s[i+3]
            print(s)
            log1 = entlog.get()
            key1 = entkey.get()
            
            r1=requests.get('https://www.calendardate.com/todays.html')
            soup = BeautifulSoup(r1.text, 'html.parser')
            a = soup.find_all(id='tprg')[6].get_text()
            a = a.replace('-','')
            a = a.replace(' ','')
            if log1 == user_login and key1 == key_login :
                if date_login >= a :
                    lblinf["text"]="Connection Succesfuly .. Please Wait"
                    if activation_login == "YES":
                        lblinf["text"]="Your User is Activated .. Please Wait"
                        #time.sleep(2)
                        lblinf["text"]=f"Connected, Your ID is {id_login}\n working till {date_login[0:4]}-{date_login[4:6]}-{date_login[6:8]}"
                        lblinf["foreground"]="#007e41"
                    else: 
                        lblinf["text"]="Your User has Disactivated"
                        lblinf["foreground"]="red"
                else :
                    lblinf["text"]="Your User has Expered"
                    lblinf["foreground"]="red"
            else :
                lblinf["text"]="Login is Faild, Try Again"
                lblinf["foreground"]="red"
        else :
            lblinf["text"]="Login is Faild, Try Again"
            lblinf["foreground"]="red"
    else:
        lblinf["text"]="No Internet Connection"
        lblinf["foreground"]="red"
    #print(log1, key1)
    #time.sleep(3)

window.mainloop()













