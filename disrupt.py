#!/usr/bin/python
#----------------------------------------------------------------------------
#Main Disrupt Modules 
#----------------------------------------------------------------------------
#The MIT License (MIT)
#
#Copyright (c) 2015 Matt Perez
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
import sys
import traceback
#from os import getcwd, mkdir, path
#ys.path.insert(0, getcwd() + '/modules/')

#Utilitys
from modules.utility.colors import *
from modules.utility.options import *
from modules.utility.update import *  

#Modules
from modules.smsbomber.smsbomber import *

disrupt_version = '0.1.0'
disrupt_message = '[!] Tread lightly...'

class Disrupt(object):
	def __init__(self):
		self.smsbomber = 0                                                  
	def run_modules(self):
		main_header()
		main_menu()
		module_choice = raw_input(colors.bold_crimson+'Disrupt ' + reset.reset+'> ')

		if module_choice == '1':
			try:
				self.smsbomber += 1
				import modules.smsbomber.smsbomber
				reload(modules.smsbomber.smsbomber)
				#SMSBomb()
			except:
				self.smsbomber -= 1
				print'\n[!] Exited with %s modules.' % self.smsbomber

		if module_choice == '5':
			try:
				help()
			except:
				sys.exit()

		if module_choice == '6':
			try:
				update()
			except:
				sys.exit()
				
		elif module_choice == '0' or module_choice == 'quit' or module_choice == 'q' or module_choice == 'exit':
			sys.exit('\n[!] Error, user quit.')


if __name__ == '__main__':
	Disrupt().run_modules()