#!/usr/bin/python
import sys
import time
import random
import argparse
from core import colors
from core import logo
try:
	from flask import Flask,abort,render_template
except:
  sys.exit(color.bold_red+'You need to install the requirementes. \n`pip install -r requirements.txt`'+colors.reset)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

app = Flask(__name__)
lat = 33.7550
lng = 84.3900
randomcolors = ['#71f4c8','#b3b3b3','#808080','#f4a871']

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

parser = argparse.ArgumentParser()
parser.add_argument(
	'-m', '--map', help='Geo live mapping system', action='store_true')
parser.add_argument(
	'-u', '--update', help="Update repository", action='store_true')
args = parser.parse_args()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""Runs the web app"""

#load base.html
@app.route("/")
def base():
  return render_template('base.html',lat=lat,lng=lng,randomcolors=randomcolors)

@app.route("/percapita")
def PerCapita():
  return render_template('percapita.html')

@app.route("/piechart")
def Chart():
  return render_template('piechart.html')

@app.route("/map")
def Map():
  return render_tempalate('map.html')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main():
  #no need for running as root at this time
	#if not os.geteuid() == 0:
		#sys.exit(colors.bold_red+'[*] You must run as root'+colors.reset)
    print logo.logo
main()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""Parser options"""

def options():
  if args.map:
    try:
      time.sleep(1)
      app.run(port=3333, debug=True) 
    except:
      print colors.bold_red+'[!] Error, Something Went Wrong?'+colors.reset
  elif args.update:
    try:
      time.sleep(1)
      reload(core.update)
    except:
      import core.update
options()
