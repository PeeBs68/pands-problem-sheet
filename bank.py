# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros and cents
# See readme.md for details on additional sources

# input section 
# take the input, print the value as inputed and also the value converted to euro and cents
# take the 1st number and validate it is an integer - if not, ask for it to be re-entered
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

# this section will input the 2nd number and validate it is an integer - if not the user will be asked to enter it again
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
# add the two numbers and divide the total by 100 to convert to euros
numtotal = (num1 + num2)/100

# output section
# define a new variable to hold the total value with 2 decimal places
newnumtotal = "{0:.2f}".format(numtotal)
# Add a new line and print the output
print (f"\nThe total in Euros and Cents is: €{newnumtotal}")
