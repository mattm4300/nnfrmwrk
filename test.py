# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:33:18 2017

@author: MORGAN
"""
import sys
import os

from configloader import loadConfigs
import logging
from tkinter import *
from tkinter.ttk import *

# TODO: Add command line arguments.  These will override written file
#       instructions eventually.

"""
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		self.master = master

	def createWidgets(self):
		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.entrything = Entry()
		self.entrything.pack()

		self.contents = StringVar()
		self.contents.set("This is a variable.")

		self.entrything["textvariable"] = self.contents

		self.entrything.bind('<Key-Return>', self.print_contents)

		self.quit = Button(self, text="QUIT",
						command=self.master.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("hi there, everyone!")

	def print_contents(self, event):
		print("hi, contents are ->", self.contents.get())
"""

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


def setup():
	print("Running Setup... ", end="")
	configs = loadConfigs("configs.json")
	logging.basicConfig(
		#filename = configs["logging"]["filename"],
		filemode = configs["logging"]["filemode"],
		format = configs["logging"]["format"],
		datefmt = configs["logging"]["datefmt"],
		level = configs["logging"]["level"],
		stream = sys.stdout
	)
	print("Done.", end="\n")

def main():
	setup()
	logging.info("Program started.")
	logging.debug("Starting GUI.")
	root = Tk()
	app = Application(master = root)
	app.mainloop()
	logging.debug("GUI exited.")
	logging.info("Program exiting.")

if __name__ == "__main__":
	main()
