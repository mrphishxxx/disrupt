#!/usr/bin/python
import random
import colors
from disrupt import *

disrupt_version = '0.1.0'
disrupt_message = '[!] Tread lightly...'

def main_header():
	print random.choice(colors_random)+'[v%s]' % (disrupt_version)
	print '\t ____   _                      _   '
	print '\t|    \ |_| ___  ___  _ _  ___ | |_ '
	print '\t|  |  || ||_ -||  _|| | || . ||  _|'
	print '\t|____/ |_||___||_|  |___||  _||_|  '
	print '\t                         |_|       '
	print '\t-==+ %s +==-' % (disrupt_message)
	print '\t-==+ https://github.com/ozylol +==-'

def main_menu():
	print random.choice(colors_random)+"""
	[1] SMS Bomber [2] DoS Attack (N/A)

3) Update
"""