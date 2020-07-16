#This will be the add items page for the seller
#----------Modules------------
from tkinter import *
from tkinter import tix
import pickle
from tkinter import messagebox as box
from PIL import ImageTk, Image
import os
#-------------Class---------------
class nameofitem:
      def __init__(self,mainmaster,master,v):
            global c1
            self.nameofseller=v
            self.master=mainmaster
            self.frame=master
            self.frame.configure(height=800,width=800)
            self.frame.pack()
            
            self.namel=Label(self.frame,text="NAME OF ITEM",bg=c1[0]).grid(row=0,column=0)
            self.nameofvar1=StringVar()
            self.name=Entry(self.frame,fg="black",bg="white",text="name of item",textvariable=self.nameofvar1)
            self.name.grid(row=0,column=1)
            
            self.pricee=IntVar()
            self.price1=Label(self.frame,text="PRICE OF THE ITEM",bg=c1[0]).grid(row=2,column=0)
            self.price=Entry(self.frame,bg="white",textvariable=self.pricee).grid(row=2,column=1)
            self.pricee.set("0")

            self.quantity=IntVar()
            self.quant=Label(self.frame,text="QUANTITY",bg=c1[0]).grid(row=4,column=0)
            self.quante=Entry(self.frame,bg="white",textvariable=self.quantity).grid(row=4,column=1)
            self.quantity.set("0")

            self.img=Label(self.frame,text="Image of the item",bg=c1[0]).grid(row=5,column=0)
            self.imgadd=StringVar()
            self.image=Entry(self.frame,text="Image location",bg="white",textvariable=self.imgadd)
            self.image.grid(row=5,column=1)
            

            self.add=Button(self.frame,bg=c1[0],text="MODIFY ITEM",command=self.modify).grid(row=10,column=0)#Button to add items to the text file

            self.back=Button(self.frame,bg=c1[0],text="Back",command=self.backbutton)
            self.back.grid(row=10,column=2)
      def modify(self):
            
            flag=0
            self.nameofvar1=self.name.get()
            self.hello1,self.hello2=1,1
            checkvariable=0
            imgadd1=self.image.get()
            try:
                  self.pri=self.pricee.get()
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
                  self.quantv1=self.quantity.get()
            except ValueError:
                  box.showerror("ERROR 101","Invalid integer for quantity")
                  self.deletefunc()
                  self.hello2=0
                  
            if self.hello1!=0 and self.hello2!=0 and checkvariable!=1:
                  name=self.nameofseller+".txt"
                  f=open(name,"r")
                  g=open("temp.txt","w")                
                  str1=" "
                  flag=0
                  while str1:
                        str1=f.readline()
                        a=str1.split(":")
                        self.nameofvar1=self.changefunc(self.nameofvar1)
                        a1=self.changefunc(a[0])
                        if self.nameofvar1==a1:
                              final=str(self.nameofvar1)+":"+str(self.pri)+":"+str(self.quantv1)+":"+str(imgadd1)
                              g.write(final+'\n')
                              self.deletefunc()
                              flag=1
                        else:
                              g.write(str1+"\n")
                  else:
                        if flag!=1:
                              box.showerror("Name","Name of item does not exist")
            f.close()
            g.close()
            os.remove(name)
            os.rename("temp.txt",name)
      def changefunc(self,st):
            st=st.strip()
            st=st.lower()
            str=st.split(" ")
            st=''
            for i in str:
                  st=st+i
            return st
      def deletefunc(self):                              #Function to reset all values to the original ones
            self.name.delete(0,END)
            self.pricee.set("0")
            self.quantity.set("0")
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
            name="Hello"+" "+v
            menubar.add_cascade(label=name,menu=display)

            master.config(menu=menubar)

#--------------Mainsection---------
c1=['white','#C92D22','#16776A','#1EBBA6']

