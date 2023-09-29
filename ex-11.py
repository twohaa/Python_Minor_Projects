# Drink Water Reminder


# Write a python program which reminds you of drinking water every hour or two.
# Your program can either beep or send desktop notifications for a specific operating system.


from plyer import notification
import time

REPEAT_INTERVAL = 10  # Repeat frequency in seconds

while True:
    time.sleep(REPEAT_INTERVAL)
    notification.notify(title="Water",
                        message="Hey Twoha Drink Water...",
                        timeout=2)
