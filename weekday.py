# weekday.py
# Author: Phelim Barry
# Purpose: outputs whether today is a weekday or not

# Need to import the datetime module
import datetime
# Create a list of days 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Returns a numeric value for today's day: 0 = Monday, 1 = Tuesday etc.
day = datetime.datetime.today().weekday()
# Check the number and print out it's equivilent from list of days
if day >=0 and day <5: # It's a weekday
    print (f"Today is a weekday, it's only {days[day]} unfortunately!")
else: # If not a week day then it must be the weekend
    print (f"Today is {days[day]} so its the weekend!!!")
