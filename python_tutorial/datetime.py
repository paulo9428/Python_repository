import datetime

now = datetime.datetime.now()
# now.year, now.month, now.day, now.hour, now.minute, now.second
now.strftime('%Y-%m-%d %H:%M:%S')
now.strftime('%Y{} %m{} %d{} %H{} %M{}'.format(*"년월일시분"))

now + datetime.timedelta(weeks=1) # days, hours, minutes, seconds
now.replace(year = (now.year + 1))
