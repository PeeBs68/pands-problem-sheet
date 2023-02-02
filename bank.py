# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros and cents

# Links
# Information on Decimals taken from the following sources to ensure the output had 2 decimal places 
# (e.g. 200/100 = 2.0. Needed this to show as 2.00)
# https://stackoverflow.com/questions/5202233/how-to-change-39-54484700000000-to-39-54-and-using-python
# https://tutorial.eyehunts.com/python/how-to-display-2-decimal-places-in-python-example-code/ and
# https://www.pythontutorial.net/advanced-python/python-decimal/

# There is a bit in this, break it down into smaller parts, 
# for example read in an integer first, (and print it back out again, 
# then do some arithmetic to it and print, then read in a second one and add the two, 
# and only then look at the formatting of the answer. of course there are many ways of doing this.

# input section 
# take the input, print the value as inputed and also converted to euro and cents
# NOTE to self - Add validations for number format - should be an INT and not CHAR etc

num1 = int(input("Input the first number in cents: "))
print(f"\nYou entered {num1} cent which is €" "{:.2f}".format(num1/100) + " in Euros and Cents")
num2 = int(input("\nInput the second number in cents: "))
print(f"\nYou entered {num2} cent which is €" "{:.2f}".format(num2/100) + " in Euros and Cents")

# calculations

numtotal = (num1 + num2)/100

# output section

# print (f"The total is: €{numtotal}") This would not necessarily print 2 decimal places

#to ensure we output 2 decimal places
newnumtotal = "{:.2f}".format(numtotal)
print (f"\nThe total in Euros and Cents is: €{newnumtotal}")

# alternatively we could have used the Decimal class from the decimal module for correct rounding/decimal places
# from decimal import Decimal
# decimal_numtotal = Decimal("%.2f" % numtotal)
# print ("€",decimal_numtotal)
