# accounts.py
# Author: Phelim Barry
# Purpose: read in a 10 character account number and output the 
# number with the last 4 digits showing as input and the others replaced with XXXXXX
# Do likewise with a string of any length

# Links
# Details on splicing - https://www.w3schools.com/python/python_strings_slicing.asp


# Part1
# read in the account number as a string (may contain letters and numbers) with 10 characters
# replace the 1st 6 characters with an 'X'
# print the result

acc_num = input("Please enter the 10 digit account number: ")
# strip out the last 4 digits
last_4_digits = acc_num[6:]
first_6_digits = acc_num[0:5]
acc_num_masked = "XXXXXX"+last_4_digits
print (f"\nThe account number in masked format is {acc_num_masked}")

# Part2
# read in the account number as a string (may contain letters and numbers)
# check the length with len
# replace the 1st (len-4) characters with an 'X'
# print the result

acc_num2 = input("Please enter the account number: ")
first_6_digits = acc_num[0:5]
last_4_digits2 = acc_num2[-4:]
# check the length
acc_num_len2 = len(acc_num2)

# amount of account number to be masked
first_part = (acc_num_len2-4)*"X"
# strip out the last 4 digits
last_4_digits2 = acc_num2[-4:]
# Combine part to be masked with the last 4 digits and print the result
acc_num_masked2 = first_part+last_4_digits2
print (f"\nThe account number in masked format is {acc_num_masked2}")