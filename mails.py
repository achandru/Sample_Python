import smtplib
import base64
from datetime import datetime
from datetime import timedelta
import time

TodayDate= datetime.now()
YestDate= TodayDate - timedelta(days=1)
EndOpt= str(YestDate.day)+'-'+str(YestDate.month)+'-'+str(YestDate.year)
conv=time.strptime(EndOpt,"%d-%M-%Y")
sampl=time.strftime("%d%M%y",conv)
filename = "/home/chandru/io_stat/io_stat_"+ sampl
# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

gmail_user = 'achandrumca@gmail.com'  
gmail_password = 'Chandru@1989'

sent_from = gmail_user

marker = "AUNIQUEMARKER"

body ="""
Hello Team.

I have attached Hardware performance report


Thanks & Regards
Anjali B

"""

to = ['achandrumca@gmail.com','chandru@dalchemy.com','anjali@dalchemy.com']


# Define the main headers.
part1 = """From: Chandru <achandrumca@gmail.com>
To: chandru <achandrumca@gmail.com> , chandru <chandru@dalchemy.com> , Anjali <anjali@dalchemy.com>
Subject: Hardware Performance Report.
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
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, message)
    server.close()

    print 'Email sent!'
except Exception as Err:
    print 'Something went wrong...'
    print Err

