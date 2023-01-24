from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window=Tk()
        text=Label(window,text="Hi python")
        bt1=Button(window,text="Red",command=self.setRed)
        bt2=Button(window,text="Violet", command=self.setViolet)
        bt3=Button(window,text="Green", command=self.setGreen)
        text.pack()
        bt1.pack()
        bt2.pack()
        bt3.pack()
        window.mainloop()
    def setRed(self):
        self.text["fg"]="red"
    def setViolet(self):
        self.text["fg"]="violet"
    def setGreen(self):
        self.text["fg"]="green"

ProcessButtonEvent()
