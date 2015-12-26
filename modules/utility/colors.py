#!/usr/bin/python
#----------------------------------------------------------------------------
#Main Disrupt Colors Modules 
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

#Going to implement a random color scheme for main_header

colors_random = ['\033[0m', '\033[31m', '\033[32m', '\033[32m', '\033[33m',
				'\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[93m'
				'\033[1;37m', '\033[1;31m', '\033[1;32m', '\033[1;33m',
				'\033[1;34m', '\033[1;38m', '\033[1;35m', '\033[1;36m']

class colors:
	#Normal Colors
	white = '\033[0m' 
	red = '\033[31m'   
	green = '\033[32m'   
	orange = '\033[33m'  
	blue = '\033[34m'   
	magenta = '\033[35m' 
	cyan = '\033[36m'    
	gray = '\033[37m'    
	yellow = '\033[93m'  

	#Bold Colors
	bold_white = '\033[1;37m'
	bold_red = '\033[1;31m'
	bold_green = '\033[1;32m'
	bold_yellow = '\033[1;33m'
	bold_blue = '\033[1;34m'
	bold_crimson  = '\033[1;38m'
	bold_magenta = '\033[1;35m'
	bold_cyan = '\033[1;36m'
	reset = "\033[0m" 
		