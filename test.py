# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 20:33:18 2017

@author: MORGAN
"""
import sys
import os
import time, datetime

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
		stream = sys.__stdout__
	)
	print("Done.", end="\n")

def main():
	setup()
	logging.info("Program started.")
	starttime = time.time()
	logging.debug("Starting GUI.")
	sys.stdout = GUI.STREAM
	GUI.GUI.mainloop()
	sys.stdout = sys.__stdout__
	logging.debug("GUI exited.")
	logging.info("Program exiting.")
	logging.info("Total runtime: {}".format(str(time.time() - starttime)))

if __name__ == "__main__":
	main()
