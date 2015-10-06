#!/bin/python 
# -*- coding: utf-8 -*-

"""
Software to build a DB for insurance Company 

TODO:
-ALL

Function
-Write/Read db from a file
-Add data in DB
-edit data
-delete Data
-export in PDF + .jpg folder into a ZIP
-put color in red for item no update in 1 year
-open different DB
-show total value for all item
-rename picture with itemNumber .ext in separate folder (picture/receipt)

DB FIELD
-ID(unique/KEY)
-itemID(unique)
-itemName
-Description
-Model Number
-Serial
-pictureName
-receiptPic


Coded by Martin Verret(verret.martin@gmail.com)

"""

#import needed library
import Tkinter as tk

class insuranceDB():
	"""
	Main program, insuranceDB is a software that help you to build an inventory for 
	your insurance company to help you list your goods in case of disaster
	"""
	version = "0.1"
	def __init__(self):
		window = tk.Tk()
		window.geometry("800x600")#START RES
		window.wm_title("insuranceDB " + self.version)#MAYBE ADD FRENCH NOR ENGLISH TITLE WITH VAR
		window.mainloop()
#START THE PROGRAM
if __name__ == '__main__':
	insuranceDB()
