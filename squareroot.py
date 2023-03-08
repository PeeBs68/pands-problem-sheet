# squareroot.py
# Author: Phelim Barry
# Purpose: script to use a function to calculate the square root of a positive floating point number
# Using the newton method of estimating square roots.

# Minute 17 of this vid has some ideas - https://www.youtube.com/watch?v=szQUIRPrAgQ
# Formula here https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# Youtube vid showing the maths in plain English - https://www.youtube.com/watch?v=2158QbsunA8

#NOTE add in actual maths formula and iterative formula (as below)

def sqrt(num):
        #define tempnum, because we need two versions of num as such
        tempnum = num
        #Try a first guess and see if it is less than the tolerence we set below (will usually be way off)
        #use abs to get a positive value
        while abs(tempnum - num * num) > tolerence_level:
                #get a new guess and try again
                num = (num+(tempnum/num))/2
                print (num) # Just for testing - take it out later
                root = num
                print (root) # Just for testing - take it out later
        return root

# the actual code
#We can set these two if we want - need to use one or the other (or both)
num_of_iterations = 10
tolerence_level = .000001
#define input num as a float so decimals can be entered
num = float(input("Please enter a positive number:  "))
#Run the funtion with additional arguements if need be
root = sqrt(num)
#print out the result to 1 decimal place
print (f"The square Root of {num} is approx. {root:.1f}")
