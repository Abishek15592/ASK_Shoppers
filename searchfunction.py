#Search Function
#---------------Modules------------------
from tkinter import *
from tkinter import tix
import string
import pickle
import objectdisplay
from tkinter import font as font
from tkinter import messagebox as box
import random
#--------------Class-----------------------
class todaydeal:
      def __init__(self,master,v):
            f=open("Productsdata.dat","rb")
            l=pickle.load(f)
            self.framet=master
            self.deal=Label(self.framet,text="Today's Deal",font=('AvantageSmall','18'),bg='black',fg='white')
            self.deal.place(x=200,y=200)
            self.deal.pack(side=TOP)
            #self.item=Label(self.framet,text=random.choice("1"),font=('AvantageSmall','18'),bg='black',fg='white')
            #self.item.place(x=400,y=400)
            #self.item.pack(side=BOTTOM)
            f.close()
class searchbar(todaydeal):
      def __init__(self,master,v):
            global c1

            self.nameofcustomer=v
            self.st=''
            self.root=master
            self.root.configure(bg='black')
            self.frame=Frame(master,height=1000,width=1000,bg='black')
            self.frame.pack()

            self.today=Frame(master,height=600,width=600,bg='black')
            self.today.pack(side=TOP)

            todaydeal.__init__(self,self.today,v)

            search=StringVar()
            self.entry=Entry(self.frame,textvariable=search,bg="white",width=71,font=('AvantageSmall','10'))
            self.entry.place(x=700,y=700)
            self.entry.pack()
            search.set("What are you looking for?")

            self.frame1=Frame(self.frame)                                     #Sample Frame on top of which another frame is made so that the products are displayed under the search bar
            self.frame1.pack(side=TOP)

            self.frame2=Frame(self.frame1)                              #Frame where the name of the products are displayed
            self.frame2.pack(side=TOP)
            
            self.entry.bind("<Button-1>",self.clear)
            self.entry.bind("<Key>",self.hello)
      def hello(self,event):
            i2=0
            self.i=0
            self.searchitem=self.entry.get()
            self.frame2.destroy()

            self.frame2=Frame(self.frame1)                                #Each time the person enters a letter this function is called the frame where the names are displayed is deleted so that the new names can be displayed
            self.frame2.pack(side=TOP)
   
            #f=open("Productsdata.dat","rb")
            g=open("seller.txt","r")
            list1=g.readlines()
            list2 = []
            for i in range(0,len(list1)):
                  x=list1[i].split(":")
                  list2.append(x[0])

            #l=pickle.load(f)
            variable=1
            if self.searchitem!='':
                  for i in list2:
                        i1=self.change(i)                                                #Function to convert the variable into a lower case variable with no spaces so that all the variables have the familiar type
                        self.searchitem=self.change(self.searchitem)
                        if len(i1)>=len(self.searchitem):                         #Checking first if the length of the entered variable is less than the name of the existing variable
                              mnum=len(self.searchitem)
                              if i1[0:mnum]==self.searchitem:
                                    self.st=i
                                    self.display1=Button(self.frame2,width=70,height=2,bg='white',text=i,command=lambda m=i :self.open1(m),borderwidth=0,relief="sunken",textvariable=i1).pack(side=BOTTOM)
                                    variable=0
                                    self.i+=1
                              if variable==1:                                             #If the variable doesnot entirely match with the entered variable then we check if the first letter matches with the variable
                                    if i[0]==self.searchitem[0]:
                                          self.display2=Button(self.frame2,width=70,height=2,bg='white',text=i,relief="sunken",borderwidth=0,command=lambda m=i :self.open1(m)).pack(side=BOTTOM)
                                          self.i+=1
                  else:
                       if self.i==0:
                             self.display3=Button(self.frame2,width=70,height=2,bg='white',text="Product Not Found",relief=SUNKEN,borderwidth=0).pack(side=BOTTOM)
      def open1(self,st):
            self.frame.destroy()                                                    #Deleting all the searchbar frames
            self.frame1.destroy()
            self.frame2.destroy()
            global c1
            str=st
            print (str)
            f=open("Allsellersname.dat","rb")
            check=0
            sellername=' '
            try:                                                                          #Getting the name of the seller of the product
                  while True:
                        str1=pickle.load(f)
                        print (str1)
                        str1=str1+".txt"
                        g=open(str1,"r")
                        str2=' '
                        while str2:                                #Checking if the seller has the product
                              str2=g.readline()
                              hello=str2.split(":")
                              if hello[0]==str:
                                    sellername=str1
                                    check=1                                      #Keeping this variable so that if there is no seller for this product error will be displayed
                                    continue
                        g.close()
            except EOFError:
                  if check==1:
                        pass
                  else:
                        box.showerror("Error","Product Not Found")
                        self.root.destroy()
                  f.close()

            f1=open(sellername,"r")                         #Opening the sellers file to get the full details of the product
            product=' '
            while product:
                  product=f1.readline()
                  productcheck=product.split(":")
                  if productcheck[0].strip()==str:
                        productdetails=productcheck
                        break
            f1.close()
            self.framet.destroy()
            self.root.configure(bg='black')
            self.mainframe=Frame(self.root,bg='black')     #A frame where the objects name price image is being displayed
            self.mainframe.pack()
            print (productdetails)
            self.frame1=Frame(self.mainframe)
            self.frame1.pack(side=LEFT)

            o=objectdisplay.objectheader(self.frame1,str)
            image=productdetails[-1]
            o2=objectdisplay.objectimage(self.frame1,image.strip())

            self.frame2=Frame(self.mainframe)
            self.frame2.pack(side=RIGHT)
            price=productdetails[1]
            quantity=productdetails[2]
            c=objectdisplay.cart(self.mainframe,self.root,self.frame2,self.nameofcustomer,str,image,price,quantity)

            p2=objectdisplay.pulldownmenu(self.root,self.nameofcustomer)
      def change(self,variable):                                                                                                    #Function to convert the variables to a lower case and no space string
            t=variable.split(' ')
            changevariable=''
            for k in t:
                  changevariable+=k
            changevariable=changevariable.lower()
            return changevariable.strip()      
      def clear(self,event):
            self.entry.delete(0,END)
#-------------MainSection---------------
c1=['white','#C92D22','#16776A','#1EBBA6']
