from flask import Flask
from datetime import datetime, time
from time import sleep

app = Flask(__name__)

@app.route("/")

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

req = datetime.strptime('2020-10-10 14:30:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

while req>now:
    print("There are %d Days %d Hours %d Minutes %d Seconds until the Wedding Ceremony begins!" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
    sleep(1)
    now = datetime.now()

print("Congratulations Mr. and Mrs. Furlow!")
