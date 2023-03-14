# squareroot.py
# Author: Phelim Barry
# Purpose: script to use a function to calculate the square root of a positive floating point number
# Using the newton method of estimating square roots.

#define the function
def sqrt(num):
        #define orig_num (as the original number), because we don't want that to change
        orig_num = num

        #Try a first guess and see the answer is less than the tolerence we set below (will usually be way off)
        #use abs to use a positive value
        while abs(orig_num - num * num) > tolerence_level:
                #get a new guess and try again
                num = (num+(orig_num/num))/2

        #assign the final result to the variable root and return it to the main program
        root = num
        return root

# the actual code
#set a tolerance level - i.e. how accurate do we want the result to be
tolerence_level = .0001

#define input num as a float so decimals can be entered
num = float(input("Please enter a positive number:  "))

#check that the entered number is positive
while num < 0:
        num = float(input("Please try again:  "))

#Call the funtion with arguement num
root = sqrt(num)

#print out the result to 1 decimal place
print (f"The square Root of {num} is approx. {root:.1f}")
