import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = "anjali@dalchemy.com"
emailto = "chandru@dalchemy.com"
fileToSend = "/home/dalchemy/crontab.text"
username = "anjali@dalchemy.com"
password = "anjali18"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "help I cannot send an attachment to save my life"
msg.preamble = "help I cannot send an attachment to save my life"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#server.starttls()
#server.ehlo()
#server.login(emailfrom,password)
#server.sendmail(emailfrom, emailto, msg.as_string())
#server.quit()


try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(emailfrom,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

    print 'Email sent!'
except Exception as Err:  
    print 'Something went wrong...'
    print Err





