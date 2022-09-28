from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
from fun import *
import time
from tkinter import filedialog as fd
from tkinter import messagebox
import pickle
import os.path
from PIL import ImageTk, Image  
import requests


window = tk.Tk()
#MyWin = Window(window)
window.title("DekCrack")
window.geometry("690x650+10+10")
window.iconbitmap("DekCrack.ico")
# window.resizable(False, False)



notebook=ttk.Notebook(window)

frame0 = ttk.Frame(notebook)
frame0.place()
frame1 = ttk.Frame(notebook)
frame1.place()
frame2 = ttk.Frame(notebook)
frame2.pack()
frame3 = ttk.Frame(notebook)
frame3.pack()
frame4 = ttk.Frame(notebook)
frame4.pack()
frame5 = ttk.Frame(notebook)
frame5.pack()
frame6 = ttk.Frame(notebook)
frame6.pack()
frame7 = ttk.Frame(notebook)
frame7.pack()


notebook.add(frame0, text="GiegLan")
notebook.add(frame1, text="Susspension")
notebook.add(frame2, text="Rippage")
notebook.add(frame3, text="Frienment")
notebook.add(frame4, text="Gaz")
notebook.add(frame5, text="Diesel")
notebook.add(frame6, text="Reglophore")
notebook.add(frame7, text="About")

notebook.pack()

menubar = Menu(window, foreground='black', activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=1, foreground='black')  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as")    
file.add_separator()  
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

Registration = Menu(menubar, tearoff=0)  
Registration.add_command(label="Login",)  
Registration.add_command(label="Registration",)
Registration.add_command(label="Refresh Connection", command=lambda:[checkInternetConnection(lblinfinternet)])
Registration.add_separator()     
Registration.add_command(label="You Have 30 Day trail",)
menubar.add_cascade(label="Registration", menu=Registration)

help = Menu(menubar, tearoff=0)  
help.add_command(label="About",)  
menubar.add_cascade(label="Help", menu=help)  
    
window.config(menu=menubar)

class douaa:
    def __init__(self, master, frameX):
        
        # Frames
        
        dir=400
        
        frameer1 = ttk.Frame(frameX, width=690, height=630)
        frameer1.grid(row=0, column=0)
       
        lf1 = ttk.LabelFrame(frameX, text = 'Actions', height=135, width=90, labelanchor="n")
        lf1.place(x=dir-7,y=80)

        lf2 = ttk.LabelFrame(frameX, text = 'CRC', height=565, width=140, labelanchor="n")
        lf2.place(x=243,y=10)

        lfmsr = ttk.LabelFrame(frameX, text = 'Mesures', height=565, width=140, labelanchor="n")
        lfmsr.place(x=96,y=10) 

        lf3 = ttk.LabelFrame(frameX, text = 'Ser.', height=565, width=70, labelanchor="n")
        lf3.place(x=20,y=10) 

        lf4 = ttk.LabelFrame(frameX, text = 'File Type', height=60, width=270, labelanchor="n")
        lf4.place(x=dir-7,y=10)

        lfpgr = ttk.LabelFrame(frameX, text = 'Progress', height=60, width=270, labelanchor="nw")
        lfpgr.place(x=dir-7,y=225)

        lf5 = ttk.LabelFrame(frameX, text = 'Statu', height=135, width=170, labelanchor="n")
        lf5.place(x=dir-7+100,y=80)

        lf6 = ttk.LabelFrame(frameX, text = 'Outils', height=120, width=270, labelanchor="nw")
        lf6.place(x=dir-7,y=295)

        lf7 = ttk.LabelFrame(frameX, text = 'Info', height=150, width=270, labelanchor="nw")
        lf7.place(x=dir-7,y=425)
        
        # Progressbar
        pb =ttk.Progressbar(frameX, orient=HORIZONTAL, length=250, mode='determinate')
        pb.place(x=403,y=248)
        
        txt1 = ttk.Label(frameX, text = '0%')
        txt1.place(x=575 ,y=160+22)
        txt1.configure(anchor="center")
 

        btn1=ttk.Button(frameX, text="Calculate", command=lambda:[step(pb,txt1), Valeus(),""" Fav(
        v3,
        v4,
        v5,
        v6,
        v7,
        v8,
        fav,
        cfav,
        txtfav
        ), Good()"""])
        btn1.place(x=dir, y=115-20)


 
# Variables

for i in range(1,85):
    RangV=f"v{i} = ''"
    exec(RangV)
    RangS=f"s{i} = ''"
    exec(RangS)


fav = ""
cfav = ""
txtfav = ""



frameer1 = ttk.Frame(frame1, width=690, height=630)
frameer1.grid(row=0, column=0)

callinit = douaa(window, frame1)
callinit = douaa(window, frame2)
callinit = douaa(window, frame3)
callinit = douaa(window, frame4)
callinit = douaa(window, frame5)
callinit = douaa(window, frame6)


# Ser.
divl=35
divl1=32


# SUSPOSION      
dinx=103
diny=30
dinm=30

disx=250
disy=30


