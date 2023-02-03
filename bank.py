# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros and cents

# Links
# Information on Decimals taken from the following source to ensure the output had 2 decimal places 
# https://www.w3schools.com/python/python_string_formatting.asp
# (e.g. 200/100 = 2.0. Needed this to show as 2.00)

# Details on how to handle non integer inputs taken form Stackoverflow
# https://stackoverflow.com/questions/62768087/how-can-i-not-allow-letters-and-only-allow-numbers-in-an-input-on-python-3


# There is a bit in this, break it down into smaller parts, 
# for example read in an integer first, (and print it back out again, 
# then do some arithmetic to it and print, then read in a second one and add the two, 
# and only then look at the formatting of the answer. of course there are many ways of doing this.

# input section 
# take the input, print the value as inputed and also the value converted to euro and cents

# this section will validate the input is an integer - if not the user will be asked to enter it again
while True:
  try:
    num1 = int(input("\nInput the first number in cents: "))
  except ValueError:
    print('Error - Your number must be an integer!')
    continue
  break

# above section replaces this simplier line although with no validations
# num1 = int(input("Input the first number in cents: "))

newnum1 = "€{:.2f} Euro"
#print(newnum1.format(num1/100))
print("\nYou Entered",num1,"cent which is",newnum1.format(num1/100))
# The above 2 lines OR 1 Below do the same thing
# print(f"\nYou entered {num1} cent which is €" "{:.2f}".format(num1/100) + " Euros")

while True:
  try:
    num2 = int(input("\nInput the second number in cents: "))
  except ValueError:
    print('Error - Your number must be an integer!')
    continue
  break
# above section replaces this line
# num2 = int(input("\nInput the second number in cents: "))

newnum2 = "€{:.2f} Euro"
#print(newnum2.format(num2/100))
print("\nYou Entered",num2,"cent which is",newnum2.format(num2/100))
# The above 2 lines OR 1 Below do the same thing
# print(f"\nYou entered {num1} cent which is €" "{:.2f}".format(num1/100) + " Euros")


# calculations
# divide the total amount by 100 to convert to euros
numtotal = (num1 + num2)/100

# output section
# to ensure we output 2 decimal places
newnumtotal = "{:.2f}".format(numtotal)
print (f"\nThe total in Euros and Cents is: €{newnumtotal}")
