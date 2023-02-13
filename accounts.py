# accounts.py
# Author: Phelim Barry
# Purpose: Part1 is to read in a 10 character account number and output the 
# number with the last 4 digits showing as input and the others replaced with XXXXXX
# Part2 is to do likewise with an account number (string) of any length

# Part1: read in the 10 digit account number as a string
acc_num = input("Please enter the 10 digit account number: ")
# strip out and store the last 4 digits to be used in the result
last_4_digits = acc_num[6:]
# Note: This is a simplistic way of replacing the first 6 characters with an X. 
# Note: And only works if the account number is in fact 10 characters
# Add the X's to the last 4 digits
acc_num_masked = 6*"X"+last_4_digits
# Print the result
print (f"\nThe account number in masked format is {acc_num_masked}")

# Part2: read in the account number, which could be any length
# Note: if 4 or less characters are entered then the code will output the number without changes
acc_num2 = input("Please enter the account number (of any length): ")
# get the length of the account number
acc_num2_len = len(acc_num2)
# get the amount of the account number needing to be masked i.e. length-4 
first_part = (acc_num2_len-4)*"X"
# strip out the last 4 digits into a new variable to be used in the output
last_4_digits2 = acc_num2[-4:]
# Combine the part to be masked with the last 4 digits and print the result
acc_num2_masked = first_part+last_4_digits2
print (f"\nThe account number in masked format is {acc_num2_masked}")