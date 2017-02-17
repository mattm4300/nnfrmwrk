from tkinter import *
from tkinter.ttk import *

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		self.master = master

	def createWidgets(self):
		self.menubar = Menu(self.master)

		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Open", command=self.say_hi)
		self.filemenu.add_command(label="Save", command=self.say_hi)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=self.master.quit)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)

		self.master.config(menu = self.menubar)

		self.lab = Label(self, text = "My first label").grid(row = 1)
		self.e1 = Entry(self)
		self.v = StringVar()
		self.e1["textvariable"] = self.v
		self.e1.bind("<Key-Return>", self.printstuff)
		self.e1.grid(row = 2)

	def say_hi(self):
		print("hi")

	def printstuff(self, event):
		print(self.v.get())

root = Tk()
GUI = Application(master = root)
