## Notify Me
Notify Me makes it easy to send yourself notifcations from your personal projects by utilizing your gmail account. It is very useful when used with your projects in order to create an easy and ***free*** way to send messages in response to events.

Personally, I think Notify Me is very handy when working with IOT devices in order to send messages in response to events such as button clicks, sensor value threshold, and much more. 

Set up:
```python
# 1. navigate to inside your project directory
# 2. clone repo
git clone https://github.com/Amark18/notify_me.git
# 3. go inside directory
cd notify_me
# 4. generate an app password for your gmail account 
# see https://www.getmailbird.com/gmail-app-password/
# 5. add your gmail+password (from step 4), phone number
# and phone provider to notify_me_secrets.py
# That's it, now you are ready to use
```

Implementation:
```python
# import into your own project
from notify_me import notify

# SAMPLE CALLS

# send only a message
notify.send_message("hello world")

# add a subject line to the message
notify.send_message(subject = "EMERGENCY", message = "no sweets detected in fridge!")

# add a file attachment
notify.send_message(subject = "I found it", message = "this is my dream car", file_attachment = "path_to_car_file")

# run without blocking main thread
notify.send_message(message = "hello world", threaded = True)
```
