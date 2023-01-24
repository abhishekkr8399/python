from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window=Tk()
        btnOK=Button(window,text="OK",fg="white", bg="yellow",command=self.processOK)
        btnCancel=Button(window,text="Cancel", fg="white",bg="red",command=self.processCancel)
        btnOK.pack()
        btnCancel.pack()
        window.mainloop()
    def processOK(self):
        print("OK button is clicked")
    def processCancel(self):
        print("Cancel button is clicked")

ProcessButtonEvent()
