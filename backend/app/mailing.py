import smtplib, ssl
import os
from dotenv import load_dotenv
import logging

port = 465  # For SSL

load_dotenv()
sender_address = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

# Create a secure SSL context
context = ssl._create_unverified_context()

def send_email(email, message):
    content = f'Subject: Ambizen report\n\nThe last value recorded by your device is {message}'

    with smtplib.SMTP_SSL("mail.tryhard.fr", context=context) as server:
        logging.getLogger('mailing').warning('Sending email to ' + email)
        server.login(sender_address, password)
        server.sendmail(sender_address, email, content)