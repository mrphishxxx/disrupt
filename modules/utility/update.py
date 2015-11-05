#!/usr/bin/python
#----------------------------------------------------------------------------
#Main Disrupt Update Module 
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
import urllib2
import subprocess

from modules.utility.colors import *
from disrupt import *

URL = 'http://www.github.com/ozylol/disrupt'
ret = urllib2.urlopen('http://www.github.com/ozylol/disrupt')

def update():
	if ret.code == 200:
		print colors.bold_crimson+'[!] Updating %s' % URL
		print reset.reset
		subprocess.Popen("git pull", shell=True).wait()
		print colors.bold_crimson+'\n[!] Disrupt repository is up to date.'+reset.reset
	elif ret.code == 404:
		print colors.bold_crimson+'[!] Error, URL may be wrong of repository does not exist.'
		sys.exit(reset.reset)