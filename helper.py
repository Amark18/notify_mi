import threading
import functools
from notify_me_secrets import *

'''
This is a helper class that contains constants 
and methods used throughout multiple files.
'''

# mms constants
EMPTY = ""
SMTP_GMAIL = "smtp.gmail.com"
SMTP_PORT = 465
FILE_TYPE = "image"
MESSAGE_TYPE = ["mms", "sms"]
MMS_SUPPORT_KEY = "mms_support"
TEXT_TYPE = "plain"
READ_BINARY = 'rb'
MB = 1000000

# see if credentials exist in secrets_firebase.py
def no_credentials_added():
    return EMPTY in [PHONE_NUMBER, SENDER_CREDENTIALS, PHONE_PROVIDER]

# exceptions
class NoCredentialsAdded(Exception):
    def __str__(self):
        return "Credentials missing from notify_me_secrets.py file."

class FileSizeExceeded(Exception):
    def __str__(self):
        return "Attachment cannot be me more than 1MB."

class PhoneNumberError(Exception):
    def __str__(self):
        return "Phone number should have 10 numbers only."
    
class ProviderNotRecognized(Exception):
    def __str__(self):
        return "Select a phone provider from providers.py file."

# decorator to automatically launch a function in a thread
def threaded(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper
