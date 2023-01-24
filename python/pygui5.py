import tkinter as tk
window= tk.Tk()
var1=tk.StringVar()
var2=tk.StringVar()
def display():
    var2.set(var1.get())
l1=tk.Label(window,text="Username")
e1=tk.Entry(window,textvariable=var1,show="*")
l2=tk.Label(window,text="Hi")
e2=tk.Entry(window,textvariable=var2)
btn=tk.Button(window,text="Submit",command=display)

l1.pack()
e1.pack()
btn.pack()
l2.pack()
e2.pack()

tk.mainloop()
