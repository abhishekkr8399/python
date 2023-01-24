import tkinter as  t
def sel():
    s="Your selected the option "+str(var.get())
    l["text"]=s
root=t.Tk()
var=t.IntVar()
var1=t.IntVar()
l=t.Label(root)
r1=t.Radiobutton(root,text="Option 1",variable=var, value=1, command=sel)
r2=t.Radiobutton(root,text="Option 2",variable=var, value=2, command=sel)
r3=t.Radiobutton(root,text="Option 3",variable=var1, value=3, command=sel)
l.pack()
r1.pack()
r2.pack()
r3.pack()
sel()
t.mainloop()
