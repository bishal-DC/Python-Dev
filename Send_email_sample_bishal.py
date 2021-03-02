import smtplib #Importing smtplib

conn=smtplib.SMTP('smtp.gmail.com',587) # connecting to the domain

conn.ehlo() # Cnnect to server sends internet traffic from python console

conn.starttls() # start encryption

response=conn.login('bishal.3gp@gmail.com','dfabkdqlxsvdjiay') #  logsin to user specific account

from_address=r'bishal.3gp@gmail.com'

to_address=r'bishal.3gp@gmail.com'

message='Subject: This is a test email\n\nHi All,\nThis is a test email to ' \
        'check everything is working or not!\n\nThanks\nBishal '

sendmail=conn.sendmail(from_address,to_address,message) #Sendmail fuction sends the email to user

print(sendmail)

conn.close()
