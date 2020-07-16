
#-----MODULES-----#

from tkinter import *
from tkinter import messagebox as box
from tkinter import font as tkfont
import os
import random
import pickle
from tkinter import tix
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

#-----CLASSES-----#
                

class payment:
    
    def __init__(self,master,name):
        self.parent= master
        self.parent1 = master
        self.parent.geometry("{0}x{1}+0+0".format(self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()))
        self.parent.configure(background='black')

        self.parent2=Frame(self.parent,height=2000,width=2000)
        self.parent2.configure(background="black")
        self.parent2.pack()

        self.parent3=Frame(self.parent)
        self.parent4=Frame(self.parent)
        self.parent5=Frame(self.parent)
        self.parent6=Frame(self.parent)
        
        self.cart=Label(self.parent2, text='CART', font=('AvantageSmall',48), fg='white' , bg='black')
        self.cart.place(x=50,y=30)

        self.custom(self.parent2)

        f = tkfont.Font(self.tagline2, self.tagline2.cget("font"))        
        f.configure(underline = True)

        
        self.itemname=Label(self.parent2, text="Item Name",  font=("AvantageSmall", 20),fg='white',bg='black')
        self.itemname.place(x=55,y=150)
        self.itemname.configure(font=f)

        self.quantity=Label(self.parent2, text="Quantity",  font=("AvantageSmall", 20),fg='white',bg='black')
        self.quantity.place(x=470,y=150)
        self.quantity.configure(font=f)

        self.price=Label(self.parent2, text="Price",  font=("AvantageSmall", 20),fg='white',bg='black')
        self.price.place(x=855,y=150)
        self.price.configure(font=f)


        self.name=name+'.dat'
        f=open(self.name,'rb')
        y=200
        self.total=0
        self.details=[]
        i=0
        try:
            while True:
                str=pickle.load(f)
                i=i+1
        except EOFError:
            f.close()
        n=0
        f=open(self.name,'rb')
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',password='ooehs',charset='utf8')
            mycursor=mydb.cursor()

            mycursor.execute("create database if not exists userdb")
            mycursor.execute("use userdb")

            mycursor.execute("create table if not exists %s (S_no integer,Item_name varchar(20),quantity integer,price integer)"%name)
            
            
            while n<=i:
                str=pickle.load(f)
                print (str)
                i=i+1
                str.strip('\n')
                nameofitems=str.split(":")
