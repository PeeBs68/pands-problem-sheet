# plottask.py
# author: Phelim Barry
# Scripts to...

'''
Write a program called plottask.py that displays:

    a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

Some marks will be given for making the plot look nice (legend etc).
'''

#Need to import numpy as x
import numpy as np
import matplotlib.pyplot as plt


count_num = 1000
std_dev = 2
mean = 5
#loc = mean, scale = standard deviation, size = sample size
numbers = np.random.normal(loc=mean, scale=std_dev, size=count_num)

x = np.array(range(0, 10))
print (x)
#Cube x
y = x**3

plt.title("Histogram and Number Plotting")
plt.xlabel("Numbers")
plt.ylabel("Height")

plt.plot(x, y, label ='Y = x3')
plt.hist(numbers, label ='Random Numbers Hist')
plt.legend()
plt.show()

#References
#https://www.w3schools.com/python/matplotlib_pie_charts.asp - plotting and legends etc
#https://stackoverflow.com/questions/27831923/python-random-number-generator-with-mean-and-standard-deviation - mean and standard deviation
