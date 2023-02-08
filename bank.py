# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros and cents
# See readme.md for details on additional sources for example try/except

# input section 
# take the 1st input and validate it is an integer

#NOTE TO SELF eed to remove this and replace with a simple input
while True:
  try:
    num1 = int(input("\nInput the first number in cents: "))
  except ValueError:
    print('Error - Your number must be an integer!')
    continue
  break

print (num1)
# output the input value in Cents and Euros
newnum1 = "{:.2f} Euro"
print("\nYou Entered "+newnum1.format(num1/100))
print("\nYou Entered ",num1,"cent which is",newnum1.format(num1/100))
print("\nYou Entered ",num1,"cent which is",newnum1.format(num1/100))

# take the 2nd input and validate it is an integer
#NOTE TO SELF eed to remove this and replace with a simple input
while True:
  try:
    num2 = int(input("\nInput the second number in cents: "))
  except ValueError:
    print('Error - Your number must be an integer!')
    continue
  break

# output the input value in Cents and Euros
newnum2 = "{:.2f} Euro"
print("\nYou Entered",num2,"cent which is",newnum2.format(num2/100))

# calculations
# add the two numbers and divide the total by 100 to convert to euros
numtotal = (num1 + num2)/100

# output section
# define a new variable to hold the total value and format with 2 decimal places
newnumtotal = "€{:.2f}".format(numtotal)
# Add a new line and print the output
print (f"\nThe total in Euros and Cents is: {newnumtotal}")
