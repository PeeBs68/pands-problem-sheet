# squareroot.py
# Author: Phelim Barry
# Purpose: script to use a function to calculate the square root of a positive floating point number
# Using the newton method of estimating square roots.

#NOTE add in actual maths formula and iterative formula (as below)

def sqrt(num):
        #define orig_num (as the original number), because we don't want that to change
        orig_num = num

        #Try a first guess and see the answer is less than the tolerence we set below (will usually be way off)
        #use abs to get a positive value

        while abs(orig_num - num * num) > tolerence_level:
                #get a new guess and try again
                num = (num+(orig_num/num))/2

        #assign the final result to the variable root and return it to the main program
        root = num
        return root

# the actual code
#We can set these two if we want - need to use one or the other (or both)
num_of_iterations = 10 #how many times we want the while loop to run
tolerence_level = .000001 #how close we want the resut to be 

#define input num as a float so decimals can be entered
num = float(input("Please enter a positive number:  "))

#check that the entered number is positive
while num < 0:
        num = float(input("Please try again:  "))

#Call the funtion with additional arguements if need be
root = sqrt(num)

#print out the result to 1 decimal place
print (f"The square Root of {num} is approx. {root:.1f}")
