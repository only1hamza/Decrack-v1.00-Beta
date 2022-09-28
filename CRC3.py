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
window.title("DekCrack")
window.geometry("690x650+10+10")
window.iconbitmap("DekCrack.ico")
window.resizable(False, False)

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
frame8 = ttk.Frame(notebook)
frame8.pack()

notebook.add(frame0, text="GiegLan")
notebook.add(frame1, text="Susspension")
notebook.add(frame2, text="Rippage")
notebook.add(frame3, text="Susspension")
notebook.add(frame4, text="Frienment")
notebook.add(frame5, text="Gaz")
notebook.add(frame6, text="Diesel")
notebook.add(frame7, text="Reglophore")
notebook.add(frame8, text="About")

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



canvas = Canvas(frame0, width = 140, height = 100)      
canvas.place(x=260, y=18)
img = PhotoImage(file="ressources/icons/dekcrack.png")      
canvas.create_image(0, 0, anchor=NW, image=img ) 




dir=400

# Frames


frameer1 = ttk.Frame(frame1, width=690, height=630)
frameer1.grid(row=0, column=0)

lf1 = ttk.LabelFrame(frame1, text = 'Actions', height=135, width=90, labelanchor="n")
lf1.place(x=dir-7,y=80)

lf2 = ttk.LabelFrame(frame1, text = 'CRC', height=565, width=140, labelanchor="n")
lf2.place(x=243,y=10)

lfmsr = ttk.LabelFrame(frame1, text = 'Mesures', height=565, width=140, labelanchor="n")
lfmsr.place(x=96,y=10) 

lf3 = ttk.LabelFrame(frame1, text = 'Ser.', height=565, width=70, labelanchor="n")
lf3.place(x=20,y=10) 

lf4 = ttk.LabelFrame(frame1, text = 'File Type', height=60, width=270, labelanchor="n")
lf4.place(x=dir-7,y=10)

lfpgr = ttk.LabelFrame(frame1, text = 'Progress', height=60, width=270, labelanchor="nw")
lfpgr.place(x=dir-7,y=225)

lf5 = ttk.LabelFrame(frame1, text = 'Statu', height=135, width=170, labelanchor="n")
lf5.place(x=dir-7+100,y=80)

lf6 = ttk.LabelFrame(frame1, text = 'Outils', height=120, width=270, labelanchor="nw")
lf6.place(x=dir-7,y=295)

lf7 = ttk.LabelFrame(frame1, text = 'Info', height=150, width=270, labelanchor="nw")
lf7.place(x=dir-7,y=425)




divl=35
divl1=32

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
l10 = ttk.Label(frame1, text = '0000 =')
l10.place(x=divl,y=divl1+30*9)
l11 = ttk.Label(frame1, text = '0000 =')
l11.place(x=divl,y=divl1+30*10)
l12 = ttk.Label(frame1, text = '0000 =')
l12.place(x=divl,y=divl1+30*11)
l13 = ttk.Label(frame1, text = '0000 =')
l13.place(x=divl,y=divl1+30*12)
l14 = ttk.Label(frame1, text = '0000 =')
l14.place(x=divl,y=divl1+30*13)
l15 = ttk.Label(frame1, text = '0000 =')
l15.place(x=divl,y=divl1+30*14)
l16 = ttk.Label(frame1, text = '0000 =')
l16.place(x=divl,y=divl1+30*15)
l17 = ttk.Label(frame1, text = '0000 =')
l17.place(x=divl,y=divl1+30*16)
l18 = ttk.Label(frame1, text = '0000 =')
l18.place(x=divl,y=divl1+30*17)


# Entry Variables
v1 = ""
v2 = ""
v3 = ""
v4 = ""
v5 = ""

v6 = ""
v7 = ""
v8 = ""
v9 = ""
v10 = ""

v11 = ""
v12 = ""
v13 = ""
v14 = ""
v15 = ""

v16 = ""
v17 = ""
v18 = ""

dis=103
dis2=30

