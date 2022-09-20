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
        self.quit_button = tk.Button(self)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.quit
        self.quit_button.grid(column=0, row=0)
        self.label = tk.Label(self)
        self.label["text"] = "Fitsum"
        self.label.grid(column=1, row=0, padx=200)

    def apply_settings(self):
        """ function applying app configurations """
        self.master.title('App')
        self.master.geometry("400x300")
        self.master.resizable()
        # self.master.wm_overrideredirect(True)
