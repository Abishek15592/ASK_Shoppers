#This will be the modify items page for the seller
#----------Modules------------
##import mysql.connector
from tkinter import *
from tkinter import tix
import pickle
from tkinter import messagebox as box
from PIL import ImageTk, Image
#-------------Class---------------
##mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
##mycursor=mydb.cursor()
##mycursor.execute("create database if not exists seller")
##mycursor.execute("use seller")
##mycursor.execute("create table if not exists additem(nameofitem varchar(20),price integer,quantity integer)")
class nameofitem:
      def __init__(self,mainmaster,master,v):
            global c1
            master.bind('<Escape>',self.close)
            self.nameofseller=v
            self.master=mainmaster
            self.frame=master
            self.frame.configure(height=150,width=150)
            self.frame.pack()
            
            self.namel=Label(master,text="NAME OF ITEM",bg=c1[0])
            self.namel.grid(row=1,column=0)
            self.nameofvar1=StringVar()
            self.name=Entry(master,fg="black",bg="white",text="name of item",textvariable=self.nameofvar1)
            self.name.grid(row=1,column=1)
            
            self.pricef=IntVar()
            self.price1=Label(master,text="PRICE OF THE ITEM",font='Avantagesmall',bg=c1[0]).grid(row=2,column=0)
            self.price=Entry(master,bg="white",textvariable=self.pricef).grid(row=2,column=1)

            self.quantity1=IntVar()
            self.quant=Label(master,font='Avantagesmall',text="QUANTITY",bg=c1[0]).grid(row=4,column=0)
            self.quante=Entry(master,bg="white",textvariable=self.quantity1).grid(row=4,column=1)

            self.img=Label(master,text="Image of the item",bg=c1[0]).grid(row=5,column=0)
            self.imgadd=StringVar()
            self.image=Entry(master,text="Image location",bg="white",font='Avantagesmall',textvariable=self.imgadd)
            self.image.grid(row=5,column=1)
            

            self.add=Button(master,bg=c1[0],text="ADD ITEM",font='Avantagesmall',command=self.additems).grid(row=10,column=0)    #Button to add items to the text file

            self.back=Button(master,bg=c1[0],text="Back",font='Avantagesmall',command=self.backbutton).grid(row=14,column=7)
##            mycursor.execute("insert into additem('{}',{},{})".format(self.name,self.price,self.quante)
##                             
##            mycursor.execute("select * from additem")
##            for x in mycursor:
##                             print(x)
      def close(self,event):
            self.master.withdraw()
            sys.exit()
      def additems(self):
            self.nameofvar1=self.name.get()
            self.hello1,self.hello2=1,1
            imgadd1=self.image.get()
            checkvariable=0
            try:
                  self.pri=self.pricef.get()
            except ValueError:
                  box.showerror("ERROR 101","Invalid integer for price")
                  self.deletefunc()
                  self.hello1=0
            try:
                  self.img=ImageTk.PhotoImage(Image.open(imgadd1))
            except IOError:
                  box.showerror("Error 404","Enter Valid /image Location")
                  checkvariable=1
            try:
                  self.quantv1=self.quantity1.get()
            except ValueError:
                  box.showerror("ERROR 101","Invalid integer for quantity")
                  self.deletefunc()
                  self.hello2=0
                  
            if self.hello1!=0 and self.hello2!=0 and checkvariable!=1:
                  name=self.nameofseller+".txt"
                  g=open("Productsdata.dat","rb")
                  l=pickle.load(g)
                  l.append(self.nameofvar1)
                  g.close()
                  g=open("Productsdata.dat","ab")
                  g.truncate()
                  pickle.dump(l,g)
                  g.close()
                  f=open(name,"a")
                  final=str(self.nameofvar1)+":"+str(self.pri)+":"+str(self.quantv1)+":"+str(imgadd1)
                  f.write(final+'\n')
                  f.close()
                  self.deletefunc()
      def deletefunc(self):                              #Function to reset all values to the original ones
            self.name.delete(0,END)
            self.pricef.set("0")
            self.quantity1.set("1")
            self.image.delete(0,END)
      def backbutton(self):
            import sellerspart
            self.frame.destroy()
            e=sellerspart.execute(self.master,self.nameofseller)
            
class pulldownmenu:
      def __init__(self,master,v):
            menubar=Menu(master)

            #Creating a display of the sellers name
            display=Menu(menubar,tearoff=0)
            name="Hello "+v
            menubar.add_cascade(label=name,menu=display)

            master.config(menu=menubar)

#--------------Mainsection---------
c1=['#44B3C2','#C92D22','#16776A','#1EBBA6']

