import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('appupadashetty@gmail.com','rajeshpadashetty@gmail.com')
server.quit()