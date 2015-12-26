#!/usr/bin/python
import os
import sys
import time
import random
import argparse

from core import colors
from core import logo
from flask import Flask,abort,render_template
app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument(
	'-m', '--map', help='Geo live mapping system', action='store_true')
parser.add_argument(
	'-u', '--update', help="Update repository", action='store_true')
args = parser.parse_args()

lat = 33.7550
lng = 84.3900

@app.route("/")
def base():
	return render_template('base.html', lat=lat, lng=lng)

@app.route("/percapita")
def PerCapita():
	return render_template('percapita.html')

@app.route("/chart")
def Chart():
	return render_template('chart.html')

def main():
	#if not os.geteuid() == 0:
		#sys.exit(colors.bold_red+'[*] You must run as root'+colors.reset)
	try:
		print logo.logo
	except:
		print logo.logo
		sys.exit()
main()

def options():
	if args.map:
		try:
			time.sleep(1)
			app.run(port=3333, debug=True) 
		except:
			print colors.bold_red+'[!] Error, Something went wrong?'+colors.reset

	if args.update:
		try:
			time.sleep(1)
			reload(core.update)
		except:
			import core.update
options()