"""
Class to handle emails. to test this class, you need execute this file into
the interactive console of python:
$ python -i emailer.py

Then, you can use:

> from_email = "Anonimous Person <aperson@gm.com>"
> subject = "This is a new subject"
> template_name = "base_template.txt"
template_html = "base_template.html"
> context = {'title': 'Title of template', 'content': 'Content of template'}
> to_emails = ['email1@example.com', 'email2@example.com']
> emailer = Emailer (from_email=from_email, subject=subject, template_name=template_name, template_html=template_html, context=context, to_emails=to_emails)
> emailer.send_mail()
"""
import os
import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template

# Environment variables
USERNAME = os.getenv('EMAIL_HOST_USER')
PASSWORD = 435#os.environ.get('EMAIL_HOST_PASSWORD')
HOST = os.environ.get('EMAIL_SMTP_HOST')
PORT = os.environ.get('EMAIL_PORT')

class Emailer():
    from_email = ""
    to_emails = []
    subject = ""
    has_html = False
    test_send = False

    def __init__(self, *args, **kwargs):
        required_keys = ['from_email', 'subject', 'template_name', 'context']
        for key in required_keys:
            if key not in kwargs:
                raise Exception(f"The {key}, is required")
        assert isinstance(kwargs.get('to_emails'), list)
        self.to_emails = kwargs.get('to_emails', None)
        self.from_email = kwargs.get('from_email')
        self.subject = kwargs.get('subject', "")
        self.template_name = kwargs.get('template_name', None)
        self.template_html = kwargs.get('template_html', None)
        self.context = kwargs.get('context', {})
        self.test_send = kwargs.get('test_send', False)
        if self.template_html != None:
            self.has_html = True

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject
        if self.template_name != None:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), 'plain')
            print(txt_part)
            msg.attach(txt_part)
        if self.template_html != None:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), 'html')
            print(html_part)
            msg.attach(html_part)
        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        msg = self.format_msg()
        # Login to smtp server
        did_send = False
        if not self.test_send:
            with smtplib.SMTP(host=HOST, port=PORT) as server:
                print("Try ehlo")
                server.ehlo()
                print("Try starttls")
                server.starttls()
                print("Make login")
                server.login(USERNAME, PASSWORD)
                try:
                    print("Trying send the email")
                    server.sendmail(from_email, to_emails, msg_str)
                    did_send = True
                except:
                    did_send = False
        return did_send