# Entrys
ent1=ttk.Entry(frame1, text="2", textvariable=v1)
ent1.place(x=dis, y=dis2)
ent2=ttk.Entry(frame1, text="2", textvariable=v2)
ent2.place(x=dis, y=dis2+30)
ent3=ttk.Entry(frame1, text="2", textvariable=v3)
ent3.place(x=dis, y=dis2+30*2)
ent4=ttk.Entry(frame1, text="2", textvariable=v4)
ent4.place(x=dis, y=dis2+30*3)
ent5=ttk.Entry(frame1, text="2", textvariable=v5)
ent5.place(x=dis, y=dis2+30*4)

ent6=ttk.Entry(frame1, text="2", textvariable=v6)
ent6.place(x=dis, y=dis2+30*5)
ent7=ttk.Entry(frame1, text="2", textvariable=v7)
ent7.place(x=dis, y=dis2+30*6)
ent8=ttk.Entry(frame1, text="2", textvariable=v8)
ent8.place(x=dis, y=dis2+30*7)
ent9=ttk.Entry(frame1, text="2", textvariable=v9)
ent9.place(x=dis, y=dis2+30*8)
ent10=ttk.Entry(frame1, text="2", textvariable=v10)
ent10.place(x=dis, y=dis2+30*9)

ent11=ttk.Entry(frame1, text="2", textvariable=v11)
ent11.place(x=dis, y=dis2+30*10)
ent12=ttk.Entry(frame1, text="2", textvariable=v12)
ent12.place(x=dis, y=dis2+30*11)
ent13=ttk.Entry(frame1, text="2", textvariable=v13)
ent13.place(x=dis, y=dis2+30*12)
ent14=ttk.Entry(frame1, text="2", textvariable=v14)
ent14.place(x=dis, y=dis2+30*13)
ent15=ttk.Entry(frame1, text="2", textvariable=v15)
ent15.place(x=dis, y=dis2+30*14)

ent16=ttk.Entry(frame1, text="2", textvariable=v16)
ent16.place(x=dis, y=dis2+30*15)
ent17=ttk.Entry(frame1, text="2", textvariable=v17)
ent17.place(x=dis, y=dis2+30*16)
ent18=ttk.Entry(frame1, text="2", textvariable=v18)
ent18.place(x=dis, y=dis2+30*17)

# Sorties Variables
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""

s6 = ""
s7 = ""
s8 = ""
s9 = ""
s10 = ""

s11 = ""
s12 = ""
s13 = ""
s14 = ""
s15 = ""

s16 = ""
s17 = ""
s18 = ""

dim=250
dim2=30

# Sorties
sort1=ttk.Entry(frame1, text="2", textvariable=s1)
sort1.place(x=dim, y=dim2)
sort2=ttk.Entry(frame1, text="2", textvariable=s2)
sort2.place(x=dim, y=dim2+30)
sort3=ttk.Entry(frame1, text="2", textvariable=s3)
sort3.place(x=dim, y=dim2+30*2)
sort4=ttk.Entry(frame1, text="2", textvariable=s4)
sort4.place(x=dim, y=dim2+30*3)
sort5=ttk.Entry(frame1, text="2", textvariable=s5)
sort5.place(x=dim, y=dim2+30*4)

sort6=ttk.Entry(frame1, text="2", textvariable=s6)
sort6.place(x=dim, y=dim2+30*5)
sort7=ttk.Entry(frame1, text="2", textvariable=s7)
sort7.place(x=dim, y=dim2+30*6)
sort8=ttk.Entry(frame1, text="2", textvariable=s8)
sort8.place(x=dim, y=dim2+30*7)
sort9=ttk.Entry(frame1, text="2", textvariable=s9)
sort9.place(x=dim, y=dim2+30*8)
sort10=ttk.Entry(frame1, text="2", textvariable=s10)
sort10.place(x=dim, y=dim2+30*9)

