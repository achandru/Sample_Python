import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("2011anjali.b@gmail.com", "anjali9964885790")
 
msg = "Hi Mental.. How are you."
server.sendmail("2011anjali.b@gmail.com", "chandru@dalchemy.com", msg)
server.quit()

