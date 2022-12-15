import smtplib, ssl
import os
from dotenv import load_dotenv
import datetime

port = 465  # For SSL

load_dotenv()
smtp_server = os.getenv('SMTP_SERVER')
sender_address = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

# Create a secure SSL context
context = ssl._create_unverified_context()

def send_email(email, message):
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    content = f'Subject: Ambizen report - {date}\n\nThe last value recorded by your device is {message}'
    with smtplib.SMTP_SSL(smtp_server, context=context) as server:
        server.login(sender_address, password)
        server.sendmail(sender_address, email, content)