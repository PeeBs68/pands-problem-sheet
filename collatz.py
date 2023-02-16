# collatz.py
# Author: Phelim Barry
# Purpose: input any positive integer, output the values after some calculations
# If the number is odd, multiple by 3 and add 1, if even, divide by 2. And so on until the number is 1

# define a list to hold the results
list_of_nums = []
# Input a number
number = int(input("Please enter a positive integer: "))
# print (int(number))
list_of_nums.append(number)
# While number is not equal to 1 do the below until it is
while number != 1:
# Check if it is divisible by 2 with no remainder, if so then it is Even
    if (number % 2) == 0:
        number = (number/2)
        list_of_nums.append(int(number))
#        print (int(number))
    else: 
# If not divisible by 2 then it must be odd
        number=(number*3)+1
        list_of_nums.append(int(number))
#        print (int(number))
# print ("All Done!")
print (*list_of_nums)

# Link for removing brackets on output
# https://stackoverflow.com/questions/62901226/howto-print-list-without-brackets-and-comma-python
