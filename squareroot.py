# squareroot.py
# Author: Phelim Barry
# Purpose: script to use a function to calculate the square root of a positive floating point number
# look at the newton method at estimating square roots.
# Minute 17 of this vid has some ideas - https://www.youtube.com/watch?v=szQUIRPrAgQ

def sqrt(number, num_of_iterations, tolerence_level):
    for x in range (num_of_iterations):
        #formula here...x= something
        newnumber = number+1
        number=number+1
        #while abs(x) is > tolerence_level:
    return newnumber

# the actual code
#We can set these two if we want or just ignore them
num_of_iterations = 10
tolerence_level = 0
number = int((input("Enter a number:  ")))
#Run the funtion with arguements if need be
newnumber=sqrt(number,num_of_iterations,tolerence_level)
print (f"Answer = {newnumber}")