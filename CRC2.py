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

class Window:
    def __init__(self, win):

        #self.Login()
        
        self.notebook=ttk.Notebook(win)
        
        frame0 = ttk.Frame(self.notebook)
        frame0.place()
        frame1 = ttk.Frame(self.notebook)
        frame1.place()
        frame2 = ttk.Frame(self.notebook)
        frame2.pack()
        frame3 = ttk.Frame(self.notebook)
        frame3.pack()
        frame4 = ttk.Frame(self.notebook)
        frame4.pack()
        frame5 = ttk.Frame(self.notebook)
        frame5.pack()
        frame6 = ttk.Frame(self.notebook)
        frame6.pack()
        frame7 = ttk.Frame(self.notebook)
        frame7.pack()
        frame8 = ttk.Frame(self.notebook)
        frame8.pack()
        
        self.notebook.add(frame0, text="GiegLan")
        self.notebook.add(frame1, text="Susspension")
        self.notebook.add(frame2, text="Rippage")
        self.notebook.add(frame3, text="Susspension")
        self.notebook.add(frame4, text="Frienment")
        self.notebook.add(frame5, text="Gaz")
        self.notebook.add(frame6, text="Diesel")
        self.notebook.add(frame7, text="Reglophore")
        self.notebook.add(frame8, text="About")
        
        self.notebook.pack()

        menubar = Menu(win, foreground='black', activebackground='white', activeforeground='black')
        file = Menu(menubar, tearoff=1, foreground='black')  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=win.quit)  
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
        Registration.add_command(label="Refresh Connection", command=lambda:[checkInternetConnection(self.lblinfinternet)])
        Registration.add_separator()     
        Registration.add_command(label="You Have 30 Day trail",)
        menubar.add_cascade(label="Registration", menu=Registration)
        
        help = Menu(menubar, tearoff=0)  
        help.add_command(label="About",)  
        menubar.add_cascade(label="Help", menu=help)  
    
        win.config(menu=menubar)
        
        dir=400
        
        # Frames
        
        frameer1 = ttk.Frame(frame1, width=690, height=630)
        frameer1.grid(row=0, column=0)
        
        self.lf1 = ttk.LabelFrame(frame1, text = 'Actions', height=135, width=90, labelanchor="n")
        self.lf1.place(x=dir-7,y=80)

        self.lf2 = ttk.LabelFrame(frame1, text = 'CRC', height=565, width=140, labelanchor="n")
        self.lf2.place(x=243,y=10)        
        
        self.lfmsr = ttk.LabelFrame(frame1, text = 'Mesures', height=565, width=140, labelanchor="n")
        self.lfmsr.place(x=96,y=10) 
        
        self.lf3 = ttk.LabelFrame(frame1, text = 'Ser.', height=565, width=70, labelanchor="n")
        self.lf3.place(x=20,y=10)         
        
        self.lf4 = ttk.LabelFrame(frame1, text = 'File Type', height=60, width=270, labelanchor="n")
        self.lf4.place(x=dir-7,y=10)
        
        self.lfpgr = ttk.LabelFrame(frame1, text = 'Progress', height=60, width=270, labelanchor="nw")
        self.lfpgr.place(x=dir-7,y=225)
        
        self.lf5 = ttk.LabelFrame(frame1, text = 'Statu', height=135, width=170, labelanchor="n")
        self.lf5.place(x=dir-7+100,y=80)        
        
        self.lf6 = ttk.LabelFrame(frame1, text = 'Outils', height=120, width=270, labelanchor="nw")
        self.lf6.place(x=dir-7,y=295)
        
        self.lf7 = ttk.LabelFrame(frame1, text = 'Info', height=150, width=270, labelanchor="nw")
        self.lf7.place(x=dir-7,y=425)
        
        
        
        
        divl=35
        divl1=32
        
        self.l1 = ttk.Label(frame1, text = '0200 =')
        self.l1.place(x=divl,y=divl1)
        self.l2= ttk.Label(frame1, text = '0320 =')
        self.l2.place(x=divl,y=divl1+30)
        self.l3= ttk.Label(frame1, text = '0410 =')
        self.l3.place(x=divl,y=divl1+30*2)
        self.l4 = ttk.Label(frame1, text = '0411 =')
        self.l4.place(x=divl,y=divl1+30*3)
        self.l5 = ttk.Label(frame1, text = '0412 =')
        self.l5.place(x=divl,y=divl1+30*4)
        self.l6 = ttk.Label(frame1, text = '0413 =')
        self.l6.place(x=divl,y=divl1+30*5)
        self.l7 = ttk.Label(frame1, text = '0414 =')
        self.l7.place(x=divl,y=divl1+30*6)
        self.l8 = ttk.Label(frame1, text = '0415 =')
        self.l8.place(x=divl,y=divl1+30*7)
        self.l9 = ttk.Label(frame1, text = '0416 =')
        self.l9.place(x=divl,y=divl1+30*8)
        self.l10 = ttk.Label(frame1, text = '0000 =')
        self.l10.place(x=divl,y=divl1+30*9)
        self.l11 = ttk.Label(frame1, text = '0000 =')
        self.l11.place(x=divl,y=divl1+30*10)
        self.l12 = ttk.Label(frame1, text = '0000 =')
        self.l12.place(x=divl,y=divl1+30*11)
        self.l13 = ttk.Label(frame1, text = '0000 =')
        self.l13.place(x=divl,y=divl1+30*12)
        self.l14 = ttk.Label(frame1, text = '0000 =')
        self.l14.place(x=divl,y=divl1+30*13)
        self.l15 = ttk.Label(frame1, text = '0000 =')
        self.l15.place(x=divl,y=divl1+30*14)
        self.l16 = ttk.Label(frame1, text = '0000 =')
        self.l16.place(x=divl,y=divl1+30*15)
        self.l17 = ttk.Label(frame1, text = '0000 =')
        self.l17.place(x=divl,y=divl1+30*16)
        self.l18 = ttk.Label(frame1, text = '0000 =')
        self.l18.place(x=divl,y=divl1+30*17)
        

        # Entry Variables
        self.v1 = ""
        self.v2 = ""
        self.v3 = ""
        self.v4 = ""
        self.v5 = ""
        
        self.v6 = ""
        self.v7 = ""
        self.v8 = ""
        self.v9 = ""
        self.v10 = ""
        
        self.v11 = ""
        self.v12 = ""
        self.v13 = ""
        self.v14 = ""
        self.v15 = ""
        
        self.v16 = ""
        self.v17 = ""
        self.v18 = ""
        
        dis=103
        dis2=30
        
        # Entrys
        self.ent1=ttk.Entry(frame1, text="2", textvariable=self.v1)
        self.ent1.place(x=dis, y=dis2)
        self.ent2=ttk.Entry(frame1, text="2", textvariable=self.v2)
        self.ent2.place(x=dis, y=dis2+30)
        self.ent3=ttk.Entry(frame1, text="2", textvariable=self.v3)
        self.ent3.place(x=dis, y=dis2+30*2)
        self.ent4=ttk.Entry(frame1, text="2", textvariable=self.v4)
        self.ent4.place(x=dis, y=dis2+30*3)
        self.ent5=ttk.Entry(frame1, text="2", textvariable=self.v5)
        self.ent5.place(x=dis, y=dis2+30*4)
        
        self.ent6=ttk.Entry(frame1, text="2", textvariable=self.v6)
        self.ent6.place(x=dis, y=dis2+30*5)
        self.ent7=ttk.Entry(frame1, text="2", textvariable=self.v7)
        self.ent7.place(x=dis, y=dis2+30*6)
        self.ent8=ttk.Entry(frame1, text="2", textvariable=self.v8)
        self.ent8.place(x=dis, y=dis2+30*7)
        self.ent9=ttk.Entry(frame1, text="2", textvariable=self.v9)
        self.ent9.place(x=dis, y=dis2+30*8)
        self.ent10=ttk.Entry(frame1, text="2", textvariable=self.v10)
        self.ent10.place(x=dis, y=dis2+30*9)
        
        self.ent11=ttk.Entry(frame1, text="2", textvariable=self.v11)
        self.ent11.place(x=dis, y=dis2+30*10)
        self.ent12=ttk.Entry(frame1, text="2", textvariable=self.v12)
        self.ent12.place(x=dis, y=dis2+30*11)
        self.ent13=ttk.Entry(frame1, text="2", textvariable=self.v13)
        self.ent13.place(x=dis, y=dis2+30*12)
        self.ent14=ttk.Entry(frame1, text="2", textvariable=self.v14)
        self.ent14.place(x=dis, y=dis2+30*13)
        self.ent15=ttk.Entry(frame1, text="2", textvariable=self.v15)
        self.ent15.place(x=dis, y=dis2+30*14)
        
        self.ent16=ttk.Entry(frame1, text="2", textvariable=self.v16)
        self.ent16.place(x=dis, y=dis2+30*15)
        self.ent17=ttk.Entry(frame1, text="2", textvariable=self.v17)
        self.ent17.place(x=dis, y=dis2+30*16)
        self.ent18=ttk.Entry(frame1, text="2", textvariable=self.v18)
        self.ent18.place(x=dis, y=dis2+30*17)

        # Sorties Variables
        self.s1 = ""
        self.s2 = ""
        self.s3 = ""
        self.s4 = ""
        self.s5 = ""
        
        self.s6 = ""
        self.s7 = ""
        self.s8 = ""
        self.s9 = ""
        self.s10 = ""
        
        self.s11 = ""
        self.s12 = ""
        self.s13 = ""
        self.s14 = ""
        self.s15 = ""
        
        self.s16 = ""
        self.s17 = ""
        self.s18 = ""
        
        dim=250
        dim2=30
        
        # Sorties
        self.sort1=ttk.Entry(frame1, text="2", textvariable=self.s1)
        self.sort1.place(x=dim, y=dim2)
        self.sort2=ttk.Entry(frame1, text="2", textvariable=self.s2)
        self.sort2.place(x=dim, y=dim2+30)
        self.sort3=ttk.Entry(frame1, text="2", textvariable=self.s3)
        self.sort3.place(x=dim, y=dim2+30*2)
        self.sort4=ttk.Entry(frame1, text="2", textvariable=self.s4)
        self.sort4.place(x=dim, y=dim2+30*3)
        self.sort5=ttk.Entry(frame1, text="2", textvariable=self.s5)
        self.sort5.place(x=dim, y=dim2+30*4)
        
        self.sort6=ttk.Entry(frame1, text="2", textvariable=self.s6)
        self.sort6.place(x=dim, y=dim2+30*5)
        self.sort7=ttk.Entry(frame1, text="2", textvariable=self.s7)
        self.sort7.place(x=dim, y=dim2+30*6)
        self.sort8=ttk.Entry(frame1, text="2", textvariable=self.s8)
        self.sort8.place(x=dim, y=dim2+30*7)
        self.sort9=ttk.Entry(frame1, text="2", textvariable=self.s9)
        self.sort9.place(x=dim, y=dim2+30*8)
        self.sort10=ttk.Entry(frame1, text="2", textvariable=self.s10)
        self.sort10.place(x=dim, y=dim2+30*9)
        
        self.sort11=ttk.Entry(frame1, text="2", textvariable=self.s11)
        self.sort11.place(x=dim, y=dim2+30*10)
        self.sort12=ttk.Entry(frame1, text="2", textvariable=self.s12)
        self.sort12.place(x=dim, y=dim2+30*11)
        self.sort13=ttk.Entry(frame1, text="2", textvariable=self.s13)
        self.sort13.place(x=dim, y=dim2+30*12)
        self.sort14=ttk.Entry(frame1, text="2", textvariable=self.s14)
        self.sort14.place(x=dim, y=dim2+30*13)
        self.sort15=ttk.Entry(frame1, text="2", textvariable=self.s15)
        self.sort15.place(x=dim, y=dim2+30*14)
        
        self.sort16=ttk.Entry(frame1, text="2", textvariable=self.s16)
        self.sort16.place(x=dim, y=dim2+30*15)
        self.sort17=ttk.Entry(frame1, text="2", textvariable=self.s17)
        self.sort17.place(x=dim, y=dim2+30*16)
        self.sort18=ttk.Entry(frame1, text="2", textvariable=self.s18)
        self.sort18.place(x=dim, y=dim2+30*17)
        
        # Read-Only (Not Working)
        #for i in range(1,19):
        #    x1=exec(f"self.sort{i}.configure(state='readonly')")
      
      
        # Buttons
        
        self.btn1=ttk.Button(frame1, text="Calculate", command=lambda:[self.step(), self.Valeus(), Fav(
        self.v3,
        self.v4,
        self.v5,
        self.v6,
        self.v7,
        self.v8,
        self.fav,
        self.cfav,
        self.txt2
        ), self.Good()])
        self.btn1.place(x=dir, y=115-20)
        
        self.btn2=ttk.Button(frame1, text="Read Data", command=lambda:[self.select_file()])
        self.btn2.place(x=dir, y=205-20)
        
        self.btn3=ttk.Button(frame1, text="Write Data", command=lambda:[self.step(), Writer(
        self.v1,
        self.v2,
        self.v3,
        self.v4,
        self.v5,
        self.v6,
        self.v7,
        self.v8,
        self.v9,
        self.s1,
        self.s2,
        self.s3,
        self.s4,
        self.s5,
        self.s6,
        self.s7,
        self.s8,
        self.s9,
        self.folder_selected
        )])
        self.btn3.place(x=dir, y=155)
        
        self.btn4=ttk.Button(frame1, text="RES Path", command=lambda:[self.select_path()])
        self.btn4.place(x=dir, y=125)
        
        self.btn5=ttk.Button(frame1, text="Delete All", command=lambda:[self.DelAll()])
        self.btn5.place(x=dir+10, y=380)
        
        self.btn6=ttk.Button(frame1, text="Info.", command=lambda:[self.MoreInf()])
        self.btn6.place(x=dir+80+10, y=380)
        
        self.btn7=ttk.Button(frame1, text="Guide", command=lambda:[self.Guide()])
        self.btn7.place(x=dir+160+10, y=380)
        
        # Labels

        self.txt1 = ttk.Label(frame1, text = '0%')
        self.txt1.place(x=575 ,y=160)
        self.txt1.configure(anchor="center")

        self.bar1 = tk.Frame(win, bg="#007e41", height=50, width=700)
        self.bar1.place(x=-2 ,y=610)
        
        self.txtbar1 = tk.Label(win, text="DekCrack v1.01 - GiegLan Tool", foreground ="white", bg="#007e41", font=("Time New Roman",9))
        self.txtbar1.place(x=257,y=610) 
        self.txtbar1.configure(anchor="center")
        
        self.txt2 = ttk.Label(frame1, text = 'SUSPENSION MESURE', font=("Time New Roman", 16))
        self.txt2.place(x=412 ,y=30)
        self.txt2.configure(anchor="center")
        
        self.txt3 = ttk.Label(frame1, text = 'MATRICULE', font=("Time New Roman", 12))
        self.txt3.place(x=485 ,y=315)
        self.txt3.configure(anchor="center")
        
        
        self.txt4 = ttk.Entry(frame1, text = "", font=(12), justify='center')
        self.txt4.place(x=440 ,y=342)
        
        # ProgressBar
        self.pb =ttk.Progressbar(frame1, orient=HORIZONTAL, length=250, mode='determinate')
        self.pb.place(x=403,y=248)
        
        
        # Variable
        self.fav = "No Statu yet"
        self.cfav = "black"
        self.txt2 = tk.Label(frame1, text = self.fav, foreground = self.cfav, font=("Time New Roman",10))
        self.txt2.place(x=505 ,y=125)
        self.txt2.configure(anchor="center")
        
        
        # Images
        """
        self.canvas = Canvas(win, width = 110, height = 110)      
        self.canvas.place(x=400, y=465)
        self.img = PhotoImage(file="ressources/icons/sus.png")      
        self.canvas.create_image(0, 0, anchor=NW, image=self.img) 
        """
        
        # Info Label
        
        self.lblinf1 = ttk.Label(frame1, text="Method :", font=("Time New Roman", 8))
        self.lblinf1.place(x=495, y=455)
        
        self.lblinf2 = ttk.Label(frame1, text="Matricule :", font=("Time New Roman", 8))
        self.lblinf2.place(x=495, y=480)
        
        self.lblinf3 = ttk.Label(frame1, text="GiegLan :", font=("Time New Roman", 8))
        self.lblinf3.place(x=495, y=505)
           
        self.lblinf4 = ttk.Label(frame1, text="Server :", font=("Time New Roman", 8))
        self.lblinf4.place(x=495, y=530)

        self.lblinf5 = ttk.Label(frame1, text="Susspension", font=("Time New Roman", 8))
        self.lblinf5.place(x=560, y=455)
        
        self.lblinfMT = ttk.Label(frame1, text="No Data", font=("Time New Roman", 8))
        self.lblinfMT.place(x=560, y=480)
        
        #Internet
        self.lblinfinternet = ttk.Label(frame1, text="", font=("Time New Roman", 8), width=10, foreground="")
        self.lblinfinternet.place(x=560, y=530)
        
        checkInternetConnection(self.lblinfinternet)
        
        
        ################################### RES ###################################
        # Error Ran : Don't load empty DataSave
        self.lblinf7 = ttk.Label(frame1, text="", font=("Time New Roman", 8))
        self.lblinf7.place(x=560, y=505)
        
        self.folder_selected=""
        if os.path.exists("DataSave.dat") == True :
            if os.path.getsize("DataSave.dat") > 0 :
                self.folder_selected = pickle.load(open("DataSave.dat", "rb"))
        else:
            Data = open("DataSave.dat", "wb")
            Data.close()
            self.folder_selected = "RES"        
        
        counter1=self.folder_selected.count("RES")
        
        if counter1 >= 1:
            self.lblinf7["text"]="YES"
            self.lblinf7["foreground"]="#007e41"
            print(self.lblinf7["text"])
        else:
            self.lblinf7["text"]="Bad"
            self.lblinf7["foreground"]="red"
            print(self.lblinf7["text"])
        ################################### RES ###################################
            

            
    
    def ON(self,value):
        if value == 1:
            for i in range (10,19):
                fun1 = f"self.ent{i}.config(state=tk.NORMAL)"
                funx1 = exec(fun1)
        elif value ==2:
            for i in range (10,19):
                fun1 = f"self.ent{i}.config(state=tk.DISABLED)"  
                funx1 = exec(fun1)

    def step(self):
        for i in range(80):
            window.update_idletasks()
            self.pb['value'] += 1.25
            time.sleep(0.02)
            self.txt1['text']= self.pb['value'],'%'
        self.pb['value'] = 0
        self.txt1['text'] = 0
    
    
    def Valeus(self, *args):
        for i in range (1,19):
            fun1 = f"self.v{i} = self.ent{i}.get()"
            funx1 = exec(fun1) 
            fun5 = f"self.s{i} = string_to_crc(self.v{i})"
            funx5 = exec(fun5) 
            #fun3 = f"s{i} = ans"
            #funx3 = exec(fun3)
            fun2 = f"self.sort{i}.delete(0,'end')"
            funx2 = exec(fun2)
            fun4 = f"self.sort{i}.insert(0,self.s{i})"
            funx4 = exec(fun4)
            funx6 = self.txt4.delete(0,'end')
            fun6 = self.txt4.insert(0,self.v1)
            
            self.lblinfMT["text"]=self.v1
            
                
    def select_file(self, *args):
        filetypes = (('Mesure Files', '*.F;*.G;*.P;*.O;*.R;*.S;*.txt'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        #print(filename)
        OF = open(f"{filename}","r")
        #print(OF.readlines())
        self.DelAll()
        File=OF.readlines()
        FileClean=[]
        for element in File:
            FileClean.append(element.strip())
        print(FileClean[0:])
        for i in range (0,9):
            FS = FileClean[i+1]
            funxn1 = exec(f"self.ent{i+1}.delete(0,'end')")
            funxn2 = exec(f"self.ent{i+1}.insert(0,FS[5:])")
        
    def select_path(self, *args):
        self.folder_selected = fd.askdirectory()
        counter1=self.folder_selected.count("RES")
        if counter1 >= 1:
            self.lblinf7["text"]="YES"
            self.lblinf7["foreground"]="#007e41"
        else:
            self.lblinf7["text"]="Bad"
            self.lblinf7["foreground"]="red"
        print(self.folder_selected)
        pickle.dump(self.folder_selected, open("DataSave.dat", "wb"))
        
    
    def DelAll(self):
        for i in range(1,19):
            fun1 = f"self.ent{i}.delete(0,'end')"
            funx1 = exec(fun1)
            fun2 = f"self.sort{i}.delete(0,'end')"
            funx2 = exec(fun2)
        self.txt4.delete(0,'end')
      # Window 1
    
    def Good(self, *args):
        if self.txt2["text"] == "FAVORABLE":
            messagebox.showinfo("DekCrack",f'Mesures is ***{self.txt2["text"]}***')
        elif self.txt2["text"] == "DEFAVORABLE":
            messagebox.showwarning("DekCrack",f'Mesures is ***{self.txt2["text"]}***')    

    def MoreInf(self, *args):
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
        values=('0410','Montesseur1','Droit',self.v3, 'FAV.'))
        my_game.insert(parent='',index='end',iid=2,text='',
        values=('0411','Montesseur1','Gauche',self.v4, 'FAV.'))
        my_game.insert(parent='',index='end',iid=3,text='',
        values=('0412','Montesseur1','Des.', self.v5, 'FAV.'))
        my_game.insert(parent='',index='end',iid=4,text='',
        values=('Sus2','','','' , ''))
        my_game.insert(parent='',index='end',iid=5,text='',
        values=('0413','Montesseur2','Droit',self.v6, 'FAV.'))
        my_game.insert(parent='',index='end',iid=6,text='',
        values=('0414','Montesseur2','Gauche',self.v7, 'FAV.'))
        my_game.insert(parent='',index='end',iid=7,text='',
        values=('0415','Montesseur2','Des.',self.v8, 'FAV.'))

        my_game.pack()

    def Guide(self):
        self.DelAll()
        self.v1.insert(0,'Matricule')
        self.v2.insert(0,'Ser. Materiel')
        self.v3.insert(0,'Sus1 Droit')
        self.v4.insert(0,'Sus1 Gauche')
        self.v5.insert(0,'Des. Sus1')
        self.v6.insert(0,'Sus2 Droit')
        self.v7.insert(0,'Sus2 Gauche')
        self.v8.insert(0,'Des. Sus2')
        for i in range(1,19):
            fun4 = f"self.sort{i}.insert(0,'Cripting CRC')"
            funx4 = exec(fun4)
        for i in range(8,19):
            fun4 = f"self.vi{i}.insert(0,'Additional Valeus')"
            funx4 = exec(fun4)
    
    def Login(self, *args):
        secwin = Toplevel(window)
        secwin.geometry("250x250")
        secwin.title("Login")
        secwin.resizable(False, False)
        label15= ttk.Label(secwin, "Login")
        label15.pack()
    
    
window = tk.Tk()
MyWin = Window(window)
window.title("DekCrack")
window.geometry("690x630+10+10")
window.iconbitmap("DekCrack.ico")
window.resizable(False, False)
window.mainloop()

