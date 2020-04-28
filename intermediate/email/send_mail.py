import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Environment variables
USERNAME = os.getenv('EMAIL_HOST_USER')
PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
HOST = os.environ.get('EMAIL_SMTP_HOST')
PORT = os.environ.get('EMAIL_PORT')

def send_mail(text='Email Body', subject='Hello World', from_email='Hungry Py <hungrypy@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # Login to smtp server
    server = smtplib.SMTP(host=HOST, port=PORT)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # Other way to start the server, login and send email
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass