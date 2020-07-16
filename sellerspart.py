from tkinter import *
from tkinter import tix
import os
import additems
import modifyitems
import deleteitem
class execute:
      def __init__(self,master,name):
            global c1
            self.master=master
            self.master.configure(bg="#44B3C2")
            self.centerWindow()
            self.frame1=Frame(master,bg="#44B3C2")
            self.frame1.configure(height=500,width=500)
            self.frame1.pack()
            
            self.nameofseller=name
            self.display=Label(self.frame1,text="What do you want to do today?",font=("AvantageSmall",18),bg="#44B3C2")
            self.display.place(x=40,y=60)
            self.add=Button(self.frame1,text="ADD ITEMS",command=self.setvariable,borderwidth=0,bg="white",font=("Avante",15))
            self.modify=Button(self.frame1,text="MODIFY ITEMS",command=self.setmodify,borderwidth=0,bg="white",font=("Avante",15))
            self.delete=Button(self.frame1,text="DELETE ITEMS",command=self.delete,borderwidth=0,bg="white",font=("Avante",15))
            self.add.place(x=93,y=120)
            self.add.configure(height=1,width=27)
            self.modify.place(x=93,y=170)
            self.modify.configure(height=1,width=27)
            self.delete.place(x=93,y=220)
            self.delete.configure(width=27)
      def setvariable(self):
            self.frame1.destroy()
            self.master.configure(bg=c1[0])
            frame=Frame(self.master,bg=c1[0])
            frame.pack()
            hello=self.nameofseller
            s=additems.pulldownmenu(self.master,hello)
            p=additems.nameofitem(self.master,frame,hello)

      def centerWindow(self):     # Function to center window
            sw = self.master.winfo_screenwidth()
            sh = self.master.winfo_screenheight()

            x = (sw - 490)/2
            y = (sh - 550)/2
                  
            self.master.geometry("%dx%d+%d+%d" %(600,500,x,y))     
      def setmodify(self):
            self.frame1.destroy()
            self.master.configure(bg=c1[0 ])
            frame=Frame(self.master,bg=c1[0])
            frame.pack()
            s=modifyitems.pulldownmenu(self.master,self.nameofseller)
            p=modifyitems.nameofitem(self.master,frame,self.nameofseller)
      def delete(self):
            self.frame1.destroy()
            self.master.configure(bg=c1[0 ])
            frame=Frame(self.master,bg=c1[0])
            frame.pack()
            s=deleteitem.pulldownmenu(self.master,self.nameofseller)
            p=deleteitem.nameofitem(self.master,frame,self.nameofseller)
c1=['white','#C92D22','#16776A','#1EBBA6']
