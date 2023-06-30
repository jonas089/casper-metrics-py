import time
import datetime

def dateTime(timestamp):
    date_format = datetime.datetime.strptime(timestamp[:-5],
    "%Y-%m-%dT%H:%M:%S"
    )
    return date_format

def unixTime(timestamp):
    return time.mktime(to_date_time(timestamp).timetuple())