##                mycursor.execute("insert into {} values{}"%name,(i,nameofitems[0],nameofitems[2],nameofitems[1]))
                mycursor.execute("insert into {} values({},'{}','{}','{}')".format(name,i,nameofitems[0],nameofitems[2],nameofitems[1]))
                mycursor.execute("select * from %s"%name)
                for j in mycursor:
                    print (j)
                mydb.commit()
                self.item=Label(self.parent2, text=nameofitems[0],  font=("Avantagesmall", 15),fg='white',bg='black')
                self.item.place(x=55,y=y)
                self.details.append(self.item)
                self.quantity=Label(self.parent2, text=nameofitems[2],  font=("Avantagesmall", 15),fg='white',bg='black')
                self.quantity.place(x=470,y=y)
                self.price=Label(self.parent2, text=nameofitems[1],  font=("Avantagesmall", 15),fg='white',bg='black')
                self.price.place(x=855,y=y)
                self.delete=Button(self.parent2,text="Delete",font=("Avantagesmall", 15),fg='white',bg='black',command=lambda n=n:self.delete1(n),textvariable=n)
                self.delete.place(x=900,y=y)
                
                self.total+=int(nameofitems[1])*int(nameofitems[2])
                y=y+50
                f2 = tkfont.Font(self.item, self.item.cget("font"))
                f2.configure(underline=True)
                n=n+1
        except EOFError:
            f.close()

        self.blankline=Label(self.parent2, text="                        ",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.blankline.place(x=780,y=575)
        self.blankline.configure(font=f2)

        self.blankline2=Label(self.parent2, text="                        ",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.blankline2.place(x=780,y=625)
        self.blankline2.configure(font=f2)
        
        self.tprice=Label(self.parent2, text=self.total,  font=("AvantageSmall", 15),fg='white',bg='black')
        self.tprice.place(x=855,y=610)

        self.tprice=Label(self.parent2, text="TOTAL",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.tprice.place(x=785,y=610)

        self.colon=Label(self.parent2, text=": ", font=("Century Gothic",15),fg='white',bg='black')
        self.colon.place(x=840,y=607)

        self.payment=Button(self.parent2, text="Payment",  font=("AvantageSmall", 15),fg='white',bg='black',command=self.paymentoptions,width=35,border=0)
        self.payment.place(x=1010,y=528)
    def delete1(self,i):
        f=open(self.name,'rb')
        g=open('temp.dat','ab')
        print (i)
        i1=0
        print (self.details)
        try:
            while True:
                str=pickle.load(f)
                str1=str.strip('\n')
                detail=str1.split(":")
                if i1==i:
                    self.details[i].destroy()
                else:
                    pickle.dump(str,g)
                i1=i1+1
        except EOFError:
            f.close()
            g.close()
        os.remove(self.name)
        os.rename('temp.dat',self.name)
        print(self.name)
        n=self.name.split('.')      
        payment.__init__(self,self.parent,n[0])
                
        #_______________________________#

    

    def paymentoptions(self):
        self.parent2.destroy()
        self.parent4.destroy()
        self.parent5.destroy()
        self.parent6.destroy()
        
        self.parent3 = Frame(self.parent,height=2000,width=2000,bg="black")
        self.parent.configure(background="black")
        self.parent3.pack()
        


        
        self.cname = Label(self.parent3, text="CUSTOMER NAME*", font=("AvantageSmall", 15),fg='white',bg='black')
        self.cname.place(x=50,y=128)   

                    
                       
        self.address = Label(self.parent3, text="EMAIL-ID*", font=("AvantageSmall", 15),fg='white',bg='black')
        self.address.place(x=50,y=228)

        self.emirate = Label(self.parent3, text="ADDRESS*", font=("AvantageSmall", 15),fg='white',bg='black')
        self.emirate.place(x=50,y=328)

        self.pobox=Label(self.parent3, text="STATE*", font=("AvantageSmall", 15),fg='white',bg='black')
        self.pobox.place(x=50,y=428)

        self.telno=Label(self.parent3, text="TEL NO", font=("AvantageSmall", 15),fg='white',bg='black')
        self.telno.place(x=50,y=528)

        self.paymentmode = Label(self.parent3, text="MODE OF PAYMENT*", font=("AvantageSmall", 15),fg='white',bg='black')
        self.paymentmode.place(x=50,y=628)
        
        self.cnamevariable=StringVar()
        self.cnameentry=Entry(self.parent3,font=('AvantageSmall',15),fg='black',bg='white',width=55,textvariable=self.cnamevariable)
        self.cnameentry.place(x=300,y=128)
        self.cnamevariable.set(self.name.strip('.dat'))
        
        self.addressval=StringVar()
        self.addressentry=Entry(self.parent3,font=('AvantageSmall',15),fg='black',bg='white',width=55,textvariable=self.addressval)
        self.addressentry.place(x=300,y=228)
        
        self.addressmain=StringVar()
        self.addressentry2=Entry(self.parent3,font=('AvantageSmall',15),fg='black',bg='white',width=55,textvariable=self.addressmain)
        self.addressentry2.place(x=300,y=328)

        self.poboxentry=Entry(self.parent3,font=('AvantageSmall',15),fg='black',bg='white',width=55)
        self.poboxentry.place(x=300,y=428)

        self.telnoentry=Entry(self.parent3,font=('AvantageSmall',15),fg='black',bg='white',width=55)
        self.telnoentry.place(x=300,y=528)

        val=self.addressval.get()

        self.mastercard1=Button(self.parent3,font=('AvantageSmall',10),text='MASTERCARD',fg='white',bg='black',border=10,command=lambda:self.mastercard(self.addressval.get(),self.addressmain.get()), width=23)
        self.mastercard1.place(x=300,y=628)

        self.visa1=Button(self.parent3,font=('AvantageSmall',10),text='VISA',fg='white',bg='black',border=10, command=lambda:self.visa(self.addressval.get(),self.addressmain.get()), width=23)
        self.visa1.place(x=510,y=628)

        self.cod1=Button(self.parent3,font=('AvantageSmall',10),text='CASH ON DELIVERY',fg='white',bg='black',border=10,command=lambda:self.cod(self.addressval.get(),self.addressmain.get()),width=23)
        self.cod1.place(x=720,y=628)

        self.note=Label(self.parent3,font=('AvantageSmall',12),text='* Fields are mandatory',fg='white',bg='black')
        self.note.place(x=730,y=710)
        
        self.custom(self.parent3)

        

        self.safety=Label(self.parent3,text="ALL TRANSACTIONS ARE SECURED VIA PAYPAL", font=('AvantageSmall',10), bg='white',width=40)
        self.safety.place(x=1060,y=710)




    def mastercard(self,email,name):
        print (name)
        self.parent3.destroy()
        self.parent4 = Frame(self.parent,height=2000,width=2000,bg="black")
        self.parent4.pack()

        self.nameofholder=Label(self.parent4, text="NAME OF CARD HOLDER",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.nameofholder.place(x=175,y=200)
        
        self.cardno=Label(self.parent4, text="CARD NUMBER ",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.cardno.place(x=175,y=300)

        self.date=Label(self.parent4, text="EXPIRY(MM/YY)",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.date.place(x=175,y=400)

        self.nameentry= Entry(self.parent4, font=("AvantageSmall", 15),fg='black',bg='white')
        self.nameentry.place(x=575, y=200)

        self.cardnumber=StringVar()
        self.cardnoentry = Entry(self.parent4, font=("AvantageSmall", 15),fg='black',bg='white',textvariable=self.cardnumber)
        self.cardnoentry.place(x=575,y=300)
        self.cardnumber.set('123456784567')
        
        self.dateentry = Entry(self.parent4, font=("AvantageSmall", 15),fg='black',bg='white')
        self.dateentry.place(x=575,y=400)         

        self.pay = Button(self.parent4, text="PAY", font=("AvantageSmall", 20),fg='white',bg='black',width=14,border=10,command=lambda: self.bill(email,name,self.cardnumber.get()))
        self.pay.place(x=575,y=500)

        self.custom(self.parent4)


        self.safety=Label(self.parent4,text="ALL TRANSACTIONS ARE SECURED VIA PAYPAL", font=('AvantageSmall',10), bg='white',width=40)
        self.safety.place(x=1060,y=710)

    def visa(self,email,name):
        self.parent3.destroy()
        self.parent5 = Frame(self.parent,height=2000,width=2000,bg="black")
        self.parent5.pack()

        

        self.nameofcard=Label(self.parent5, text="NAME OF CARD HOLDER",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.nameofcard.place(x=175,y=200)
        
        self.cardno=Label(self.parent5, text="CARD NUMBER ",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.cardno.place(x=175,y=300)

        self.date=Label(self.parent5, text="EXPIRY(MM/YY)",  font=("AvantageSmall", 15),fg='white',bg='black')
        self.date.place(x=175,y=400)

        self.nameentry= Entry(self.parent5, font=("AvantageSmall", 15),fg='black',bg='white')
        self.nameentry.place(x=575, y=200)
        
        self.cardnumber=StringVar()
        self.cardnoentry = Entry(self.parent5, font=("AvantageSmall", 15),fg='black',bg='white',textvariable=self.cardnumber)
        self.cardnoentry.place(x=575,y=300)
        self.cardnumber.set('1234567891024123')
        
        self.dateentry = Entry(self.parent5, font=("AvantageSmall", 15),fg='black',bg='white')
        self.dateentry.place(x=575,y=400)         

        self.pay = Button(self.parent5, text="PAY", font=("AvantageSmall", 20),fg='white',bg='black',width=14,border=10,command=lambda:self.bill(email,name,self.cardnumber.get()))
        self.pay.place(x=575,y=500)

        self.custom(self.parent5)



        self.safety=Label(self.parent5,text="ALL TRANSACTIONS ARE SECURED VIA PAYPAL", font=('AvantageSmall',10), bg='white',width=40)
        self.safety.place(x=1060,y=710)


    def cod(self,email,name):

        self.parent3.destroy()
        self.parent6 = Frame(self.parent,height=2000,width=2000,bg='black')
        self.parent6.pack()
        
        
        self.custom(self.parent6)


        self.safety=Label(self.parent6,text="ALL TRANSACTIONS ARE SECURED VIA PAYPAL", font=('AvantageSmall',10), bg='white',width=40)
        self.safety.place(x=1060,y=710)

        self.codcharge=Label(self.parent6,text="An additional amount of INR 40 will be charged for item(s) purchased via COD",font=('Avantagesmall',15),bg='black',fg='white')
        self.codcharge.place(x=150,y=300)

        self.total+=20

        self.pay=Button(self.parent6,text="PAY",font=('Avantagesmall',30),bg='black',fg='white',border=10,command=lambda:self.codbill(email,name))
        self.pay.place(x=480,y=400)

    def codbill(self,email,add):
        try:
            
            
            msg = MIMEMultipart()
            msg['From'] = 'shoppersask@gmail.com'
            msg['To'] = email
            msg['Subject'] = 'Thank You'
            message = 'Thank you for purchasing at ASK Shoppers.======== ========= \n Price of purchase:'+str(self.total)+'\n'+"======== ======="
            msg.attach(MIMEText(message))

            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
            mailserver.login('shoppersask@gmail.com', 'computerproject')

            mailserver.sendmail("shoppersask@gmail.com",email,msg.as_string())

            mailserver.quit()
        except  smtplib.SMTPRecipientsRefused:
            box.showerror("INVALID EMAIL-ID","Enter a valid email id")
            self.paymentoptions()
        else:
            root2=tix.Tk()
            root2.configure(bg="black",height=500,width=500)
            ordeidgen=random.randrange(12589010,15768593)
            self.nameshow=Label(root2,text="Name",font=("AvantageSmall",20)).place(x=0,y=20)
            self.namestuff=Label(root2,text=self.name.strip('.dat'),font=("AvantageSmall",20)).place(x=100,y=20)
            self.emailaddress=Label(root2,text="Email ID",font=("AvantageSmall",20)).place(x=0,y=50)
            self.eaddress=Label(root2,text=email,font=("AvantageSmall",20)).place(x=100,y=50)
            self.actualaddress=Label(root2,text="Address",font=("AvantageSmall",20)).place(x=0,y=80)
            self.actualaddres1=Label(root2,text=add,font=("AvantageSmall",20)).place(x=100,y=80)
            self.amt=Label(root2,text="Total",font=("AvantageSmall",20)).place(x=0,y=110)
            self.total1=Label(root2,text=self.total,font=("AvantageSmall",20)).place(x=100,y=110)
            self.total=0

    def bill(self,email,add,cardnumber='1234567890123456'):
        
        try:
            a=int(cardnumber)
            msg = MIMEMultipart()
            msg['From'] = 'shoppersask@gmail.com'
            msg['To'] = email
            msg['Subject'] = 'Thank You'
            message = 'Thank you for purchasing at ASK Shoppers.======== ========= \n Price of purchase:'+str(self.total)+'\n'+"======== ======="
            msg.attach(MIMEText(message))

            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
            mailserver.login('shoppersask@gmail.com', 'computerproject')

            mailserver.sendmail("shoppersask@gmail.com",email,msg.as_string())

            mailserver.quit()

        except ValueError:
            box.showerror("Re-enter","Invalid card number")
            self.paymentoptions()
        except  smtplib.SMTPRecipientsRefused:
            box.showerror("INVALID EMAIL-ID","Enter a valid email id")
            self.paymentoptions()
        else:
            root2=tix.Tk()
            root2.configure(bg="black",height=500,width=500)
            ordeidgen=random.randrange(12589010,15768593)
            self.nameshow=Label(root2,text="Name",font=("AvantageSmall",20)).place(x=0,y=20)
            self.namestuff=Label(root2,text=self.name.strip('.dat'),font=("AvantageSmall",20)).place(x=100,y=20)
            self.emailaddress=Label(root2,text="Email ID",font=("AvantageSmall",20)).place(x=0,y=50)
            self.eaddress=Label(root2,text=email,font=("AvantageSmall",20)).place(x=100,y=50)
            self.actualaddress=Label(root2,text="Address",font=("AvantageSmall",20)).place(x=0,y=80)
            self.actualaddres1=Label(root2,text=add,font=("AvantageSmall",20)).place(x=100,y=80)
            self.amt=Label(root2,text="Total",font=("AvantageSmall",20)).place(x=0,y=110)
            self.total1=Label(root2,text=self.total,font=("AvantageSmall",20)).place(x=100,y=110)
            self.total=0

    def custom(self,parent):
        #Custom#
        self.hello=parent
        
        canvas=Canvas(self.hello,height=900,width=500,background='white')
        canvas.place(x=1010,y=0)

        self.tm=Label(self.hello,text='TM',font=('AvantageSmall',10),bg='white')
        self.tm.place(x=1290,y=28)
        
        self.ask=Label(self.hello,text='A S K',font=('AvantageSmall',60),bg='white')
        self.ask.place(x=1090,y=15)
        
        self.shoppers=Label(self.hello,text='S     H     O     P     P     E     R     S ', font=('AvantageSmall',8),bg='white')
        self.shoppers.place(x=1088,y=110)

        self.tagline=Label(self.hello,text="Shop", font=('AvantageSmall',30),bg='white')
        self.tagline.place(x=1088,y=240)

        self.tagline2=Label(self.hello,text="the",font=('AvantageSmall',20),bg='white')
        self.tagline2.place(x=1088,y=290)

        self.tagline3=Label(self.hello,text="Desire", font=('AvantageSmall',60),bg='white')
        self.tagline3.place(x=1088,y=318)

    
 