ent1=ttk.Entry(frame1, text="2", textvariable=v1)
ent1.place(x=dinx, y=diny)
ent2=ttk.Entry(frame1, text="2", textvariable=v2)
ent2.place(x=dinx, y=diny+dinm)
ent3=ttk.Entry(frame1, text="2", textvariable=v3)
ent3.place(x=dinx, y=diny+dinm*2)
ent4=ttk.Entry(frame1, text="2", textvariable=v4)
ent4.place(x=dinx, y=diny+dinm*3)
ent5=ttk.Entry(frame1, text="2", textvariable=v5)
ent5.place(x=dinx, y=diny+dinm*4)
ent6=ttk.Entry(frame1, text="2", textvariable=v6)
ent6.place(x=dinx, y=diny+dinm*5)
ent7=ttk.Entry(frame1, text="2", textvariable=v7)
ent7.place(x=dinx, y=diny+dinm*6)
ent8=ttk.Entry(frame1, text="2", textvariable=v8)
ent8.place(x=dinx, y=diny+dinm*7)
ent9=ttk.Entry(frame1, text="2", textvariable=v9)
ent9.place(x=dinx, y=diny+dinm*8)

sort1=ttk.Entry(frame1, text="2", textvariable=s1)
sort1.place(x=disx, y=diny)
sort2=ttk.Entry(frame1, text="2", textvariable=s2)
sort2.place(x=disx, y=diny+dinm)
sort3=ttk.Entry(frame1, text="2", textvariable=s3)
sort3.place(x=disx, y=diny+dinm*2)
sort4=ttk.Entry(frame1, text="2", textvariable=s4)
sort4.place(x=disx, y=diny+dinm*3)
sort5=ttk.Entry(frame1, text="2", textvariable=s5)
sort5.place(x=disx, y=diny+dinm*4)
sort6=ttk.Entry(frame1, text="2", textvariable=s6)
sort6.place(x=disx, y=diny+dinm*5)
sort7=ttk.Entry(frame1, text="2", textvariable=s7)
sort7.place(x=disx, y=diny+dinm*6)
sort8=ttk.Entry(frame1, text="2", textvariable=s8)
sort8.place(x=disx, y=diny+dinm*7)
sort9=ttk.Entry(frame1, text="2", textvariable=s9)
sort9.place(x=disx, y=diny+dinm*8)

