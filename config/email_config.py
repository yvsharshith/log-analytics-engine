'''
import smtplib
from email.mime.text import MIMEText

print("starting email script...")

sender = "harshith7422@gmail.com"
receiver = "harshithyvs2002@gmail.com"
password = "xplj fywh jutl dwmw"

print("creating email content...")

# create the email content
message = MIMEText("Sending this email using Python!!")

message['Subject'] = "Test email from Python"
message['From'] = sender
message['To'] = receiver

print("connecting to Gmail SMTP server...")
server = smtplib.SMTP('smtp.gmail.com', 587)

print("starting TLS encryption...")
server.starttls() # encrypt connection

print("logging in...")
server.login(sender, password)

print("sending email...")
server.sendmail(sender, receiver, message.as_string())

print("email sent sucessfully!")

print("closing server connection...")
server.quit()

print("program finished.")

'''
import smtplib
from email.mime.text import MIMEText

def send_email(sender, receiver, password, subject, body):
    print("starting email script...")

    print("creating email content...")
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    print("connecting to Gmail SMTP server...")
    server = smtplib.SMTP('smtp.gmail.com', 587)

    print("starting TLS encryption...")
    server.starttls()

    print("logging in...")
    server.login(sender, password)

    print("sending email...")
    server.sendmail(sender, receiver, message.as_string())

    print("email sent successfully!")

    print("closing server connection...")
    server.quit()

    print("program finished.")

sender = "harshith7422@gmail.com"
receiver = "harshithyvs2002@gmail.com"
password = "xplj fywh jutl dwmw"
subject = "Test email using python-smtp"
body = "Sending this email to confirm SMPT connection!"
send_email(sender, receiver, password, subject, body)
