from tkinter import *
from tkinter import messagebox
def addition():
 num1=float(t1.get())
 num2=float(t2.get())
 messagebox.showinfo("Result","The sum is %.2f" %(num1+num2))
def subtraction():
 num1=float(t1.get())
 num2=float(t2.get())
 messagebox.showinfo("Result","The difference is %.2f" %(num1-num2))
def multiplication():
 num1=float(t1.get())
 num2=float(t2.get())
 messagebox.showinfo("Result","The product is %.2f" %(num1*num2))
def division():
 num1=float(t1.get())
 num2=float(t2.get())
 messagebox.showinfo("Result","The quotient is %.2f" %(num1/num2))
window=Tk()
l1=Label(window,text="Enter the number 1")
l2=Label(window,text="Enter the number 2")
t1=Entry(window,width=10)
t2=Entry(window,width=10)
b1=Button(window,text="Add",command=addition)
b2=Button(window,text="Subtract",command=subtraction)
b3=Button(window,text="Multiply",command=multiplication)
b4=Button(window,text="Divide",command=division)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
window.mainloop()
