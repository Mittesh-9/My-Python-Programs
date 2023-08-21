from datetime import datetime, timedelta

present_date = datetime.now()
yesterday = present_date - timedelta(1)
tomorrow = present_date + timedelta(1)

print("Yesterday >", yesterday.strftime('%d-%m-%Y'))
print("Today >", present_date.strftime('%d-%m-%Y'))
print("Tomorrow >", tomorrow.strftime('%d-%m-%Y'))