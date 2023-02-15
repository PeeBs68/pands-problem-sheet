# collatz.py
# Author: Phelim Barry
# Purpose: <placeholder for now>

# Input a number
number = int(input("Enter a positive number: "))
# While number is not equal to 1 do the below until it is
while (number !=1):
    print (number) # NOTE Seems to get stuck on this...
if (number % 2) == 0:
        newnum=(number/2)
else:
        newnum=(number*3)+1
print (number, newnum)

