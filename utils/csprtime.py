import time
import datetime

def to_date_time(timestamp):
    date_format = datetime.datetime.strptime(timestamp[:-5],
    "%Y-%m-%dT%H:%M:%S"
    )
    return date_format

def to_unix(timestamp):
    return time.mktime(to_date_time(timestamp).timetuple())
