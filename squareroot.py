# squareroot.py
# Author: Phelim Barry
# Purpose: script to use a function to calculate the square root of a positive floating point number
# look at the newton method at estimating square roots.
# Minute 17 of this vid has some ideas - https://www.youtube.com/watch?v=szQUIRPrAgQ
# Formula here https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# Youtube vid showing the maths in plain English - https://www.youtube.com/watch?v=2158QbsunA8

#NOTE add in actual maths formula and iterative formula (as below)

def sqrt(num):
        tempnum = num
        #use abs to get a positive value
        while abs(tempnum - num * num) > tolerence_level:
                #get a new guess and try again
                num = (num+(tempnum/num))/2
                print (num)
                root = num
#                print (root)
        return root

# the actual code
#We can set these two if we want or just ignore them
num_of_iterations = 10
tolerence_level = .000001
#define as a float so decimals can be entered
num = float(input("Please neter a positive number:  "))
#Run the funtion with arguements if need be
root = sqrt(num)
#print (f"Answer = {newnumber}")
print (f"The square Root of {num} is approx. {root:.1f}")
