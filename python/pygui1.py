from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")
    
window =Tk()

#label=Label(window,text="welcome to python")
#button= Button(window,text="Click Me")
#label.pack()
#button.pack()
btnOK=Button(window,text="OK",fg="red", bg="white",command=processOK)
btnCancel=Button(window,text="Cancel", fg="white",bg="red",command=processCancel)
btnOK.pack()
btnCancel.pack()
window.mainloop()
