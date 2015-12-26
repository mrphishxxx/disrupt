#!/usr/bin/python
import urllib2
import subprocess
import colors

url = 'https://github.com/ozylol/voyager'
ret = urllib2.urlopen('https://github.com/ozylol/voyager')

def update():
	if ret.code == 200:
		print '[!] Updating %s' % url;
		subprocess.Popen("git pull", shell=True).wait()
		print '\n[!] Voyager is up to date!'
	elif ret.code == 404:
		print '[!] Error, URL may be wrong of repository does not exist?'