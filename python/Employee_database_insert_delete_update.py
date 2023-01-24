# ----------- Execute the program using Python version 3 ---------------# 
# ----------- In Python 2.7  - use MySQLdb instead of pymysql -----------# 
''' Steps to be follwoed before the exeution of this program:
1 - Loin to mysql
2 - Create database EMP  
3 - create table emp  
		emp( ssn varchar(10),Fname varchar(10),Lname varchar(10),age int,place varchar(20),Salary int)'''
import tkinter
import pymysql
from tkinter import messagebox

window = tkinter.Tk()
var1=tkinter.IntVar()
var2=tkinter.StringVar()
var3=tkinter.StringVar()
var4=tkinter.IntVar()
var5=tkinter.StringVar()
var6=tkinter.IntVar()

def Insert():	
	db = pymysql.connect("172.16.2.3","student","student","student" )
	cursor = db.cursor()
	sql = "INSERT INTO emp164 VALUES ('%s','%s','%s',%d,'%s',%d)"%(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get())
	try:
		cursor.execute(sql)
		db.commit()
		messagebox.showinfo("Success","Successfully inserted")
	except:
		messagebox.showerror("Error","Something Wrong")
	db.close()

def Delete():
	w =tkinter.Toplevel()
	def dele():
		db = pymysql.connect("172.16.2.3","student","student","student" )
		cursor = db.cursor()
		sql = "DELETE FROM emp164 WHERE salary > %d and place='%s' " % (v1.get(),v2.get())
		try:
			cursor.execute(sql)
			db.commit()
			messagebox.showinfo("Success","Successfully Deleted")
		except:
			messagebox.showerror("Error","Something Wrong")
			print("error")
		db.close()

	
	v1=tkinter.IntVar()
	v2=tkinter.StringVar()

	l1 = tkinter.Label(w, text="Salary")
	e1 = tkinter.Entry(w,textvariable=v1)

	l2 = tkinter.Label(w, text="Place")
	e2 = tkinter.Entry(w,textvariable=v2)

	b1= tkinter.Button(w, text ="Delete",command=dele)
	l1.grid(row=0,column=0)
	e1.grid(row=0,column=1)

	l2.grid(row=1,column=0)
	e2.grid(row=1,column=1)
	b1.grid(row=3,column=0)
	w.mainloop()

def Update():
	
	db = pymysql.connect("172.16.2.3","student","student","student" )
	cursor = db.cursor()
	sql = "UPDATE emp164 SET fname='%s',lname='%s',age=%d,place='%s',salary=%d WHERE ssn ='%s'" % (var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var1.get())
	try:
		cursor.execute(sql)
		db.commit()
		messagebox.showinfo("Success","Successfully Updated")
	except:
		messagebox.showerror("Error","Something Wrong")
	db.close()

label1 = tkinter.Label(window, text="SSN")
entry1 = tkinter.Entry(window,textvariable=var1)

label2 = tkinter.Label(window, text="FName")
entry2 = tkinter.Entry(window,textvariable=var2)

label3 = tkinter.Label(window, text="LName")
entry3 = tkinter.Entry(window,textvariable=var3)

label4 = tkinter.Label(window, text="Age")
entry4 = tkinter.Entry(window,textvariable=var4)

label5 = tkinter.Label(window, text="Palce")
entry5 = tkinter.Entry(window,textvariable=var5)

label6 = tkinter.Label(window, text="Salary")
entry6 = tkinter.Entry(window,textvariable=var6)

button1= tkinter.Button(window, text ="Insert Employee Details",command=Insert)
button2= tkinter.Button(window, text ="Delete based on Salary and Place",command=Delete)
button3= tkinter.Button(window, text ="Update Employee details based on SSN",command=Update)


label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)

label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)

label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)

label4.grid(row=3,column=0)
entry4.grid(row=3,column=1)

label5.grid(row=4,column=0)
entry5.grid(row=4,column=1)

label6.grid(row=5,column=0)
entry6.grid(row=5,column=1)

button1.grid(row=6,column=0)
button2.grid(row=6,column=1)
button3.grid(row=6,column=2)

window.mainloop()
