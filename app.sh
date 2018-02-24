#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.width = self.winfo_reqwidth()/2
        self.master.title('Sample application')
        self.master.geometry("400x300")
        self.master.resizable()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()


app = Application()
app.mainloop() 

                           
