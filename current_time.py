from datetime import datetime

current_date_and_time = datetime.now()
current_time = current_date_and_time.strftime("%H:%M:%S")
print("Current Time is", current_time)