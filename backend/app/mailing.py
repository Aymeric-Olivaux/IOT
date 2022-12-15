import smtplib, ssl
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
smtp_server = os.getenv('SMTP_SERVER')
sender_address = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

class Info:
    email: str
    max_value: (int, str)
    mean_value: int

    def __init__(self, email, max_value, mean_value):
        self.email = email
        self.max_value = max_value
        self.mean_value = mean_value

# Create a secure SSL context
context = ssl._create_unverified_context()

def send_email(email, info):
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    content = f'Subject: Ambizen report - {date}\n\nThis is a report of the last 24 hours for your Ambizen device.\n\nThe maximum decibel value was {info.max_value[0]} at {info.max_value[1]}.\n\nThe mean decibel value was {info.mean_value}.\n\nThank you for using Ambizen!'
    with smtplib.SMTP_SSL(smtp_server, port=465, context=context) as server:
        server.login(sender_address, password)
        server.sendmail(sender_address, info.email, content)