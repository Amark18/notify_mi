## Notify Me
Notify Me makes it easy to send yourself notifcations from your personal projects by utilizing your gmail account. It is very useful when used together with a Raspberry Pi in order to create an easy way and ***free*** way to send messages in response to events from IOT devices. 

How to Use:
```python
# 1. navigate to inside your project directory
# 2. clone repo
git clone https://github.com/Amark18/notify_me.git
# 3. go inside directory
cd notify_me
# 4. generate an app password for your gmail account 
# see https://www.getmailbird.com/gmail-app-password/
# 5. add your gmail+password and phone provider to notify_me_secrets.py

# 6. import into your own project
from notify_me import notify

# That's it, now you are ready to use

# sample calls

# send only a message
notify.send_message("sending a message...")

# add a subject line to the message
notify.send_message(subject = "No more soap", message = "go buy some now")

# add a file attachment
notify.send_message(subject = "I found it", message = "this is my dream car", file_attachment = "path_to_car_file")

# run without blocking main thread
notify.send_message(message = "sending a message...", threaded = True)
```
