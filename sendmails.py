# Welcome To My Repository :
# This is a code snippet to send emails using your own account.
# This code is writting by RABAH DJEBBES.

import smtplib

your_email = 'YOUR EMAIL ADDRESS'
email_password = 'EMAIL PASSWORD'
recipient = 'EMAIL OF RECIPIENT'
subject = 'SUBJECT HERE'
body = 'BODY HERE !'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (your_email, recipient, subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, email_password)
    server.sendmail(your_email, recipient, email_text)
    server.close()
except:
    print("Something went wrong...")

