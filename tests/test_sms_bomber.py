"""This is a test for the SMSBomber. Currently not updated."""
#!/usr/bin/python
import smtplib
import getpass
import sys

class SMSBomber(object):
    def __init__(self):
        self.sent_buffer = 0
    def sms_buffer(self):
        gmail_username = raw_input('[!] Enter Secure Gmail: ') 
        gmail_password = getpass.getpass(prompt='[!] Enter Secure Pass: ')
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        msg_from = '\x30' 
        msg_subject = '\x30'   
        msg_to = ''   
        thread_count = raw_input('[!] How many threads: ')
        msg_text = '\x30'*int(thread_count)

        thread_send = raw_input('[!] How many times would you like to send the thread: ')
        for i in xrange(int(thread_count)):
            bomb_phone = ("From: %s\r\nTo: %s \r\n\r\n %s" % (gmail_username, "" .join(msg_to), "" .join(msg_text)))
            print'\n[!] Sending Threads'

        session = smtplib.SMTP(smtp_server, smtp_port)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(gmail_username, gmail_password)
        session.sendmail(msg_from, msg_to, bomb_phone)
        session.quit()


if __name__ == '__main__':
    SMSBomber().sms_buffer()