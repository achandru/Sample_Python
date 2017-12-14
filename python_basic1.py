import smtplib

TO = 'anjali.b@ambertag.com'
SUBJECT = 'sending via python script.'
TEXT = 'Hi, this is Anju'


gmail_sender = '2011anjali.b@gmail.com'
gmail_passwd = 'anjali18'


BODY = '\r\n'.join([
       'To: %s' % TO,
       'From: %s' % gmail_sender,
       'Subject: %s' % SUBJECT,
       '',
       TEXT
       ])


try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(gmail_sender,gmail_passwd)
    server.sendmail(gmail_sender, [TO], BODY)
    print "email sent"
except Exception as err:
    print err
    print "error sending email"


server.quit()

