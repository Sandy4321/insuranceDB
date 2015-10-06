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
-ID(unique/KEY, Auto Incriment, NOT NULL)
-itemID(unique), autoIncrement NOT NULL)
-itemNamei(NOT NULL)
-Description(NOT NULL)
-Model Number
-Serial
-pictureName
-receiptPic
-lastEdited(NOT NULL)#AUTO ON TODAY DATE OF SAVING


Coded by Martin Verret
https://github.com/arist0v/insuranceDB

"""

#import needed library
import Tkinter as tk#import tkinter library
from Languages import language_frCA as text#import the home library for the language
import tkFileDialog as tkf#import the file dialog widget for tkinter
import sqlite3

class insuranceDB():
	"""
	Main program, insuranceDB is a software that help you to build an inventory for 
	your insurance company to help you list your goods in case of disaster
	"""
	version = "0.1"
	def __init__(self):
		window = tk.Tk()
		window.geometry("800x600")#START RES
		window.wm_title(text.mainText.program + " " + self.version)#MAYBE ADD FRENCH NOR ENGLISH TITLE WITH VAR
		self.mainPage(window)
		window.mainloop()

	def mainPage(self, window):
		'''
		function to provide the main windows for the software
		'''
		self.clearWindow(window)#reset main Window
		
		mainFrame = tk.Frame(window)#create main frame
		
		'''
		creating Menu Bar
		'''
		menubar = tk.Menu(mainFrame)#create the menu bar

		filemenu = tk.Menu(menubar, tearoff=0)#create the file menu

		'''
		add file menu entry!!!
		'''
		
		filemenu.add_command(label=text.menuText.newDB, command = lambda: self.createNewTable(tkf.asksaveasfilename(defaultextension=".idb", filetypes=(("InsuranceDB files", "*.idb"),("ALL FILES", "*.*")))))
		filemenu.add_command(label=text.menuText.fileQuit, command = lambda: self.exit(window))
				
		menubar.add_cascade(label=text.menuText.fileMenu, menu=filemenu)#apply the file menu
			
		window.config(menu=menubar)
	
	def clearWindow(self, window):
		"""
		Function to clear the window content 
		"""
		try:
	                for children in window.winfo_children():
	                        children.destroy()#try to destroy window children(if exist):
		except:
			pass		

	def exit(self, window):
		'''
		function to quit the program
		'''

		window.quit()
	
	def createNewTable(self, fileName):

		'''
		function to create a new DB.
		'''
		conn = sqlite3.connect(fileName)
		sqlRequest = "CREATE TABLE items(ID INTEGER NOT NULL UNIQUE PRIMARY KEY,itemID INTEGER NOT NULL UNIQUE,itemName VARCHAR(255) NOT NULL,description VARCHAR(255),modelNumber VARCHAR(255),serialNumber VARCHAR(255),pictureFile VARCHAR(255),receiptFile VARCHAR(255),lastEdited SMALLDATE NOT NULL)"
		conn.execute(sqlRequest)
		conn.close()
		
		
#START THE PROGRAM
if __name__ == '__main__':
	insuranceDB()
