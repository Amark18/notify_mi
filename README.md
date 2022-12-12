## Notify Me
Notify Me simplifies sending yourself text notifcations from your personal projects by utilizing your gmail account. It is a convenient and cost-effective solution with the goal of providing you an `easy` and `free` way to send messages in response to events.

It is particularly useful when working with IOT devices. It can allow you to receive messages in response to events such as when a sensor value reaches a certain threshold, when a sensor detects something, when a sensor encounters an error, or when a daily or custom timed event occurs. This makes it easy to keep track of what is happening with your IOT device and react to any change or issue that may arise.

With Notify Me, you can also `attach files` to your messages. The maximum file size allowed is 1MB and you can use any of the 69 supported file extensions, thus providing you flexibility in the type of attachment you can include in your messages.

### Table of Contents
- [Purpose](#purpose)
- [Getting Started](#getting-started)
- [Usage](#usage)

#### Purpose:

Sending notifications through your Gmail account is not a novel idea. Notify Me is designed to be a `modular` and `reliable` way to send notifications without having to spend time and effort figuring out how to do it each time you want to add this feature to your project. Plus, the implementation process should be straightforward and `take only a few minutes`. This way, you can focus on other aspects of your project and save time.

#### Getting Started:

To add Notify Me to your project, place in your top level directory.  
> Your_Project  
> &emsp; &#x21B3; ✔️ notify_me  
> &emsp; &#x21B3; your files  
> &emsp; &#x21B3; a directory  
> &emsp; &emsp; &#x21B3; ❌ notify_me

```python
# 1. navigate to inside your project directory
# 2. clone repo
git clone https://github.com/Amark18/notify_me.git
# 3. go inside directory
cd notify_me
# 4. generate an app password for your gmail account 
# see https://www.getmailbird.com/gmail-app-password/
# 5. add your gmail + password (from step 4), phone number
# and phone provider to notify_me_secrets.py
# That's it, now you are ready to use
```

#### Usage:

```python
# import into your own project
from notify_me import notify

# send only a message
notify.send_message("hello world")

# add a subject line to the message
notify.send_message(subject = "EMERGENCY", message = "no sweets detected in fridge!")

# add a file attachment
notify.send_message(subject = "I found it", message = "this is my dream car", file_attachment = "path_to_car_file")

# run without blocking main thread
notify.send_message("hello world", threaded = True)
```
