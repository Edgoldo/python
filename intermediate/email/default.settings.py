import os

# Set environment variables to connect with your email account
os.environ['EMAIL_HOST_USER'] = 'example@example.com'
os.environ['EMAIL_HOST_PASSWORD'] = 'password'
os.environ['EMAIL_USE_TLS'] = 'True or False'
os.environ['EMAIL_SMTP_HOST'] = 'smtp.server.com'
os.environ['EMAIL_SMTP_PORT'] = '587'
os.environ['EMAIL_IMAP_HOST'] = 'imap.server.com'
os.environ['EMAIL_IMAP_PORT'] = '587'
os.environ['EMAIL_FROM'] = os.getenv('EMAIL_HOST_USER')