import datetime

now = datetime.datetime.now()
print("The current date and time is :", now)

today = datetime.date.today()
print("Today's date is: ", today)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formated:", formatted)