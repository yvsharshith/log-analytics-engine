from typing import Dict
from email.message import EmailMessage
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL = "harshith7422@gmail.com"
PASSWORD = "xplj fywh jutl dwmw"


def send_anomaly_email(to_email: str, anomaly: Dict):
    subject = "Log Anomaly Detected!!"

    body = f"""
[Anomaly Detected in System Logs]

Time Window : {anomaly['timestamp']}
Error Count : {anomaly['error_count']}
Z-Score     : {round(anomaly['z_score'], 2)}

Please investigate immediately.

Regards,
Log Monitoring System
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

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
'''

