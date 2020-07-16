#-----MODULES-----#
from tkinter import *
from tkinter import messagebox as box
from PIL import ImageTk, Image
import os
import pickle
from tkinter import tix
#-----CLASSES-----#

class frame_title(Frame):  #Frame class
    
    def __init__(self,parent):
        frame=Frame(parent)
        frame.pack()
                           
class login_frame(frame_title):  #The Login Frame
    
    def __init__(self,parent):
        
        frame_title.__init__(self,parent)
        self.parent = parent
        self.parent.title("ASK SHOPPERS  |  2016-2017")
        
        self.parent.configure(background='black')
        self.centerWindow()

        self.frame=Frame(parent)
        self.frame.configure(height=600,width=600,bg='black')
        self.frame.pack()
        
        self.login_label=Label(self.frame, text='LOGIN SCREEN', font=('Avantagesmall',50), fg='white', background='black')
        self.login_label.place(x=90,y=100)

        self.user_label=Label(self.frame, text="Enter/Choose your username: ",  font=('Avantagesmall', 13), fg='white', background='black', width=30)
        self.user_label.place(x=0,y=190)

        self.pass_label=Label(self.frame, text="Enter/Choose your password: ",  font=('Avantagesmall', 13), fg='white', background='black', width=30)
        self.pass_label.place(x=0,y=270)

        self.entry_user = Entry(self.frame, width = 25, font=("Avantagesmall", 13),background='white',fg='black')
        self.entry_user.place(x=300, y=190)
        
        self.entry_pass = Entry(self.frame, width = 25, font=("Avantagesmall", 13),background='white',fg='black',)
        self.entry_pass.place(x=300, y=270)

        self.login = Button(self.frame, text="Log In", font=('Avantagesmall', 12),command=self.login, background='white', fg='black', height=1, width=10)
        self.login.place(x= 170, y = 339)

        self.signup = Button(self.frame, text="Sign Up", font=('Avantagesmall', 12), command=self.signup, background='white', fg='black', height=1, width=10)
        self.signup.place(x= 330, y =340)

        self.quit = Button(self.frame, text="Quit", font=('Avantagesmall', 18), command=self.quit, background='white', fg='black', height=1, width=5)
        self.quit.place(x= 480, y = 425)

    def centerWindow(self):     # Function to center window
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - 490)/2
        y = (sh - 550)/2
            
        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        
    def quit(self):
        self.parent.destroy()

    def login(self):
        global a
        self.username=self.entry_user.get().lower()
        self.password=self.entry_pass.get()
        f=open('customeruser.dat','rb')
        try:
            while True:
                a=pickle.load(f)
                self.usernames=a.keys()
                if len(self.usernames)==1:
                    self.entry_pass.delete(0,'end')
        except EOFError:
            pass
        if self.password=='':
            box.showerror('ERROR','Please enter a password before trying to login')
        else:
            if self.username.strip() not in self.usernames:
                box.showerror('ERROR',"That username wasn't found in our directory.\nPlease sign up first")
        if self.username.strip() in self.usernames:
            if self.password==a[self.username.strip()]:
                self.frame.destroy()
                root.configure(bg="darkblue")
                
                import searchfunction
                s=searchfunction.searchbar(root,self.username.strip())
            else:
                box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid details')
                self.entry_pass.delete(0,'end')

    def signup(self):
        global a
        self.username=self.entry_user.get().lower()
        self.password=self.entry_pass.get()
        f=open('customeruser.dat','rb')
        self.collection=dict()
        try:
            while True:
                self.collection=pickle.load(f)
                self.usernames=self.collection.keys()
        except EOFError:
            pass
        f.close()
        if len(self.password.strip())==0:
                box.showerror('ERROR','Please enter a password') 
        else:
            if self.username.strip() in self.usernames:
                box.showerror('ERROR','The entered username has already been taken.\nPlease enter another one')
                self.entry_pass.delete(0,'end')
                self.entry_user.delete(0,'end')
            else:
                self.collection[self.username.strip()]=self.password
                f=open('customeruser.dat','wb')
                pickle.dump(self.collection,f)
                f.close()
                box.showinfo('Success','Your details have been saved.')
                self.userdata='Username: '+self.username.strip()+'\nPassword: '+self.password
                box.showinfo('Your details',self.userdata)
                

#-----MAIN_SECTION-----#

#----MAKING THE USERNAME/PASSWORD FILE-----#
f=open('customeruser.dat','ab').close()                        #Creating a file, if its doesn't exist.
f=open('customeruser.dat','rb')
a=dict()
try:
    while True:
        a=pickle.load(f)
except EOFError:
    pass
if type(a)==dict:
    pass
else:
    a=dict()

f.close()
f=open('customeruser.dat','wb')
pickle.dump(a,f)
f.close()


root = tix.Tk( )
b=frame_title(root)
c=login_frame(root)
root.mainloop( )

#-----MAIN_SECTION-----#
