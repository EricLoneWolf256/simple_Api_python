import datetime, pytz

year = int(input())

month = int(input())

day = int(input())

hour = int(input())

minute =int(input())
#converting to date #
users_time = datetime.datetime(year,month,day,hour, minute)

print(users_time.isoformat())

#generate the cairo time zone #

cairo_timezone = pytz.timezone('Africa/cairo')

#convert the users' time zone to cairo#
cairo_time = pytz.utc.localize(users_time).astimezone(cairo_timezone)

print('Cairo Time zone is:', cairo_time.isoformat())

# London time #
london_timezone = pytz.timezone('UTC')

london_time = pytz.utc.localize(users_time).astimezone(london_timezone)

print('London Time zone is:',london_time.isoformat())

#New Delhi time#
delhi_timezone = pytz.timezone('Asian/Kolkata')

delhi_time = pytz.utc.localize(users_time).astimezone(delhi_timezone)

print('New Delhi time zone is:',delhi_time.isoformat())

#Sydney time zone#
sydney_timezone = pytz.timezone('Australia')

sydney_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)

print('Sydney time zone is:',sydney_time.isoformat)