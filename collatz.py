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

# Might be able to reuse some of this...
b = []
print ('What is Sarahs age?')
isCorrect = False
while isCorrect == False:
    response = int(input("?"))
    b.append(response)
    if int(response) == 21:
        isCorrect = True
        print ('Yep, thats right, well done')
        print ('You tried...' + str(b))
        print (f"You tried...{b}")
    else:
        print ('Nope, try again')

        # useful Links
        # https://www.w3schools.com/python/python_conditions.asp If..Else etc
        # 