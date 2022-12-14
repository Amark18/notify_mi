## Notify Mi
🔔 Notify Mi simplifies sending yourself text and email notifications from your personal projects by utilizing your gmail account. It is a convenient and cost-effective solution with the goal of providing you an `easy` and `free` way to send messages in response to events.

Notify Mi is particularly useful when working with IoT devices. It can allow you to receive messages in response to events such as when a sensor value reaches a certain threshold, when a sensor detects something, when a sensor encounters an error, or when a daily or custom timed event occurs. This makes it easy to keep track of what is happening with your IoT device and react to any change or issue that may arise.

With Notify Mi, you can also `attach a file` with your text or email message. The maximum file size allowed is 1 MB and you can use any of the 69 [supported file types](https://github.com/Amark18/notify_mi/blob/c9078313de1ea406ef087217ab11ceddc85d4968/src/notify_mi/helper.py#L64), thus providing you flexibility in the type of attachment you want to include in your messages.

### Table of Contents
- [Purpose](#purpose)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [List of Phone Providers](#list-of-phone-providers)
- [Special Thanks](#special-thanks)

#### Purpose:

Sending notifications through your Gmail account is not a novel idea. Notify Mi is designed to be a `modular` and `reliable` way to send notifications without having to spend time and effort figuring out how to do it each time you want to add this feature to your project. Plus, the implementation process is straightforward and `takes only a couple of minutes`. This way, you can focus on other aspects of your project and `save time`. 

#### Getting Started:

1. Generate an app password for your gmail account by clicking [here](https://myaccount.google.com/apppasswords).  
⤷ place your gmail and app password in a tuple:  
&emsp; &nbsp; &nbsp; ⤷ ("gmail_address", "app_password") ⤶  
⤷ (optional) step by step [guide](https://www.getmailbird.com/gmail-app-password/) on how to generate an app password.
    
2. Install Notify Mi

```python
# 2. install notify_mi using pip
pip install notify_mi

# ✔️ That's it, now you are ready to use
```

#### Usage:

###### Import
```python
from notify_mi import notify
```

###### Text messsage Only
```python
# send only a text message
# include phone_number and phone_provider (see providers list below)
# phone number: "(619) 123-4567", "619-123-4567", or "6191234567" (all acceptable)
notify.send_message("Hello World!", 
       ("gmail", "app_password"), 
       phone_number = "your_number", 
       phone_provider= "your_phone_provider")
```

###### Text + Email
```python
# send text message + email
# include phone_number, phone_provider (see providers list below), and receiver email
# phone number: "(619) 123-4567", "619-123-4567", or "6191234567" (all acceptable)
notify.send_message("Hello World!", 
       ("gmail", "app_password"), 
       phone_number = "your_number", 
       phone_provider= "your_phone_provider", 
       send_to = "email@gmail.com")
```

###### Email Only
```python
# send only email
# include receiver email
notify.send_message("Hello World!", 
       ("gmail", "app_password"), 
       send_to = "email@gmail.com")
```

###### Optional Parameters
```python
# add a subject line to the message
notify.send_message(subject = "EMERGENCY", 
       message = "No sweets detected in fridge!")

# add a file attachment (69 file types supported)
notify.send_message(subject = "I found it", 
       message = "My dream car", 
       file_attachment = "/path/car.png")

# run without blocking main thread
notify.send_message("Hello World!", 
       threaded = True)
```

###### Available Parameters
```python
# this is all the parameters you can use
notify.send_message(threaded = True,
       file_attachment = "/path/to/file"
       phone_number = "your_number", 
       phone_provider = "your_phone_provider", 
       send_to = "email@gmail.com",
       sender_credentials = ("gmail", "app_password"), 
       message = "No sweets detected in fridge!")
```

#### List of Phone Providers
```python
# Select From: 
"AT&T", "Boost Mobile", "C-Spire", "Cricket Wireless", 
"Consumer Cellular", "Google Project Fi", "Metro PCS", 
"Mint Mobile", "Page Plus", "Republic Wireless", "Sprint",
"Straight Talk", "T-Mobile", "Ting", "Tracfone", 
"U.S. Cellular", "Verizon", "Virgin Mobile", "Xfinity Mobile"
```

#### Special Thanks:
[Alfredo Sequeida](https://github.com/AlfredoSequeida) for writing a detailed [article](https://www.alfredosequeida.com/blog/how-to-send-text-messages-for-free-using-python-use-python-to-send-text-messages-via-email/) and for making a great [video](https://www.youtube.com/watch?v=4-ysecoraKo&t=2s) that went step by step on how to send text messages using python. It was very useful for one of my projects so I am adding to what he did so that other people can find it useful.

Alfredo also made a package named [etext](https://github.com/AlfredoSequeida/etext) so check that out!
