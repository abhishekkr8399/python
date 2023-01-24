from tkinter import *
from tkinter import messagebox
import pymysql #download pymysql if not exists
def search():
 db = pymysql.connect ("172.16.2.3","student","student","College") #Here college is a Database name
 cursor = db.cursor()
 sql="select * from student where usn='%s'"%(v1.get())
 try:
   cursor.execute(sql)
   data=cursor.fetchall()
   if len(data)==0:
    messagebox.showinfo("Error","USN does not exists.")
   else:
    for row in data:
     name=row[1]
     age=row[2]
     branch=row[3]
     v2.set(name)
     v3.set(age)
     v4.set(branch)
     messagebox.showinfo("Success","USN found")
 except:
    messagebox.showerror("Error","Unsuccessful")
 db.close()
window=Tk()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
window.geometry("250x190")
l1=Label(window,text="Enter the usn")
b=Button(window,text="Search",command=search)
l2=Label(window,text="Name")
l3=Label(window,text="Age")
l4=Label(window,text="Branch")
t1=Entry(window,width=20,textvariable=v1)
t2=Entry(window,width=20,textvariable=v2)
t3=Entry(window,width=10,textvariable=v3)
t4=Entry(window,width=10,textvariable=v4)
l1.grid(column=0,row=0)
l2.grid(column=0,row=2)
l3.grid(column=0,row=3)
l4.grid(column=0,row=4)
t1.grid(column=1,row=0)
t2.grid(column=1,row=2)
t3.grid(column=1,row=3)
t4.grid(column=1,row=4)
b.grid(column=1,row=1)
window.mainloop()