# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:33:18 2017

@author: MORGAN
"""
import sys
import os

from configloader import loadConfigs
import logging
import GUI

# TODO: Add command line arguments.  These will override written file
#       instructions eventually.


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
	GUI.GUI.mainloop()
	logging.debug("GUI exited.")
	logging.info("Program exiting.")

if __name__ == "__main__":
	main()
