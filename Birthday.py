from calendar import month
import datetime

# ask the user for thier birthday

day = int(input("Enter your birth day(1-31): "))
month = int(input("Enter your month(1-12)"))
year = int(input("Enter your birth year (e.g., 2000): "))

# getting today's date
today = datetime.datetime.today()

# creating the birthday date for this year

birthday_this_year = datetime.datetime(today.year, month, day)
# checking if the birthday has already passed this year
# if is has passed i will calculate for next year

if birthday_this_year < today:
    birthday_next = datetime.date(today.year + 1, month, day)

else:
    birthday_next = birthday_this_year

# calculate the difference
days_remaining =(birthday_next - today).days

# Calculate weeks + extra days
weeks = days_remaining // 7
extra_days = days_remaining % 7

# get the day of he week 
day_of_the_week = birthday_next.strftime("%A")

#Calculate age
age_next = birthday_next.year - year

print(f"🎉🎉 Your birthday is in {days_remaining} days!")
print(f"📅 It will fall on a {day_of_the_week}.")
print(f"🎂 You will be {age_next} years old.")
print(f"🗓 That is about {weeks} weeks and {extra_days} days from now.")
