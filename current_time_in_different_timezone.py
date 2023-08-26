from datetime import datetime
import pytz

UTC = pytz.utc
IST = pytz.timezone("Asia/Kolkata")

print("UTC in Default Format : ",datetime.now(UTC))
print("IST in Default Format : ",datetime.now(IST))

datetime_utc = datetime.now(UTC)
print("Date & Time in UTC : ",datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_ist = datetime.now(IST)
print("Date & Time in IST : ",datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))