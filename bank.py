# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros and cents

# Links
# Information on Decimals taken from the following sources to ensure the output had 2 decimal places 
# (e.g. 200/100 = 2.0. Needed this to show as 2.00)
# https://www.w3schools.com/python/python_string_formatting.asp

# There is a bit in this, break it down into smaller parts, 
# for example read in an integer first, (and print it back out again, 
# then do some arithmetic to it and print, then read in a second one and add the two, 
# and only then look at the formatting of the answer. of course there are many ways of doing this.

# input section 
# take the input, print the value as inputed and also the value converted to euro and cents
# NOTE to self - Add validations for number format - should be an INT and not CHAR etc

num1 = int(input("Input the first number in cents: "))

newnum1 = "You entered €{:.2f} euro"
print(newnum1.format(num1/100))

print(f"\nYou entered {num1} cent which is €" "{:.2f}".format(num1/100) + " Euros")

num2 = int(input("\nInput the second number in cents: "))
print(f"\nYou entered {num2} cent which is €" "{:.2f}".format(num2/100) + " Euros")

# calculations
# divide the total amount by 100 to convert to euros
numtotal = (num1 + num2)/100

# output section
# to ensure we output 2 decimal places
newnumtotal = "{:.2f}".format(numtotal)
print (f"\nThe total in Euros and Cents is: €{newnumtotal}")

# alternatively we could have used the Decimal class from the decimal module for correct rounding/decimal places
# from decimal import Decimal
# decimal_numtotal = Decimal("%.2f" % numtotal)
# print ("€",decimal_numtotal)
