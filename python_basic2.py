import smtplib
import base64

filename = "/home/ambertag/schema.csv"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = '2011anjali.b@gmail.com'
passwrd = 'anjali18'
reciever = 'anjali.b@ambertag.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""

# Define the main headers.
part1 = """From: '2011anjali.b@gmail.com'
To: 'sharath@ambertag.com'
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)
        

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)



# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3


try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(sender,passwrd)
    server.sendmail(sender, reciever, message)
    print "Successfully sent email"
except Exception as err:
   print "Error: unable to send email"
   print err
