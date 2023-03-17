# plottask.py
# author: Phelim Barry
# Script to plot a histogram and a function on the same plot

#Need to import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

#1st plot: Histogram
#define limits/values for the numbers generation 
count_num = 1000
std_dev = 2
mean = 5
#create random and normalised values for histogram
#loc = mean, scale = standard deviation, size = sample size
numbers = np.random.normal(loc=mean, scale=std_dev, size=count_num)


#2nd plot: the function h(x)=x3
#generate an array of numbers for x with a range of 0 to 10. 
x = np.array(range(11))
#Cube x for y value
y = x**3

#define titles and labels for the plot
plt.title("Histogram and Function Plotting")
plt.xlabel("X")
plt.ylabel("Y (X cubed)")

#define the lables to be used for the legend
plt.hist(numbers, label ='Random Numbers Histogram')
plt.plot(x, y, label ='Y = X cubed')
plt.legend()

#Print the plot. Note, the terminal will freeze while the plot is open
plt.show()
