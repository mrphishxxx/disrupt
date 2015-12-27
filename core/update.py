#!/usr/bin/python
import os
import time
import urllib2

url = 'https://github.com/ozylol/voyager.git'
ret = urllib2.urlopen('https://github.com/ozylol/voyager')

def update():
	if ret.code == 200:
		print '[!] Updating {}\n'.format(url)
		time.sleep(1)
		os.system('git reset --hard HEAD')
		os.system('git pull {}'.format(url))
		print '\n[!] Voyager is up to date!'
	elif ret.code == 404:
		print '[!] Error, URL may be wrong of repository does not exist?'
update()