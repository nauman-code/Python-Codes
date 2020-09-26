#Complete the code below. We've gone ahead and created
#variables for the current date and current time. Now,
#we want to print date with the format year/month/day,
#and the time with the format hour:minute:second.
#
#This is a tough one! Think about what we've learned
#about converting and putting together strings.
#Remember, we can add two strings together. For
#example: "5" + "1" = "51".

from datetime import date
import datetime
todays_date = date.today()
current_time = datetime.datetime.now()

#Don't modify the code above!

#Complete the line below to print today's date with the
#form year/month/day. For example, January 15th, 2016
#would be 2016/1/15.
todays_year=todays_date.year
todays_month=todays_date.month
todays_day=todays_date.day
print(str(todays_year)+"/"+str(todays_month)+"/"+str(todays_day))

#Complete the line below to print the current time with
#the form hour:minute:second, such as 12:57:15. Don't worry
#about the leading 0s for single-digit times. If it's
#1:05PM and 7 seconds, the correct answer would be:
#13:5:7 (13 because Python uses 24-hour timeby default).
current_hour=current_time.hour
current_minute=current_time.minute
current_second=current_time.second

print(current_time)