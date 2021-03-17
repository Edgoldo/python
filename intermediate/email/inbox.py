import os
import imaplib
import email
import settings

# Environment variables
USERNAME = os.getenv('EMAIL_HOST_USER')
PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
HOST = os.environ.get('EMAIL_IMAP_HOST')
PORT = os.environ.get('EMAIL_PORT')

def get_inbox():
    mail = imaplib.IMAP4_SSL(HOST)
    mail.login(USERNAME, PASSWORD)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)
# print(search_data)