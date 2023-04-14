# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros

# input section 
# input the 1st input as an integer
first_number = int(input("\nInput the first number in Cents: "))
# Add a new line and output the input value in Cents 
print (f"\nThe first amount in Cent is: {first_number}")
# input the 2nd input as an integer
second_number = int(input("\nInput the second number in Cents: "))
# Add a new line and output the input value in Cents 
print (f"\nThe second amount in Cent is: {second_number}")

# calculations
# Add the numbers to get the total (in cents)
num_total = (first_number + second_number)
# define two new variables to store the euro total and cent totals
euro_total = num_total//100 # Using floor division keeps the result as an int
cent_total = num_total%100 # Using the modulo operator to get the remainder keeps the result as an int

# output section
# Add a new line and print the results
print (f"\nThe total is {euro_total} Euro and {cent_total} Cent")
