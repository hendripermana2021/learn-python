import datetime

x = datetime.datetime.now()
new_date = datetime.datetime(2020, 5, 17)
print("Current date and time:", x)
print(x.year)
print(x.month)
print(x.timestamp())
print(x.strftime("%A"))
print(x.strftime("%B"))
print("new date", new_date)