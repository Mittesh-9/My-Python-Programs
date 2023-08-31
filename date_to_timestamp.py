import time
import datetime

string = "01/01/2023"

element = datetime.datetime.strptime(string,"%d/%m/%Y")

tuple = element.timetuple()
timestamp = time.mktime(tuple)

print(timestamp)