# weekday.py
# Author: Phelim Barry
# Purpose:  outputs whether today is a weekday or not

# Needs some googling to figure out what day today is
# Need to import datetime maybe
# then use date.weekday() which will produce an int value 

# Output1: print ("Yes, unfortunately today is a weekday")
# Output2: print ("It is the weekend, yay!")
#For assignment5 - day of the week
# Getting the day - NOTE Monday = 1, Tuesday = 2, etc
import datetime
#now = datetime.datetime.now()
#print (now)
#today = datetime.datetime.today()
#print (today)
#from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
day = datetime.datetime.today().weekday()
print (day) # use this one
#now, 2 options to know what to print out
#1 create a list ("monday", "Tuesday" etc)
# then match the day with the position in the list
days = ["Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday"]
# print (days[1])
#Or if day number between 0 and 4 then its a weekday else is a weekend
if day >=0 and day <5:
    print (f"Today is a weekday, it's only {days[day]}")
else:
    print (f"Today is {days[day]} so its the weekend!!!")
#print (f"Today is: {days[day]}")

# This is very short, maybe add the actual day from the list as well - something like
#if day >=0 and day <5:
#    print (f"Today is a weekday - it's only {days[day]}")
#else:
#    print ("Its the weekend")