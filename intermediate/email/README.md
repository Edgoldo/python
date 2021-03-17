Work With Emails 
================

    This practice starting with a tutorial of Coding for Entrepreneurs - 30-Days-of-Python, where the instructor (Justin Mitchel), build a module to send and read emails in the 9th day of Python.

1) Environment Variables:
-------------------------

    You need to set variables in your settings.py file (can use default.settings.py as a guide), to connect with your email server. Example

    # Set environment variables to connect with your email account
    os.environ['EMAIL_HOST_USER'] = 'example@example.com'
    os.environ['EMAIL_HOST_PASSWORD'] = 'password'

    # Get environment variables
    USER = os.getenv('EMAIL_HOST_USER')
    PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

    # Getting non-existent keys
    FOO = os.getenv('FOO') # None
    BAR = os.environ.get('BAR') # None
    BAZ = os.environ['BAZ'] # KeyError: key does not exist.

2) Execute options:
-------------------

    The python version used to work with this folder was python 3.8. The main file to be excecuted is send.py, you can run in python terminal using:

    (python) $ python -i send.py name_example email_address

    That command runs the send file passing two parameters, name_example (is a name used to test the code), email_address (used to send an email, must be a valid address to check that receive the email)

    The option -i in that command allows to the interactive mode in python including all the send.py code