from tkinter import *
from tkinter.ttk import *

class stdoutOverride(object):
	def __init__(self, widget):
		self.widget = widget

	def write(self, string):
		self.widget.insert(INSERT, string)
		self.widget.see(END)

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		master.minsize(width = 100, height = 100)
		master.maxsize(width = 500, height = 500)
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

		self.nnmenu = Menu(self.menubar, tearoff = 0)
		self.nnmenu.add_command(label = "Import", command = self.say_hi)
		self.nnmenu.add_command(label = "Export", command = self.say_hi)
		self.nnmenu.add_separator()
		self.nnmenu.add_command(label = "Close", command = self.say_hi)
		self.menubar.add_cascade(label = "Network", menu = self.nnmenu)

		self.master.config(menu = self.menubar)

		self.lab = Label(self, text = "My first label").grid(row = 0)
		self.e1 = Entry(self)
		self.v = StringVar()
		self.e1["textvariable"] = self.v
		self.e1.bind("<Key-Return>", self.printstuff)
		self.e1.grid(row = 2)

		self.t = Text(self)
		self.t.grid(row = 3, rowspan = 3, columnspan = 2)

		global TEXTBOX
		TEXTBOX = self.t

	def say_hi(self):
		print("hi")

	def printstuff(self, event):
		print(self.v.get())

root = Tk()
GUI = Application(master = root)
STREAM = stdoutOverride(TEXTBOX)
