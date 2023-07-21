from tkinter import *
import tkinter.messagebox as msg
import pymysql
from pymysql import Error

def database():
    global conn,cursor
    conn=pymysql.connect(host="localhost",user="root",\
                         password="12arun[[]]",database="inspannerdb",\
                            port=3306)
    cursor=conn.cursor()



def register():
    database()
    if USER.get=="" or PASS.get=="" or NAME.get=="" or ADDRESS.get=="":
        l6.config(text="please fill the required feild",fg="Orange")

    else:
        cursor.execute("select * from ,'user' where 'user' = %s",[USER.get])
        if cursor.fetchone() is not None:
            l6.config(text="username is already stored".fg="red")
        
        else:
            cursor.execute("inser into 'user' (user,pass,name,address) values(%s,%s,%s,%s)",\
                           (str(USER.get())),str(PASS.get()),\
                            str(NAME.get()),str(ADDRESS.get()))
            conn.commit()
            USER.set("")
            PASS.set("")
            NAME.set("")
            l6.config(text="Successfully created")
        cursor.close()
        conn.close()

root=Tk()
root.title("Register Form")
root.geometry("700X700")
root.resizable(0,0)

USER=StringVar()
PASS=StringVar()
NAME=StringVar()
ADDRESS=StringVar()

def Exit():
    result=msg.askquestion('System','want to Exit ??',icon="warning")
    if result=='yes':
        root.destroy()
        exit()

tf=Frame(root,height=100,width=640,bd=1,relief=SOLID)
tf.pack(side=TOP)

tf=Frame(root,height=100,width=640,bd=1,relief=SOLID)

l1=Label(rf,text="Register Form",font=('arial',18),bd=1,width=640)
l1.pack()

l2=label(rf,text="user name",font=('arial',18),bd=1)
l2.grid(row=1)

l3=label(rf,text="Password",font=('arial',18),bd=1)
l3.grid(row=2)

user=Entry(rf,font('arial',20),textvariable=USER,width=15,show="*")
user.grid(row=1,column=1)

pass1=Entry(rf,font('arial',20),textvariable=USER,width=15)
pass1.grid(row=2,column=1)

btn=Button(rf,)