#!/usr/bin/python
#----------------------------------------------------------------------------
#Main Disrupt Options Modules 
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
import random

from colors import *
from disrupt import *

def main_header():
	print colors.bold_crimson+'[v%s]' % (disrupt_version)
	print'\t ____   _                      _   '
	print'\t|    \ |_| ___  ___  _ _  ___ | |_ '
	print'\t|  |  || ||_ -||  _|| | || . ||  _|'
	print'\t|____/ |_||___||_|  |___||  _||_|  '
	print'\t                         |_|       '
	print'\t-==+ %s +==-' % (disrupt_message)
	print'\t-==+ https://github.com/ozylol +==-'
	print reset.reset 

def main_menu():
	print"""
	[1] SMS Bomber   [3] N/A
	[2] DoS Attack   [4] N/A

[5] Help 
[6] Update
"""

def help():
	print"""
Usage:
	
	Options [5]: Display help menu. 

Disrupt Option:
	
	SMS Bomber:	 Allows users to clog victims sms using smtplib.
"""

#def main_carriers():
#	print color.bold_crimson+"""
#	[1] AT&T
#	[2] Boost Mobile
#	[3] MetroPCS
#	[4] Sprint
#	[5] T-Mobile
#	[6] Virgin Mobile
#	[7] Verizon
#	"""
#	reset.reset