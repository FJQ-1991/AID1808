__author__ = 'freedom'
from tkinter import *
class Application(Frame):
    def __init__(self,master):
        frame =Frame(master)
        frame.pack()
        self.counter = 0
        self.button = Button(frame)
        self.button["text"] = "Click:0"
        self.button['command'] = self.updata
        self.button.grid()
        self.button2 = Button(frame)
        self.button2['text'] = 'QUIT'
        self.button2['command'] = frame.quit
        self.button2.grid()
    def updata(self):
        self.counter +=1
        self.button['text'] = 'Click:' +str(self.counter)
root = Tk()
root.title("Click Test")
root.geometry("2000x100")
app = Application(root)
root.mainloop()