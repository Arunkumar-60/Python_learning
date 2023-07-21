import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages")
from tkinter import *
import tkinter.messagebox as msg
import pymysql
from pymysql import Error

root=Tk()
root.title("Registration Form")
root.geometry("700x700")
root.resizable(0,0)

USER=StringVar()
PASS=StringVar()
NAME=StringVar()
ADDRESS=StringVar()


def database():
    global conn,cursor 
    conn=pymysql.connect(host="localhost",user="root",\
                         password="root",database="inspannerdb")
    cursor=conn.cursor()


def Register():
    database()
    if USER.get()== "" or PASS.get=="" or NAME.get()=="" or ADDRESS.get()=="":
        l6.config(text="please fill the required field",fg="orange")
        
    else:
        cursor.execute("select * from user1 where user = %s",\
                       [USER.get()])
        if cursor.fetchone() is not None:
            l6.config(text="UserName is already stored",fg="red")
        else:
            cursor.execute("insert into user1 (user,pass,name,address) values (%s,%s,%s,%s)",\
                           (str(USER.get()),str(PASS.get()),str(NAME.get()),\
                            str(ADDRESS.get())))
            conn.commit()
            USER.set("")
            PASS.set("")
            NAME.set("")
            l6.config(text="Successfully created")
        cursor.close()
        conn.close()


def Exit(): 
    result=msg.askquestion('System','want to Exit ??',icon="warning")
    if result=='yes':
        root.destroy()
        exit()

tf=Frame(root,height=100,width=640,bd=1,relief=SOLID)
tf.pack(side=TOP)

rf=Frame(root)
rf.pack(side=TOP,pady=20)

l1=Label(tf,text="Register Form",font=('arial',18),bd=1,width=640)
l1.pack()

l2=Label(rf,text="UserName",font=('arial',18),bd=18)
l2.grid(row=1)

l3=Label(rf,text="Password",font=('arial',18),bd=18)
l3.grid(row=2)

l4=Label(rf,text="Name",font=('arial',18),bd=18)
l4.grid(row=3)

l5=Label(rf,text="Address",font=('arial',18),bd=18)
l5.grid(row=4)

l6=Label(rf,text="",font=('arial',18))
l6.grid(row=5,columnspan=2)

user=Entry(rf,font=('arial',20),textvariable=USER,width=15)
user.grid(row=1,column=1)

pass1=Entry(rf,font=('arial',20),textvariable=PASS,\
            width=15,show="*")
pass1.grid(row=2,column=1)

name=Entry(rf,font=('arial',20),textvariable=NAME,width=15)
name.grid(row=3,column=1)

address=Entry(rf,font=('arial',20),textvariable=ADDRESS,width=15)
address.grid(row=4,column=1)

btn=Button(rf,font=('arial',20),text="Register",command=Register)
btn.grid(row=6,columnspan=2)

menubar=Menu(root)
fl=Menu(menubar,tearoff=0)
fl.add_command(label="Exit")
menubar.add_cascade(label="FILE",menu=fl)
root.config(menu=menubar)

root.mainloop()