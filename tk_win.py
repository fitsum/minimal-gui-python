"""  importing tkinter """
import tkinter as tk


class App(tk.Frame):
    """ class representing tk app """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.apply_settings()
        self.mainloop()

    def create_widgets(self):
        """ function creating app widgets """
        self.quit_button = tk.Button(self, text='Quit',
                                     command=self.quit)
        self.quit_button.grid()

    def apply_settings(self):
        """ function applying app configurations """
        self.master.title('App')
        self.master.geometry("400x300")
        self.master.resizable()
        # self.master.wm_overrideredirect(True)