sort11=ttk.Entry(frame1, text="2", textvariable=s11)
sort11.place(x=dim, y=dim2+30*10)
sort12=ttk.Entry(frame1, text="2", textvariable=s12)
sort12.place(x=dim, y=dim2+30*11)
sort13=ttk.Entry(frame1, text="2", textvariable=s13)
sort13.place(x=dim, y=dim2+30*12)
sort14=ttk.Entry(frame1, text="2", textvariable=s14)
sort14.place(x=dim, y=dim2+30*13)
sort15=ttk.Entry(frame1, text="2", textvariable=s15)
sort15.place(x=dim, y=dim2+30*14)

sort16=ttk.Entry(frame1, text="2", textvariable=s16)
sort16.place(x=dim, y=dim2+30*15)
sort17=ttk.Entry(frame1, text="2", textvariable=s17)
sort17.place(x=dim, y=dim2+30*16)
sort18=ttk.Entry(frame1, text="2", textvariable=s18)
sort18.place(x=dim, y=dim2+30*17)

# Read-Only (Not Working)
#for i in range(1,19):
#    x1=exec(f"sort{i}.configure(state='readonly')")
      
      
# Buttons

btn1=ttk.Button(frame1, text="Calculate", command=lambda:[step(), Valeus(), Fav(
v3,
v4,
v5,
v6,
v7,
v8,
fav,
cfav,
txtfav
), Good()])
btn1.place(x=dir, y=115-20)

btn2=ttk.Button(frame1, text="Read Data", command=lambda:[select_file()])
btn2.place(x=dir, y=205-20)

