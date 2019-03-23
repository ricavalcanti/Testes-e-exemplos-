import datetime
dt = datetime.datetime.now()
x = datetime.datetime(dt.year, dt.month, dt.day,dt.hour,dt.minute - 5,dt.second,dt.microsecond)
print(x)