import datetime
today = datetime.datetime.now()
future = today + datetime.timedelta(days=19)
past = today - datetime.timedelta(days=11)
print(today)
print(future)
print(past)