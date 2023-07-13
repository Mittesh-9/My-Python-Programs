import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 20 and plugged != True:
    notification.notify(
        title='Battery Low',
        message=str(percent) + '% Battery remaining!',
        timeout=5  # Duration is in seconds
    )