l1 = ttk.Label(frame1, text = '0200 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(frame1, text = '0320 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(frame1, text = '0410 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(frame1, text = '0411 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(frame1, text = '0412 =')
l5.place(x=divl,y=divl1+30*4)
l6 = ttk.Label(frame1, text = '0413 =')
l6.place(x=divl,y=divl1+30*5)
l7 = ttk.Label(frame1, text = '0414 =')
l7.place(x=divl,y=divl1+30*6)
l8 = ttk.Label(frame1, text = '0415 =')
l8.place(x=divl,y=divl1+30*7)
l9 = ttk.Label(frame1, text = '0416 =')
l9.place(x=divl,y=divl1+30*8)


# RIPPAGE

ent10=ttk.Entry(frame2, text="2", textvariable=v10)
ent10.place(x=dinx, y=diny)
ent11=ttk.Entry(frame2, text="2", textvariable=v11)
ent11.place(x=dinx, y=diny+dinm)
ent12=ttk.Entry(frame2, text="2", textvariable=v12)
ent12.place(x=dinx, y=diny+dinm*2)
ent13=ttk.Entry(frame2, text="2", textvariable=v13)
ent13.place(x=dinx, y=diny+dinm*3)
ent14=ttk.Entry(frame2, text="2", textvariable=v14)
ent14.place(x=dinx, y=diny+dinm*4)

sort10=ttk.Entry(frame2, text="2", textvariable=s10)
sort10.place(x=disx, y=diny)
sort11=ttk.Entry(frame2, text="2", textvariable=s11)
sort11.place(x=disx, y=diny+dinm)
sort12=ttk.Entry(frame2, text="2", textvariable=s12)
sort12.place(x=disx, y=diny+dinm*2)
sort13=ttk.Entry(frame2, text="2", textvariable=s13)
sort13.place(x=disx, y=diny+dinm*3)
sort14=ttk.Entry(frame2, text="2", textvariable=s14)
sort14.place(x=disx, y=diny+dinm*4)

l1 = ttk.Label(frame2, text = '0200 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(frame2, text = '0320 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(frame2, text = '0401 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(frame2, text = '0402 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(frame2, text = '0403 =')
l5.place(x=divl,y=divl1+30*4)

# FRIENMENT Scroll
main_frame = Frame(frame3, height = 700 , width = 650)
main_frame.place(x=0,y=0)

my_canvas = Canvas(main_frame, height =580, width = 375)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))


second_frame = Frame(my_canvas, height = 1200, width = 400)
second_frame.grid(row=0,column=0)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

lf2 = ttk.LabelFrame(second_frame, text = 'CRC', height=1160, width=140, labelanchor="n")
lf2.place(x=243,y=10)

lfmsr = ttk.LabelFrame(second_frame, text = 'Mesures', height=1160, width=140, labelanchor="n")
lfmsr.place(x=96,y=10) 

lf3 = ttk.LabelFrame(second_frame, text = 'Ser.', height=1160, width=70, labelanchor="n")
lf3.place(x=20,y=10) 

# FRIENMENT

ent15=ttk.Entry(second_frame, text="2", textvariable=v1)
ent15.place(x=dinx, y=diny)
ent16=ttk.Entry(second_frame, text="2", textvariable=v2)
ent16.place(x=dinx, y=diny+dinm)
ent17=ttk.Entry(second_frame, text="2", textvariable=v3)
ent17.place(x=dinx, y=diny+dinm*2)
ent18=ttk.Entry(second_frame, text="2", textvariable=v4)
ent18.place(x=dinx, y=diny+dinm*3)
ent19=ttk.Entry(second_frame, text="2", textvariable=v5)
ent19.place(x=dinx, y=diny+dinm*4)
ent20=ttk.Entry(second_frame, text="2", textvariable=v6)
ent20.place(x=dinx, y=diny+dinm*5)
ent21=ttk.Entry(second_frame, text="2", textvariable=v7)
ent21.place(x=dinx, y=diny+dinm*6)
ent22=ttk.Entry(second_frame, text="2", textvariable=v8)
ent22.place(x=dinx, y=diny+dinm*7)
ent23=ttk.Entry(second_frame, text="2", textvariable=v9)
ent23.place(x=dinx, y=diny+dinm*8)
ent24=ttk.Entry(second_frame, text="2", textvariable=v10)
ent24.place(x=dinx, y=diny+dinm*9)
ent25=ttk.Entry(second_frame, text="2", textvariable=v11)
ent25.place(x=dinx, y=diny+dinm*10)
ent26=ttk.Entry(second_frame, text="2", textvariable=v12)
ent26.place(x=dinx, y=diny+dinm*11)
ent27=ttk.Entry(second_frame, text="2", textvariable=v13)
ent27.place(x=dinx, y=diny+dinm*12)
ent28=ttk.Entry(second_frame, text="2", textvariable=v14)
ent28.place(x=dinx, y=diny+dinm*13)
ent29=ttk.Entry(second_frame, text="2", textvariable=v15)
ent29.place(x=dinx, y=diny+dinm*14)
ent30=ttk.Entry(second_frame, text="2", textvariable=v16)
ent30.place(x=dinx, y=diny+dinm*15)
ent31=ttk.Entry(second_frame, text="2", textvariable=v17)
ent31.place(x=dinx, y=diny+dinm*16)
ent32=ttk.Entry(second_frame, text="2", textvariable=v18)
ent32.place(x=dinx, y=diny+dinm*17)
ent33=ttk.Entry(second_frame, text="2", textvariable=v19)
ent33.place(x=dinx, y=diny+dinm*18)
ent34=ttk.Entry(second_frame, text="2", textvariable=v20)
ent34.place(x=dinx, y=diny+dinm*19)
ent35=ttk.Entry(second_frame, text="2", textvariable=v21)
ent35.place(x=dinx, y=diny+dinm*20)
ent36=ttk.Entry(second_frame, text="2", textvariable=v22)
ent36.place(x=dinx, y=diny+dinm*21)
ent37=ttk.Entry(second_frame, text="2", textvariable=v23)
ent37.place(x=dinx, y=diny+dinm*22)
ent38=ttk.Entry(second_frame, text="2", textvariable=v24)
ent38.place(x=dinx, y=diny+dinm*23)
ent39=ttk.Entry(second_frame, text="2", textvariable=v25)
ent39.place(x=dinx, y=diny+dinm*24)
ent40=ttk.Entry(second_frame, text="2", textvariable=v26)
ent40.place(x=dinx, y=diny+dinm*25)
ent41=ttk.Entry(second_frame, text="2", textvariable=v27)
ent41.place(x=dinx, y=diny+dinm*26)
ent42=ttk.Entry(second_frame, text="2", textvariable=v28)
ent42.place(x=dinx, y=diny+dinm*27)
ent43=ttk.Entry(second_frame, text="2", textvariable=v29)
ent43.place(x=dinx, y=diny+dinm*28)
ent44=ttk.Entry(second_frame, text="2", textvariable=v30)
ent44.place(x=dinx, y=diny+dinm*29)
ent45=ttk.Entry(second_frame, text="2", textvariable=v31)
ent45.place(x=dinx, y=diny+dinm*30)
ent46=ttk.Entry(second_frame, text="2", textvariable=v32)
ent46.place(x=dinx, y=diny+dinm*31)
ent47=ttk.Entry(second_frame, text="2", textvariable=v33)
ent47.place(x=dinx, y=diny+dinm*32)
ent48=ttk.Entry(second_frame, text="2", textvariable=v34)
ent48.place(x=dinx, y=diny+dinm*33)
ent49=ttk.Entry(second_frame, text="2", textvariable=v35)
ent49.place(x=dinx, y=diny+dinm*34)
ent50=ttk.Entry(second_frame, text="2", textvariable=v36)
ent50.place(x=dinx, y=diny+dinm*35)
ent51=ttk.Entry(second_frame, text="2", textvariable=v37)
ent51.place(x=dinx, y=diny+dinm*36)
ent52=ttk.Entry(second_frame, text="2", textvariable=v38)
ent52.place(x=dinx, y=diny+dinm*37)

sort15=ttk.Entry(second_frame, text="2", textvariable=v1)
sort15.place(x=disx, y=diny)
sort16=ttk.Entry(second_frame, text="2", textvariable=v2)
sort16.place(x=disx, y=diny+dinm)
sort17=ttk.Entry(second_frame, text="2", textvariable=v3)
sort17.place(x=disx, y=diny+dinm*2)
sort18=ttk.Entry(second_frame, text="2", textvariable=v4)
sort18.place(x=disx, y=diny+dinm*3)
sort19=ttk.Entry(second_frame, text="2", textvariable=v5)
sort19.place(x=disx, y=diny+dinm*4)
sort20=ttk.Entry(second_frame, text="2", textvariable=v6)
sort20.place(x=disx, y=diny+dinm*5)
sort21=ttk.Entry(second_frame, text="2", textvariable=v7)
sort21.place(x=disx, y=diny+dinm*6)
sort22=ttk.Entry(second_frame, text="2", textvariable=v8)
sort22.place(x=disx, y=diny+dinm*7)
sort23=ttk.Entry(second_frame, text="2", textvariable=v9)
sort23.place(x=disx, y=diny+dinm*8)
sort24=ttk.Entry(second_frame, text="2", textvariable=v10)
sort24.place(x=disx, y=diny+dinm*9)
sort25=ttk.Entry(second_frame, text="2", textvariable=v11)
sort25.place(x=disx, y=diny+dinm*10)
sort26=ttk.Entry(second_frame, text="2", textvariable=v12)
sort26.place(x=disx, y=diny+dinm*11)
sort27=ttk.Entry(second_frame, text="2", textvariable=v13)
sort27.place(x=disx, y=diny+dinm*12)
sort28=ttk.Entry(second_frame, text="2", textvariable=v14)
sort28.place(x=disx, y=diny+dinm*13)
sort29=ttk.Entry(second_frame, text="2", textvariable=v15)
sort29.place(x=disx, y=diny+dinm*14)
sort30=ttk.Entry(second_frame, text="2", textvariable=v16)
sort30.place(x=disx, y=diny+dinm*15)
sort31=ttk.Entry(second_frame, text="2", textvariable=v17)
sort31.place(x=disx, y=diny+dinm*16)
sort32=ttk.Entry(second_frame, text="2", textvariable=v18)
sort32.place(x=disx, y=diny+dinm*17)
sort33=ttk.Entry(second_frame, text="2", textvariable=v19)
sort33.place(x=disx, y=diny+dinm*18)
sort34=ttk.Entry(second_frame, text="2", textvariable=v20)
sort34.place(x=disx, y=diny+dinm*19)
sort35=ttk.Entry(second_frame, text="2", textvariable=v21)
sort35.place(x=disx, y=diny+dinm*20)
sort36=ttk.Entry(second_frame, text="2", textvariable=v22)
sort36.place(x=disx, y=diny+dinm*21)
sort37=ttk.Entry(second_frame, text="2", textvariable=v23)
sort37.place(x=disx, y=diny+dinm*22)
sort38=ttk.Entry(second_frame, text="2", textvariable=v24)
sort38.place(x=disx, y=diny+dinm*23)
sort39=ttk.Entry(second_frame, text="2", textvariable=v25)
sort39.place(x=disx, y=diny+dinm*24)
sort40=ttk.Entry(second_frame, text="2", textvariable=v26)
sort40.place(x=disx, y=diny+dinm*25)
sort41=ttk.Entry(second_frame, text="2", textvariable=v27)
sort41.place(x=disx, y=diny+dinm*26)
sort42=ttk.Entry(second_frame, text="2", textvariable=v28)
sort42.place(x=disx, y=diny+dinm*27)
sort43=ttk.Entry(second_frame, text="2", textvariable=v29)
sort43.place(x=disx, y=diny+dinm*28)
sort44=ttk.Entry(second_frame, text="2", textvariable=v30)
sort44.place(x=disx, y=diny+dinm*29)
sort45=ttk.Entry(second_frame, text="2", textvariable=v31)
sort45.place(x=disx, y=diny+dinm*30)
sort46=ttk.Entry(second_frame, text="2", textvariable=v32)
sort46.place(x=disx, y=diny+dinm*31)
sort47=ttk.Entry(second_frame, text="2", textvariable=v33)
sort47.place(x=disx, y=diny+dinm*32)
sort48=ttk.Entry(second_frame, text="2", textvariable=v34)
sort48.place(x=disx, y=diny+dinm*33)
sort49=ttk.Entry(second_frame, text="2", textvariable=v35)
sort49.place(x=disx, y=diny+dinm*34)
sort50=ttk.Entry(second_frame, text="2", textvariable=v36)
sort50.place(x=disx, y=diny+dinm*35)
sort51=ttk.Entry(second_frame, text="2", textvariable=v37)
sort51.place(x=disx, y=diny+dinm*36)
sort52=ttk.Entry(second_frame, text="2", textvariable=v38)
sort52.place(x=disx, y=diny+dinm*37)


l1 = ttk.Label(second_frame, text = '0200 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(second_frame, text = '0320 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(second_frame, text = '0420 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(second_frame, text = '0421 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(second_frame, text = '0422 =')
l5.place(x=divl,y=divl1+30*4)
l6 = ttk.Label(second_frame, text = '0423 =')
l6.place(x=divl,y=divl1+30*5)
l7 = ttk.Label(second_frame, text = '0424 =')
l7.place(x=divl,y=divl1+30*6)
l8 = ttk.Label(second_frame, text = '0425 =')
l8.place(x=divl,y=divl1+30*7)
l9 = ttk.Label(second_frame, text = '0426 =')
l9.place(x=divl,y=divl1+30*8)
l10 = ttk.Label(second_frame, text = '0427 =')
l10.place(x=divl,y=divl1+30*9)
l11 = ttk.Label(second_frame, text = '0430 =')
l11.place(x=divl,y=divl1+30*10)
l12 = ttk.Label(second_frame, text = '0431 =')
l12.place(x=divl,y=divl1+30*11)
l13 = ttk.Label(second_frame, text = '0434 =')
l13.place(x=divl,y=divl1+30*12)
l14 = ttk.Label(second_frame, text = '0435 =')
l14.place(x=divl,y=divl1+30*13)
l15 = ttk.Label(second_frame, text = '0436 =')
l15.place(x=divl,y=divl1+30*14)
l16 = ttk.Label(second_frame, text = '0437 =')
l16.place(x=divl,y=divl1+30*15)
l17 = ttk.Label(second_frame, text = '0438 =')
l17.place(x=divl,y=divl1+30*16)
l18 = ttk.Label(second_frame, text = '0439 =')
l18.place(x=divl,y=divl1+30*17)
l19 = ttk.Label(second_frame, text = '0442 =')
l19.place(x=divl,y=divl1+30*18)
l20= ttk.Label(second_frame, text = '0443 =')
l20.place(x=divl,y=divl1+30*19)
l21= ttk.Label(second_frame, text = '0444 =')
l21.place(x=divl,y=divl1+30*20)
l22 = ttk.Label(second_frame, text = '0445 =')
l22.place(x=divl,y=divl1+30*21)
l23 = ttk.Label(second_frame, text = '0446 =')
l23.place(x=divl,y=divl1+30*22)
l24 = ttk.Label(second_frame, text = '0447 =')
l24.place(x=divl,y=divl1+30*23)
l25 = ttk.Label(second_frame, text = '0448 =')
l25.place(x=divl,y=divl1+30*24)
l26 = ttk.Label(second_frame, text = '0449 =')
l26.place(x=divl,y=divl1+30*25)
l27 = ttk.Label(second_frame, text = '0450 =')
l27.place(x=divl,y=divl1+30*26)
l28 = ttk.Label(second_frame, text = '0451 =')
l28.place(x=divl,y=divl1+30*27)
l29 = ttk.Label(second_frame, text = '0454 =')
l29.place(x=divl,y=divl1+30*28)
l30 = ttk.Label(second_frame, text = '0460 =')
l30.place(x=divl,y=divl1+30*29)
l31 = ttk.Label(second_frame, text = '0461 =')
l31.place(x=divl,y=divl1+30*30)
l32 = ttk.Label(second_frame, text = '0462 =')
l32.place(x=divl,y=divl1+30*31)
l33 = ttk.Label(second_frame, text = '0465 =')
l33.place(x=divl,y=divl1+30*32)
l34 = ttk.Label(second_frame, text = '0466 =')
l34.place(x=divl,y=divl1+30*33)
l35 = ttk.Label(second_frame, text = '0467 =')
l35.place(x=divl,y=divl1+30*34)
l36 = ttk.Label(second_frame, text = '0468 =')
l36.place(x=divl,y=divl1+30*35)
l37 = ttk.Label(second_frame, text = '0469 =')
l37.place(x=divl,y=divl1+30*36)
l38 = ttk.Label(second_frame, text = '0471 =')
l38.place(x=divl,y=divl1+30*37)

# GAZ

ent53=ttk.Entry(frame4, text="2", textvariable=v1)
ent53.place(x=dinx, y=diny)
ent54=ttk.Entry(frame4, text="2", textvariable=v2)
ent54.place(x=dinx, y=diny+dinm)
ent55=ttk.Entry(frame4, text="2", textvariable=v3)
ent55.place(x=dinx, y=diny+dinm*2)
ent56=ttk.Entry(frame4, text="2", textvariable=v4)
ent56.place(x=dinx, y=diny+dinm*3)
ent57=ttk.Entry(frame4, text="2", textvariable=v5)
ent57.place(x=dinx, y=diny+dinm*4)
ent58=ttk.Entry(frame4, text="2", textvariable=v6)
ent58.place(x=dinx, y=diny+dinm*5)
ent59=ttk.Entry(frame4, text="2", textvariable=v7)
ent59.place(x=dinx, y=diny+dinm*6)
ent60=ttk.Entry(frame4, text="2", textvariable=v8)
ent60.place(x=dinx, y=diny+dinm*7)
ent61=ttk.Entry(frame4, text="2", textvariable=v9)
ent61.place(x=dinx, y=diny+dinm*8)
ent62=ttk.Entry(frame4, text="2", textvariable=v10)
ent62.place(x=dinx, y=diny+dinm*9)

sort53=ttk.Entry(frame4, text="2", textvariable=s1)
sort53.place(x=disx, y=diny)
sort54=ttk.Entry(frame4, text="2", textvariable=s2)
sort54.place(x=disx, y=diny+dinm)
sort55=ttk.Entry(frame4, text="2", textvariable=s3)
sort55.place(x=disx, y=diny+dinm*2)
sort56=ttk.Entry(frame4, text="2", textvariable=s4)
sort56.place(x=disx, y=diny+dinm*3)
sort57=ttk.Entry(frame4, text="2", textvariable=s5)
sort57.place(x=disx, y=diny+dinm*4)
sort58=ttk.Entry(frame4, text="2", textvariable=s6)
sort58.place(x=disx, y=diny+dinm*5)
sort59=ttk.Entry(frame4, text="2", textvariable=s7)
sort59.place(x=disx, y=diny+dinm*6)
sort60=ttk.Entry(frame4, text="2", textvariable=s8)
sort60.place(x=disx, y=diny+dinm*7)
sort61=ttk.Entry(frame4, text="2", textvariable=s9)
sort61.place(x=disx, y=diny+dinm*8)
sort62=ttk.Entry(frame4, text="2", textvariable=s10)
sort62.place(x=disx, y=diny+dinm*9)

l1 = ttk.Label(frame4, text = '0501 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(frame4, text = '0502 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(frame4, text = '0503 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(frame4, text = '0504 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(frame4, text = '0509 =')
l5.place(x=divl,y=divl1+30*4)
l6 = ttk.Label(frame4, text = '0510 =')
l6.place(x=divl,y=divl1+30*5)
l7 = ttk.Label(frame4, text = '0511 =')
l7.place(x=divl,y=divl1+30*6)
l8 = ttk.Label(frame4, text = '0513 =')
l8.place(x=divl,y=divl1+30*7)
l9 = ttk.Label(frame4, text = '0514 =')
l9.place(x=divl,y=divl1+30*8)
l10 = ttk.Label(frame4, text = '0320 =')
l10.place(x=divl,y=divl1+30*9)

# DIESEL

ent63=ttk.Entry(frame5, text="2", textvariable=v1)
ent63.place(x=dinx, y=diny)
ent64=ttk.Entry(frame5, text="2", textvariable=v2)
ent64.place(x=dinx, y=diny+dinm)
ent65=ttk.Entry(frame5, text="2", textvariable=v3)
ent65.place(x=dinx, y=diny+dinm*2)
ent66=ttk.Entry(frame5, text="2", textvariable=v4)
ent66.place(x=dinx, y=diny+dinm*3)
ent67=ttk.Entry(frame5, text="2", textvariable=v5)
ent67.place(x=dinx, y=diny+dinm*4)
ent68=ttk.Entry(frame5, text="2", textvariable=v6)
ent68.place(x=dinx, y=diny+dinm*5)
ent69=ttk.Entry(frame5, text="2", textvariable=v7)
ent69.place(x=dinx, y=diny+dinm*6)
ent70=ttk.Entry(frame5, text="2", textvariable=v8)
ent70.place(x=dinx, y=diny+dinm*7)
ent71=ttk.Entry(frame5, text="2", textvariable=v9)
ent71.place(x=dinx, y=diny+dinm*8)
ent72=ttk.Entry(frame5, text="2", textvariable=v10)
ent72.place(x=dinx, y=diny+dinm*9)
ent73=ttk.Entry(frame5, text="2", textvariable=v11)
ent73.place(x=dinx, y=diny+dinm*10)
ent74=ttk.Entry(frame5, text="2", textvariable=v12)
ent74.place(x=dinx, y=diny+dinm*11)
ent75=ttk.Entry(frame5, text="2", textvariable=v13)
ent75.place(x=dinx, y=diny+dinm*12)
ent76=ttk.Entry(frame5, text="2", textvariable=v14)
ent76.place(x=dinx, y=diny+dinm*13)

sort63=ttk.Entry(frame5, text="2", textvariable=s1)
sort63.place(x=disx, y=diny)
sort64=ttk.Entry(frame5, text="2", textvariable=s2)
sort64.place(x=disx, y=diny+dinm)
sort65=ttk.Entry(frame5, text="2", textvariable=s3)
sort65.place(x=disx, y=diny+dinm*2)
sort66=ttk.Entry(frame5, text="2", textvariable=s4)
sort66.place(x=disx, y=diny+dinm*3)
sort67=ttk.Entry(frame5, text="2", textvariable=s5)
sort67.place(x=disx, y=diny+dinm*4)
sort68=ttk.Entry(frame5, text="2", textvariable=s6)
sort68.place(x=disx, y=diny+dinm*5)
sort69=ttk.Entry(frame5, text="2", textvariable=s7)
sort69.place(x=disx, y=diny+dinm*6)
sort70=ttk.Entry(frame5, text="2", textvariable=s8)
sort70.place(x=disx, y=diny+dinm*7)
sort71=ttk.Entry(frame5, text="2", textvariable=s9)
sort71.place(x=disx, y=diny+dinm*8)
sort72=ttk.Entry(frame5, text="2", textvariable=s10)
sort72.place(x=disx, y=diny+dinm*9)
sort73=ttk.Entry(frame5, text="2", textvariable=s11)
sort73.place(x=disx, y=diny+dinm*10)
sort74=ttk.Entry(frame5, text="2", textvariable=s12)
sort74.place(x=disx, y=diny+dinm*11)
sort75=ttk.Entry(frame5, text="2", textvariable=s13)
sort75.place(x=disx, y=diny+dinm*12)
sort76=ttk.Entry(frame5, text="2", textvariable=s14)
sort76.place(x=disx, y=diny+dinm*13)

l1 = ttk.Label(frame5, text = '0530 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(frame5, text = '0531 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(frame5, text = '0532 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(frame5, text = '0533 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(frame5, text = '0534 =')
l5.place(x=divl,y=divl1+30*4)
l6 = ttk.Label(frame5, text = '0535 =')
l6.place(x=divl,y=divl1+30*5)
l7 = ttk.Label(frame5, text = '0536 =')
l7.place(x=divl,y=divl1+30*6)
l8 = ttk.Label(frame5, text = '0537 =')
l8.place(x=divl,y=divl1+30*7)
l9 = ttk.Label(frame5, text = '0538 =')
l9.place(x=divl,y=divl1+30*8)
l10 = ttk.Label(frame5, text = '0539 =')
l10.place(x=divl,y=divl1+30*9)
l11 = ttk.Label(frame5, text = '0541 =')
l11.place(x=divl,y=divl1+30*10)
l12 = ttk.Label(frame5, text = '0542 =')
l12.place(x=divl,y=divl1+30*11)
l13 = ttk.Label(frame5, text = '0543 =')
l13.place(x=divl,y=divl1+30*12)
l14 = ttk.Label(frame5, text = '0320 =')
l14.place(x=divl,y=divl1+30*13)


# REGLOPHORE

ent77=ttk.Entry(frame6, text="2", textvariable=v1)
ent77.place(x=dinx, y=diny)
ent78=ttk.Entry(frame6, text="2", textvariable=v2)
ent78.place(x=dinx, y=diny+dinm)
ent79=ttk.Entry(frame6, text="2", textvariable=v3)
ent79.place(x=dinx, y=diny+dinm*2)
ent80=ttk.Entry(frame6, text="2", textvariable=v4)
ent80.place(x=dinx, y=diny+dinm*3)
ent81=ttk.Entry(frame6, text="2", textvariable=v5)
ent81.place(x=dinx, y=diny+dinm*4)
ent82=ttk.Entry(frame6, text="2", textvariable=v6)
ent82.place(x=dinx, y=diny+dinm*5)
ent83=ttk.Entry(frame6, text="2", textvariable=v7)
ent83.place(x=dinx, y=diny+dinm*6)
ent84=ttk.Entry(frame6, text="2", textvariable=v8)
ent84.place(x=dinx, y=diny+dinm*7)

sort77=ttk.Entry(frame6, text="2", textvariable=s1)
sort77.place(x=disx, y=diny)
sort78=ttk.Entry(frame6, text="2", textvariable=s2)
sort78.place(x=disx, y=diny+dinm)
sort79=ttk.Entry(frame6, text="2", textvariable=s3)
sort79.place(x=disx, y=diny+dinm*2)
sort80=ttk.Entry(frame6, text="2", textvariable=s4)
sort80.place(x=disx, y=diny+dinm*3)
sort81=ttk.Entry(frame6, text="2", textvariable=s5)
sort81.place(x=disx, y=diny+dinm*4)
sort82=ttk.Entry(frame6, text="2", textvariable=s6)
sort82.place(x=disx, y=diny+dinm*5)
sort83=ttk.Entry(frame6, text="2", textvariable=s7)
sort83.place(x=disx, y=diny+dinm*6)
sort84=ttk.Entry(frame6, text="2", textvariable=s8)
sort84.place(x=disx, y=diny+dinm*7)

l1 = ttk.Label(frame6, text = '0320 =')
l1.place(x=divl,y=divl1)
l2= ttk.Label(frame6, text = '0200 =')
l2.place(x=divl,y=divl1+30)
l3= ttk.Label(frame6, text = '0490 =')
l3.place(x=divl,y=divl1+30*2)
l4 = ttk.Label(frame6, text = '0491 =')
l4.place(x=divl,y=divl1+30*3)
l5 = ttk.Label(frame6, text = '0492 =')
l5.place(x=divl,y=divl1+30*4)
l6 = ttk.Label(frame6, text = '0493 =')
l6.place(x=divl,y=divl1+30*5)
l7 = ttk.Label(frame6, text = '0494 =')
l7.place(x=divl,y=divl1+30*6)
l8 = ttk.Label(frame6, text = '0495 =')
l8.place(x=divl,y=divl1+30*7)

canvas = Canvas(frame0, width = 140, height = 100)      
canvas.place(x=260, y=18)
img = PhotoImage(file="ressources/icons/dekcrack.png")      
canvas.create_image(0, 0, anchor=NW, image=img ) 
        
class hasna:
    def __init__(self, master, frameX):
        
        dir=400

        btn2=ttk.Button(frameX, text="Read Data", command=lambda:[select_file()])
        btn2.place(x=dir, y=205-20)

        btn3=ttk.Button(frameX, text="Write Data", command=lambda:[step(), Writer(
        v1,
        v2,
        v3,
        v4,
        v5,
        v6,
        v7,
        v8,
        v9,
        s1,
        s2,
        s3,
        s4,
        s5,
        s6,
        s7,
        s8,
        s9,
        folder_selected
        )])
        btn3.place(x=dir, y=155)

        btn4=ttk.Button(frameX, text="RES Path", command=lambda:[select_path()])
        btn4.place(x=dir, y=125)

        btn5=ttk.Button(frameX, text="Delete All", command=lambda:[DelAll()])
        btn5.place(x=dir+10, y=380)

        btn6=ttk.Button(frameX, text="Info.", command=lambda:[MoreInf()])
        btn6.place(x=dir+80+10, y=380)

        btn7=ttk.Button(frameX, text="Guide", command=lambda:[Guide()])
        btn7.place(x=dir+160+10, y=380)

        txt3 = ttk.Label(frameX, text = 'MATRICULE', font=("Time New Roman", 12))
        txt3.place(x=485 ,y=315)
        txt3.configure(anchor="center")


        txt4 = ttk.Entry(frameX, text = "", font=(12), justify='center')
        txt4.place(x=440 ,y=342)        
    
        # Info Label

        lblinf1 = ttk.Label(frameX, text="Method :", font=("Time New Roman", 8))
        lblinf1.place(x=495, y=455)

        lblinf2 = ttk.Label(frameX, text="Matricule :", font=("Time New Roman", 8))
        lblinf2.place(x=495, y=480)

        lblinf3 = ttk.Label(frameX, text="GiegLan :", font=("Time New Roman", 8))
        lblinf3.place(x=495, y=505)
           
        lblinf4 = ttk.Label(frameX, text="Server :", font=("Time New Roman", 8))
        lblinf4.place(x=495, y=530)

        lblinf5 = ttk.Label(frameX, text="Susspension", font=("Time New Roman", 8))
        lblinf5.place(x=560, y=455)


        #Internet
        lblinfinternet = ttk.Label(frameX, text="", font=("Time New Roman", 8), width=10, foreground="")
        lblinfinternet.place(x=560, y=530)

        checkInternetConnection(lblinfinternet)


def DelAll():
    for i in range(1,85):
        fun1 = f"ent{i}.delete(0,'end')"
        funx1 = exec(fun1)
        fun2 = f"sort{i}.delete(0,'end')"
        funx2 = exec(fun2)
    txt4.delete(0,'end')

def Valeus():
    print(s1)
    funx6 = txt4.delete(0,'end')
    fun6 = txt4.insert(0,v1)     
    lblinfMT["text"]=v1
    for i in range (1,85):
        fun1 = f"v{i} = ent{i}.get()"
        funx1 = exec(fun1) 
        fun5 = f"s{i} = string_to_crc(v{i})"
        funx5 = exec(fun5) 
        #fun3 = f"s{i} = ans"
        #funx3 = exec(fun3)
        fun2 = f"sort{i}.delete(0,'end')"
        funx2 = exec(fun2)
        fun4 = f"sort{i}.insert(0,s{i})"
        funx4 = exec(fun4)


def step(pb,txt1):
    for i in range(80):
        window.update_idletasks()
        pb['value'] += 1.25
        time.sleep(0.02)
        txt1['text']= pb['value'],'%'
    pb['value'] = 0
    txt1['text'] = 0

callinit = hasna(window, frame1)
callinit = hasna(window, frame2)
callinit = hasna(window, frame3)
callinit = hasna(window, frame4)
callinit = hasna(window, frame5)
callinit = hasna(window, frame6)


        
txt4 = ttk.Entry(frame1, text = "", font=(12), justify='center')
txt4.place(x=440 ,y=342) 

bar1 = tk.Frame(window, bg="#007e41", height=50, width=700)
bar1.place(x=-2 ,y=610)

lblinfMT = ttk.Label(frame1, text="No Data", font=("Time New Roman", 8))
lblinfMT.place(x=560, y=480)
        

txtbar1 = tk.Label(window, text="DekCrack v1.01 - GiegLan Tool", foreground ="white", bg="#007e41", font=("Time New Roman",9))
txtbar1.place(x=257,y=610) 
txtbar1.configure(anchor="center")


window.mainloop()
