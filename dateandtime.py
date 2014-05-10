# bring in the date and time functions
import datetime
from datetime import *

# Take today's date and format it
formattedtoday = date.today().strftime("%A %B %d %Y")
print ("Today's date is: ", formattedtoday)
today = date.today()

# Take a previous date and format it
previousday = date(1994, 01, 29)
formattedpreviousday = previousday.strftime("%A %B %d %Y")
print ("A previous day is: ", formattedpreviousday)

# calculate the difference between the 2 days
difference = (today - previousday).days
print ("The number of days between the previous day and today is: ", difference)

# calculate the difference using integers
# 1st convert the previous day to an integer
previousdayinteger = date.toordinal(previousday)
# then convert today to an integer
todayinteger = date.toordinal(today)
# calculate the difference between them
integerdifference = todayinteger - previousdayinteger
print ("Using integers, the difference in days between the previous day and today is: ", integerdifference)

formattedtimedate = datetime.now().strftime("%A %B %d %Y %H %M %S")
print ("Today's date and time is: ", formattedtimedate)
