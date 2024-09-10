import datetime

date = datetime.date(2025, 2, 15)

print(date)

today = datetime.date.today()

print(today)

time = datetime.time(12, 30, 0)
print(time)

time_now = datetime.datetime.now()


time_now = time_now.strftime("%H:%M:%S %m-%d-%Y")

print(time_now)


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print('Target date has passed')
else:
    print('Target date has not passed')