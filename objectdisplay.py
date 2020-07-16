#------Modules-------
from tkinter import *
from PIL import ImageTk, Image
from tkinter import tix
import pickle
from tkinter import messagebox as box
import string
import Payment
#-----Class------------
class objectheader:
      def __init__(self,master,v):   #First I need to change the colour of the background 
            self.frame=master
            self.frame.configure(bg='black')
            global c1
            self.name=v
            #Creating the header for the objects name
            self.label1=Label(self.frame,text=v,bg='black',font="AvantageSmall",fg='white')
            self.label1.place(x=0,y=150)
            self.label1.pack()
      def returnname(self):
            return self.name

class objectimage:
      def __init__(self,master,imagename):
            #Placing the image of the object
            self.frame=master
            self.imagelocation=imagename
            global c1
            self.frame.configure(bg='black')
            self.img = ImageTk.PhotoImage(Image.open(imagename))                              #Displaying the image of the object
            self.imglabel = Button(self.frame,image=self.img,height=200,highlightbackground=c1[3],width=200,relief=SUNKEN,borderwidth=0,command=self.newwindow)
            self.imglabel.place(x=0,y=300)
            self.imglabel.pack()                                                                           
      def newwindow(self):
            self.imagewindow=Toplevel(self.frame)
            self.image=imagezoom(self.imagewindow,self.imagelocation)
class imagezoom(objectimage):                                                                                                                                            #Window where the image in the zoomed form is visible
      def __init__(self,master,image):
            self.frame=Frame(master,height=200,width=100)
            self.img = ImageTk.PhotoImage(Image.open(image))
            self.imglabel = Label(master, image=self.img).grid(row=0,column=0)
class priceandquantity:
      def __init__(self,master,price,quantity):                                                                              #Displaying the price and quantity
            self.frame=master
            self.frame.configure(bg="black")
            global c1
            self.price=price
            self.quantity=quantity
            self.frame.configure(height=100,width=100,padx=10,pady=10,bg='black')
            self.pricelabel=Label(self.frame,text='PRICE:',font="AvantageSmall",bg="black",fg="white",width=20).grid(row=0,column=0)
            self.quantlabel=Label(self.frame,text='QUANTITY:',font="AvantageSmall",bg="black",fg="white",width=20).grid(row=1,column=0)
            self.price=Label(self.frame,text=price,bg="black",font="AvantageSmall",fg="white").grid(row=0,column=1)
            self.quant=Scale(self.frame,from_=0,to=int(quantity),bg="white")
            self.quant.grid(row=1,column=1)
class cart(priceandquantity):                                                                         #The class where the items are added to the cart
      def __init__(self,mainmaster,tkwindow,master,v,n,img,pri,quant):
            self.cart=Button(master,text="VIEW CART",command=self.cart,width=20,height=2,font="AvantageSmall",bg="white")
            self.cart.grid(row=20,column=0)
            priceandquantity.__init__(self,master,pri,quant)
            self.mainmaster=mainmaster
            mainmaster.configure(bg="black")
            self.tk=tkwindow
            self.master=master
            self.nameofcustomer=v
            m=[n,pri,img]
            self.cartbutton=Button(master,text='ADD TO CART',bg="white",width=20,height=2,font="AvantageSmall",command=lambda: self.additems(m))
            self.cartbutton.grid(row=14,column=0)


            self.backbutton=Button(master,text='BACK TO SHOPPING',bg="white",width=20,height=2,font="AvantageSmall",command=lambda: self.back(self.tk,v))
            self.backbutton.grid(row=26,column=0)

      def back(self,root,v):
            
            import searchfunction
            self.parent = root
            self.mainmaster.destroy()
            self.parent.configure(background='black')
            s=searchfunction.searchbar(root,v)
            
      def additems(self,l):
            quantity=self.quant.get()
            nameofile=self.nameofcustomer+".dat"
            name2=str(l[0]).strip()+":"+str(l[1]).strip()+":"+str(quantity).strip()
            f=open(nameofile,"ab")
            pickle.dump(name2,f)
            f.close()
            box.showinfo("Cart","Added Item to cart")
      def cart(self):
            self.mainmaster.destroy()

            p=Payment.payment(self.tk,self.nameofcustomer)
            
            
            
class pulldownmenu:
      def __init__(self,master,v):
            menubar=Menu(master)

            #Creating a display of the sellers name
            display=Menu(menubar,tearoff=0)
            display.add_command(label="Go to cart")
            name="Hello"+" "+v
            menubar.add_cascade(label=name,menu=display)
            master.config(menu=menubar)

#---------------Mainsection----------------------
c1=['white','#C92D22','#16776A','#1EBBA6']
