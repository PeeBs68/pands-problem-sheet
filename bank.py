# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros

# input section 
# input the 1st input as an integer
first_number = int(input("\nInput the first number in cents: "))
# Add a new line and output the input value in Cents 
print (f"\nThe first amount in Cent is: {first_number}")
# input the 2nd input as an integer
second_number = int(input("\nInput the second number in cents: "))
# Add a new line and output the input value in Cents 
print (f"\nThe second amount in Cent is: {second_number}")

# calculations
# add the two numbers and divide the total by 100 to convert to euros
numtotal = (first_number + second_number)/100

# output section
# define a new variable, numtotal to hold the total value and format with 2 decimal places
numtotal = "€{:.2f}".format(numtotal)
# Add a new line and print the output
print (f"\nThe total in Euros and Cents is: {numtotal}")
