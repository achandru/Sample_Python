import smtplib
from smtplib import SMTPException

sender = '2011anjali.b@gmail.com'
receivers = ['anjali.b@ambertag.com']

message = """From: From Person <2011anjali.b@gmail.com>
To: To Person <anjali.b@ambertag.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
