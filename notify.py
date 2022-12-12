from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from notify_me_secrets import *
from providers import PROVIDERS
from pathlib import Path
import smtplib, ssl
import helper

''' 
This program utilizes gmail to send an SMS/MMS message 
to a phone number whose service provider is known. 
'''

# param: message -> message to be sent
# param: subject -> add a subject to message
# param: file_attachment -> path to file to attach to message
# param: threaded -> user can decide if they want this to not block main thread
def send_message(message, subject = None, file_attachment = None, threaded = False):
    # allow user to not block the main thread when calling
    if threaded:
        helper.threaded(__send_message_via_email(message, subject, file_attachment))
    else:
        __send_message_via_email(message, subject, file_attachment)

def __send_message_via_email(message, subject = None , file_attachment = None):
    check_for_exceptions()
    
    # initialize variables needed
    phone_number: str = PHONE_NUMBER
    _message: str = message
    file_attachment: str = file_attachment
    _subject: str = subject
    phone_provider: str = PHONE_PROVIDER
    sender_credentials: tuple = SENDER_CREDENTIALS
    smtp_server: str = helper.SMTP_GMAIL
    smtp_port: int = helper.SMTP_PORT
    if file_attachment is not None:
        attachment = Path(file_attachment)
        mime_subtype: str = attachment.suffix
        mime_maintype: str = helper.find_ext_mime_type(mime_subtype)
        file_name: str = attachment.name
        
    # get information needed to send message
    sender_email, email_password = sender_credentials
    # get message type (sms/mms) based on provider
    # some do not allow mms
    message_type = helper.MESSAGE_TYPE[0] \
        if PROVIDERS.get(phone_provider).get(helper.MMS_SUPPORT_KEY) \
        else helper.MESSAGE_TYPE[0]
    # create receiver email based on their phone number and carrier
    receiver_email = f'{phone_number}@{PROVIDERS.get(phone_provider).get(message_type)}'
    
    # create gmail body
    email_message = MIMEMultipart()
    if _subject is not None:
        email_message["Subject"] = _subject
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message.attach(MIMEText(_message, helper.TEXT_TYPE))
    
    # if file was included, attach to message
    if file_attachment is not None and Path(file_attachment).is_file:
        # gmail does not allow a file > 1MB to be attached
        # therefore the entire message will not be sent
        if attachment.stat().st_size > 1 * helper.MB:
            raise helper.FileSizeExceeded
        
        # open file being sent and attach to email_message
        with open(file_attachment, helper.READ_BINARY) as attachment:
            part = MIMEBase(mime_maintype, mime_subtype)
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={file_name}",)
            email_message.attach(part)

    # send the message
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context = ssl.create_default_context()) as email:
        # securely login to gmail
        email.login(sender_email, email_password)
        # send email with body and attachment
        email.sendmail(sender_email, receiver_email, email_message.as_string())

def check_for_exceptions():
    # check if info have been addeded in notify_me_secrets.py
    if helper.no_credentials_added():
        raise helper.NoCredentialsAdded
    # verify phone number formatting
    if len(PHONE_NUMBER) != 10 or not PHONE_NUMBER.isdigit():
        raise helper.PhoneNumberError
    # verify provider is found in oroviders.py
    if PROVIDERS.get(PHONE_PROVIDER) is None:
        raise helper.ProviderNotRecognized
    