btn3=ttk.Button(frame1, text="Write Data", command=lambda:[step(), Writer(
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

btn4=ttk.Button(frame1, text="RES Path", command=lambda:[select_path()])
btn4.place(x=dir, y=125)

btn5=ttk.Button(frame1, text="Delete All", command=lambda:[DelAll()])
btn5.place(x=dir+10, y=380)

btn6=ttk.Button(frame1, text="Info.", command=lambda:[MoreInf()])
btn6.place(x=dir+80+10, y=380)

btn7=ttk.Button(frame1, text="Guide", command=lambda:[Guide()])
btn7.place(x=dir+160+10, y=380)

# Labels

txt1 = ttk.Label(window, text = '0%')
txt1.place(x=575 ,y=160+22)
txt1.configure(anchor="center")

bar1 = tk.Frame(window, bg="#007e41", height=50, width=700)
bar1.place(x=-2 ,y=610)

txtbar1 = tk.Label(window, text="DekCrack v1.01 - GiegLan Tool", foreground ="white", bg="#007e41", font=("Time New Roman",9))
txtbar1.place(x=257,y=610) 
txtbar1.configure(anchor="center")

txt2 = ttk.Label(window, text = 'SUSPENSION MESURE', font=("Time New Roman", 16))
txt2.place(x=412 ,y=30+22)
txt2.configure(anchor="center")

txt3 = ttk.Label(window, text = 'MATRICULE', font=("Time New Roman", 12))
txt3.place(x=485 ,y=315+22)
txt3.configure(anchor="center")


txt4 = ttk.Entry(window, text = "", font=(12), justify='center')
txt4.place(x=440 ,y=342+22)

# ProgressBar
pb =ttk.Progressbar(window, orient=HORIZONTAL, length=250, mode='determinate')
pb.place(x=403,y=248+22)


# Variable
fav = "No Statu yet"
cfav = "black"
txtfav = tk.Label(window, text = fav, foreground = cfav, font=("Time New Roman",10))
txtfav.place(x=505 ,y=125+22)
txtfav.configure(anchor="center")


# Images
"""
canvas = Canvas(window, width = 110, height = 110)      
canvas.place(x=400, y=465)
img = PhotoImage(file="ressources/icons/sus.png")      
canvas.create_image(0, 0, anchor=NW, image=img) 
"""

# Info Label

lblinf1 = ttk.Label(window, text="Method :", font=("Time New Roman", 8))
lblinf1.place(x=495, y=455+22)

lblinf2 = ttk.Label(window, text="Matricule :", font=("Time New Roman", 8))
lblinf2.place(x=495, y=480+22)

lblinf3 = ttk.Label(window, text="GiegLan :", font=("Time New Roman", 8))
lblinf3.place(x=495, y=505+22)
   
lblinf4 = ttk.Label(window, text="Server :", font=("Time New Roman", 8))
lblinf4.place(x=495, y=530+22)

lblinf5 = ttk.Label(window, text="Susspension", font=("Time New Roman", 8))
lblinf5.place(x=560, y=455+22)

lblinfMT = ttk.Label(window, text="No Data", font=("Time New Roman", 8))
lblinfMT.place(x=560, y=480+22)

#Internet
lblinfinternet = ttk.Label(window, text="", font=("Time New Roman", 8), width=10, foreground="")
lblinfinternet.place(x=560, y=530+22)

checkInternetConnection(lblinfinternet)


################################### RES ###################################
# Error Ran : Don't load empty DataSave
lblinf7 = ttk.Label(frame1, text="", font=("Time New Roman", 8))
lblinf7.place(x=560, y=505)

folder_selected=""
if os.path.exists("DataSave.dat") == True :
    if os.path.getsize("DataSave.dat") > 0 :
        folder_selected = pickle.load(open("DataSave.dat", "rb"))
else:
    Data = open("DataSave.dat", "wb")
    Data.close()
    folder_selected = "RES"

counter1=folder_selected.count("RES")

if counter1 >= 1:
    lblinf7["text"]="YES"
    lblinf7["foreground"]="#007e41"
    print(lblinf7["text"])
else:
    lblinf7["text"]="Bad"
    lblinf7["foreground"]="red"
    print(lblinf7["text"])
################################### RES ###################################
    

print(v3,v4,v5)
    
def ON(value):
    if value == 1:
        for i in range (10,19):
            fun1 = f"ent{i}.config(state=tk.NORMAL)"
            funx1 = exec(fun1)
    elif value ==2:
        for i in range (10,19):
            fun1 = f"ent{i}.config(state=tk.DISABLED)"  
            funx1 = exec(fun1)

def step():
    for i in range(80):
        window.update_idletasks()
        pb['value'] += 1.25
        time.sleep(0.02)
        txt1['text']= pb['value'],'%'
    pb['value'] = 0
    txt1['text'] = 0
        
    
def Valeus():
    for i in range (1,39):
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
        funx6 = txt4.delete(0,'end')
        fun6 = txt4.insert(0,v1)
            
        lblinfMT["text"]=v1
            

def select_file():
    filetypes = (('Mesure Files', '*.F;*.G;*.P;*.O;*.R;*.S;*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    #print(filename)
    OF = open(f"{filename}","r")
    #print(OF.readlines())
    DelAll()
    File=OF.readlines()
    FileClean=[]
    for element in File:
        FileClean.append(element.strip())
        print(FileClean[0:])
    for i in range (0,9):
        FS = FileClean[i+1]
        funxn1 = exec(f"ent{i+1}.delete(0,'end')")
        funxn2 = exec(f"ent{i+1}.insert(0,FS[5:])")

def select_path(self, *args):
    folder_selected = fd.askdirectory()
    counter1=folder_selected.count("RES")
    if counter1 >= 1:
        lblinf7["text"]="YES"
        lblinf7["foreground"]="#007e41"
    else:
        lblinf7["text"]="Bad"
        lblinf7["foreground"]="red"
    print(folder_selected)
    pickle.dump(folder_selected, open("DataSave.dat", "wb"))

    
def DelAll():
    for i in range(1,19):
        fun1 = f"ent{i}.delete(0,'end')"
        funx1 = exec(fun1)
        fun2 = f"sort{i}.delete(0,'end')"
        funx2 = exec(fun2)
    txt4.delete(0,'end')
              # Window 1
        
def Good():
    if txtfav["text"] == "FAVORABLE":
        messagebox.showinfo("DekCrack",f'Mesures is ***{txtfav["text"]}***')
    elif txtfav["text"] == "DEFAVORABLE":
        messagebox.showwarning("DekCrack",f'Mesures is ***{txtfav["text"]}***')    

def MoreInf():
    window1 = Toplevel(window)
    #window1.geometry("500x500")
    window1.title("More Information")
    window1.resizable(False,False)
    window1.lift()
    window1.attributes("-topmost", True)

    game_frame = Frame(window1)
    game_frame.pack()
    style = ttk.Style()
    style.configure("Treeview", background="", fielbackground="")
    style.map("Treeview", background=[('selected', '#007e41')])


    my_game = ttk.Treeview(game_frame)

        #define our column
    my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

        # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("player_id",anchor=CENTER, width=80)
    my_game.column("player_name",anchor=CENTER,width=80)
    my_game.column("player_Rank",anchor=CENTER,width=80)
    my_game.column("player_states",anchor=CENTER,width=80)
    my_game.column("player_city",anchor=CENTER,width=80)

        #Create Headings 
    my_game.heading("player_id",text="Ser.",anchor=CENTER)
    my_game.heading("player_name",text="Materiel",anchor=CENTER)
    my_game.heading("player_Rank",text="Statu",anchor=CENTER)
    my_game.heading("player_states",text="Mesure",anchor=CENTER)
    my_game.heading("player_city",text="State",anchor=CENTER)

        #add data 
    my_game.insert(parent='',index='end',iid=0,text='',
    values=('Sus1','','','',''))
    my_game.insert(parent='',index='end',iid=1,text='',
    values=('0410','Montesseur1','Droit',v3, 'FAV.'))
    my_game.insert(parent='',index='end',iid=2,text='',
    values=('0411','Montesseur1','Gauche',v4, 'FAV.'))
    my_game.insert(parent='',index='end',iid=3,text='',
    values=('0412','Montesseur1','Des.', v5, 'FAV.'))
    my_game.insert(parent='',index='end',iid=4,text='',
    values=('Sus2','','','' , ''))
    my_game.insert(parent='',index='end',iid=5,text='',
    values=('0413','Montesseur2','Droit',v6, 'FAV.'))
    my_game.insert(parent='',index='end',iid=6,text='',
    values=('0414','Montesseur2','Gauche',v7, 'FAV.'))
    my_game.insert(parent='',index='end',iid=7,text='',
    values=('0415','Montesseur2','Des.',v8, 'FAV.'))

    my_game.pack()

def Guide():
    DelAll()
    v1.insert(0,'Matricule')
    v2.insert(0,'Ser. Materiel')
    v3.insert(0,'Sus1 Droit')
    v4.insert(0,'Sus1 Gauche')
    v5.insert(0,'Des. Sus1')
    v6.insert(0,'Sus2 Droit')
    v7.insert(0,'Sus2 Gauche')
    v8.insert(0,'Des. Sus2')
    for i in range(1,19):
        fun4 = f"sort{i}.insert(0,'Cripting CRC')"
        funx4 = exec(fun4)
    for i in range(8,19):
        fun4 = f"vi{i}.insert(0,'Additional Valeus')"
        funx4 = exec(fun4)
    
def Login():
    secwin = Toplevel(window)
    secwin.geometry("250x250")
    secwin.title("Login")
    secwin.resizable(False, False)
    label15= ttk.Label(secwin, "Login")
    label15.pack()
    
def Fav(v3,v4,v5,v6,v7,v8,fav,cfav,txtfav):
    if float(v8) < 30 and float(v5) < 30 and float(v3) > 49 and float(v4) > 49 and float(v6) > 49 and float(v7) > 49 :
        fav = "FAVORABLE"
        cfav = "green"
        txtfav["text"] = f"{fav}"
        txtfav["foreground"] = f"{cfav}"
        print(fav+cfav)
        print(v3)
    else :
        fav = "DEFAVORABLE"
        cfav = "red"
        txtfav["text"] = f"{fav}"
        txtfav["foreground"] = f"{cfav}"
        print(fav+cfav)
        print(v3)
    return cfav , fav

window.mainloop()

