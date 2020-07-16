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
            self.frame.configure(height=150,width=150)
            self.frame.pack()
            
            self.namel=Label(self.frame,text="NAME OF ITEM",bg=c1[0]).grid(row=0,column=0)
            self.nameofvar1=StringVar()
            self.name=Entry(self.frame,fg="black",bg="white",text="name of item",textvariable=self.nameofvar1)
            self.name.grid(row=0,column=1)

            self.add=Button(self.frame,bg=c1[0],text="DELETE ITEM",command=self.delete).grid(row=10,column=0)#Button to add items to the text file

            self.back=Button(self.frame,bg=c1[0],text="Back",command=self.backbutton).grid(row=14,column=7)
      def delete(self):
            
            flag=0
            self.nameofvar1=self.name.get()
                  
            
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
                        pass
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

