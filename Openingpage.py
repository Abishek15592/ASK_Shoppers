from tkinter import *
from tkinter import tix
import os
root=tix.Tk()
def customer():
      os.system('customerpart.py')
      root.destroy()
def seller():
      os.system('CompProject.py')
      root.destroy()
      #root.configure(bg="white")

def custom(parent):
      #Custom#
      hello=parent
        
      selftimeframe=parent
      canvas=Canvas(selftimeframe,height=900,width=600,background='white')
      canvas.place(x=110,y=0)

      tm=Label(selftimeframe,text='TM',font=('Avantagesmall',10),bg='white')
      tm.place(x=290,y=28)
                
      ask=Label(selftimeframe,text='A S K',font=('Avantagesmall',60),bg='white')
      ask.place(x=190,y=15)
                
      shoppers=Label(selftimeframe,text='S     H     O     P     P     E     R     S ', font=('Avantagesmall',8),bg='white')
      shoppers.place(x=188,y=110)
      tagline=Label(selftimeframe,text="Shop", font=('Avantagesmall',30),bg='white')
      tagline.place(x=188,y=140)

      tagline2=Label(selftimeframe,text="the",font=('Avantagesmall',20),bg='white')
      tagline2.place(x=188,y=190)

      tagline3=Label(selftimeframe,text="Desire", font=('Avantagesmall',60),bg='white')
      tagline3.place(x=188,y=218)

      global customer
      global seller
      
      customer1=Button(parent,text="Customer",command=customer,borderwidth=0,font=('Cloud Light',20),bg='white',relief='sunken',underline=True).place(x=220,y=300)
      seller1=Button(parent,text="Seller",command=seller,borderwidth=0,font=('Cloud Light',20),bg='white',relief='sunken',underline=True).place(x=240,y=350)
def centerWindow():     # Function to center window
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - 490)/2
        y = (sh - 550)/2
            
        root.geometry("%dx%d+%d+%d" %(600,500,x,y))
        
centerWindow()

custom(root) 

root.mainloop()
      
