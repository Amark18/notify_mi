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
This program uses gmail to send a SMS/MMS message to a phone number
with a known service provider and optionally to an email address.
'''

def send_message(
    message, 
    subject = None, 
    send_to = None, 
    threaded = False,
    send_email_only = None, 
    file_attachment = None):
    
    '''
    Send a message using gmail via SMS/MMS, email, or both
    
    :param            str : message : message to be sent
    :param <optional> str : subject : add a subject to message
    :param <optional> str : file_attachment : path to file to attach to message
    :param <optional> bool: threaded : user can decide if they want to not block main thread
    :param <optional> str : send_to : email address to send to
    :param <optional> bool: send_email_only : only send email and do not send a text message
    '''
    
    # allow user to not block the main thread when calling
    if threaded:
        helper.threaded(__send_message_via_email(
            message, subject, send_to, send_email_only, file_attachment))
    else:
        __send_message_via_email(
            message, subject, send_to, send_email_only, file_attachment)

def __send_message_via_email(
    message, 
    subject = None , 
    send_to = None, 
    send_email_only = False, 
    file_attachment = None):
    
    # ensure that credentials and info added meets specifications
    __check_for_exceptions()
    
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
        
    # retrieve information needed to send message
    sender_email, email_password = sender_credentials
    # get message type (sms/mms) based on provider
    # some do not have mms capabilities
    message_type = helper.MESSAGE_TYPE[0] \
        if PROVIDERS.get(phone_provider).get(helper.MMS_SUPPORT_KEY) \
        else helper.MESSAGE_TYPE[1]
    # create receiver email based on their phone number and carrier
    receiver_phone_number = f'{phone_number}@{PROVIDERS.get(phone_provider).get(message_type)}'
    
    # create gmail body
    email_message = MIMEMultipart()
    if _subject is not None:
        email_message["Subject"] = _subject
    email_message["From"] = sender_email
    email_message["To"] = receiver_phone_number
    email_message.attach(MIMEText(_message, helper.TEXT_TYPE))
    
    # if file was included, attach to message
    if file_attachment is not None and Path(file_attachment).is_file:
        # gmail does not allow a file > 1 MB to be attached
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
        # login to gmail
        email.login(sender_email, email_password)
        
        # send SMS/MMS message
        if not send_email_only:
            # send email with body and attachment
            email.sendmail(sender_email, receiver_phone_number, email_message.as_string())
            
        # send to email address
        # only basic checking is done to the email provided due to the user 
        # being a "programmer", hence it is assumed that they will input a 
        # correct email address
        if send_to is not None:
            if helper.AT_SYMBOL in send_to and helper.EMAIL_SUFFIX in send_to:
                # send email with body and attachment
                email.sendmail(sender_email, send_to, email_message.as_string())
            else:
                raise helper.EmailFormatError

def __check_for_exceptions():
    # check if credentials have been added to notify_me_secrets.py
    if helper.no_credentials_added():
        raise helper.NoCredentialsAdded
    # verify phone number is formatted correctly
    if len(PHONE_NUMBER) != 10 or not PHONE_NUMBER.isdigit():
        raise helper.PhoneNumberError
    # verify provider given is found in providers.py
    if PROVIDERS.get(PHONE_PROVIDER) is None:
        raise helper.ProviderNotRecognized
