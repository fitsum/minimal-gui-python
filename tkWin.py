import tkinter as tk

class App(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		self.applySettings()
		self.mainloop()

	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
		self.quitButton.grid()

	def applySettings(self):
		self.master.title('App')
		self.master.geometry("400x300")
		self.master.resizable()
		#self.master.wm_overrideredirect(True)



