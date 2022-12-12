## Notify Me
Notify Me makes it easy to send yourself text notifcations from your personal projects by utilizing your gmail account. It is very useful because it gives you an `easy` and `free` way to send messages in response to events.

Personally, I think Notify Me is very handy when working with IOT (Internet of Things) devices in order to send messages in response to events such as sensor value thresholds, sensor detection, sensor errors, daily or custom timed events and much more.

### Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)

#### Getting Started:
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
