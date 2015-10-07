# -*- coding: utf-8 -*-
#!/usr/bin/python

'''
@author = Martin Verret
Language Pack for French Canada for insuranceDB
'''

'''
Text for Main Program function(windoe etc...)
'''

class mainSoftwareText:
	
	def __init__(self):
		self.program = "AssuranceDB"#name of the program
		self.author = "Martin Verret"
		self.contact = "https://github.com/arist0v/insuranceDB"

mainText = mainSoftwareText()

'''
text for the menu bar
'''

class menuSoftwareText:

	def __init__(self):
		self.fileMenu = "Fichier"
		self.fileQuit = "Quitter"
		self.newDB = "Nouvelle Liste"
		self.openDB = "Ouvrir Liste"
menuText = menuSoftwareText()

class softErrorMessage:
	'''
	text for all error message
	'''
	def __init__(self):
		self.windowTitle = "Erreur"
		self.errorOpenDB = "Échec de l'ouverture du fichier!"

errorMessage = softErrorMessage()	
