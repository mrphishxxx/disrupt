#!/usr/bin/python
import urllib2
import subprocess
import colors

url = 'http://www.github.com/ozylol/voyager'
ret = urllib2.urlopen('http://www.github.com/ozylol/voyager')

def update():
	if ret.code == 200:
		print '[!] Updating %s' % ur;
		subprocess.Popen("git pull", shell=True).wait()
		print '\n[!] Voyager is up to date!'
	elif ret.code == 404:
		print '[!] Error, URL may be wrong of repository does not exist?'