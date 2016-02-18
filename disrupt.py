#!/usr/bin/python
# ----------------------------------------------------------------------------
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
import os
import sys
import time
import random
import urllib2
from modules.colors import *
from modules.options import *
from modules.smsbomber import *

url = 'http://www.github.com/ozylol/disrupt.git'
ret = urllib2.urlopen('http://www.github.com/ozylol/disrupt')

class Disrupt(object): ##Class for disrupt
    def __init__(self):
        self.url_error = False
        self.smsbomber = 0
        self.dos = 0
    def run_modules(self):
        main_header()
        main_menu()
        bash = random.choice(colors_random)+'Disrupt ' ##User input
        bash += '> '+reset
        module_choice = raw_input(bash)
        if module_choice == '1':
            try:
                self.smsbomber += 1
                ##SMSBomber is loaded through function not file
                #reload(modules.smsbomber)
                SMSBomb()
            except Exception:
                self.smsbomber -= 1
                import modules.smsbomber
        elif module_choice == '2':
            try:
                self.dos -= 1
                print 'Currently in beta.' ##no working DOS modules 
            except Exception:
                self.dos -= 1
                import modules.dos
        elif module_choice == '3':
            if ret.code == 200:
                print '[!] Updating {}\n'.format(url)
                time.sleep(1)
                os.system('git reset --hard HEAD') ##used `git reset --hard HEAD` then pulled the repo for update 
                os.system('git pull {}'.format(url))
                print '\n[!] Disrupt is up to date!'
                self.url_error = False
                Disrupt().run_modules()
            elif ret.code == 404:
                self.url_error = True ##if repo gets a 404 error exit and mark with class
                print '[!] Error, URL may be wrong of repository does not exist?'
        elif module_choice == '0' or module_choice == 'quit' or module_choice == 'exit':
            sys.exit('\n[!] Error, user quit.')

if __name__ == '__main__': 
    Disrupt().run_modules()