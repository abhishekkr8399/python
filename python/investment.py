from tkinter import*
def calc():
 i=eval(t1.get())
 y=eval(t2.get())
 r=eval(t3.get())/1200
 d=i*(r+1)**(y*12)
 t4.configure(text=str(d))
window=Tk()
window.geometry('250x150')
lbl1=Label(window,text="Investment Amount")
lbl1.grid(column=0,row=0)
lbl2=Label(window,text="Years")
lbl2.grid(column=0,row=1)
lbl3=Label(window,text="Annual Interst Rate")
lbl3.grid(column=0,row=2)
lbl4=Label(window,text="FutureValue")
lbl4.grid(column=0,row=3)
t1=Entry(window,width=20)
t1.grid(column=1,row=0)
t2=Entry(window,width=20)
t2.grid(column=1,row=1)
t3=Entry(window,width=20)
t3.grid(column=1,row=2)
t4=Label(window)
t4.grid(column=1,row=3)
b=Button(window,text="Calculate",command=calc)
b.grid(column=1,row=4)
window.mainloop()
