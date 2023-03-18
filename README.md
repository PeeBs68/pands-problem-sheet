Readme.md for pands-problem-sheet  
Author: Phelim Barry  
Overview: This file provides details of each of the individual task files (python files) for the weekly assignments. It also lists the sources of information (URLs) which were used as references. 

Python v3.10.7   
VS Code: 1.74.3

---

**Table of Contents**
| Filename | Short Description | Link |
| --- | ---| ---|
| helloworld.py | Task1: Output **Hello World** to the terminal window. | [Task01](#1-Helloworld) 
| bank.py| Task2: Take two inputs in Cents, add them and output the result in Euros | [Task02](#2-Bank) 
| accounts.py| Task3: Masking characters in a string with the value 'X' | [Task03](#3-Accounts) 
| collatz.py| Task4: The Collatz Conjecture | [Task04](#4-Collatz) 
| weekday.py| Task5: To output what day of the week it is | [Task05](#5-Weekday) 
| squareroot.py| Task6: To calculate the square root using the Newton method | [Task06](#6-squareroot) 
| es.py| Task7: Count the number of occurrances of a letter in a file, using command line arguements | [Task07](#7-es) 
| plottask.py| Task8: Placeholder for Task08 | [Task08](#8-plottask) 

# 1. Helloworld

Filename: helloworld.py (Task01)

Summary: Simple script to output **Hello World** to the terminal window. 

Details: The purpose of this script is to print the string "Hello World!". No input is required.

Input:
```

```
Output:
```
Hello World!
```

# 2. Bank

Filename: bank.py (Task02)

Summary: Script to input two integer values, add them together and output the result

Details: The purpose of this script is to prompt the user to input two values (in cents), add the two values together and output the result (in euros). The script is broken down into three sections.
1) Input - prompt the user to input two values in cents. The inputted values are then displayed back to the user. (Note: No validations are added at this stage  - entering a non INT value will cause the script to fail - we could have used ValueError to get around this.)
2) Calculations - in this section the two values are added together and divided by 100 to give a total in Euros (and Cents). When dividing an INT by an INT Python gives it a type of FLOAT so we need to declare it as type INT.
3) Output - the print command is used to output the result back to the terminal. The output is formatted to ensure that two decimal places are displayed. 

Sample Input:
```python
Input the first number in cents: 50012
Input the second number in cents: 32290
```
Sample Output:
```
The first number in Cent is: 50012
The second number in Cent is: 32290

The total in Euros and Cents is: €823.02
```

Additional Links referenced for this task:  
https://www.w3schools.com/python/python_string_formatting.asp - string formatting   
https://thepythonguru.com/python-string-formatting/ - more string formatting


# 3. Accounts

Filename: accounts.py (Task03)

Summary: Read in a 10 character account number and output the number with the last 4 digits showing as input and the others replaced with XXXXXX. Do likewise with a string of any length.

Details: This script is split into two sections. 
1) The first part is to take in a 10 character string as input, replace the first six characters with the character 'X' and output the result. 
Using a while loop we validate that the account number entered is in fact 10 characters. We use a simple method of string slicing to strip out the last four characters and added 6*"X" to the beginning. Using hard coding of 6*"X" works because we have enforced the entry of 10 characters. The method used in section 2 below would also work for this section and may be a better way of doing it.

2) The second part of this script is to take in a string of any length and again only printing the last four digits as inputed and replacing the rest with 'X'. We follow the same structure as in part1 above but remove the length validation. We check the length of the string after it has been input to identify how many characters we need to replace (Length-4). We then replace this with the equivalent number of "X" characters and combine with the last 4 to get the result. If 4 or less characters are entered then the code will not seem to do anything - it needs a minimum of 5 characters to work correctly.

Sample Input1:
```python
Please enter the 10 digit account number: 1234ABCD56
```
Sample Output1:
```
The account number in masked format is XXXXXXCD56
```

Sample Input2:
```python
Please enter the account number (of any length): ABDC1234EFGHIJ
```
Sample Output2:
```
The account number in masked format is XXXXXXXXXXGHIJ
```
Additional Links referenced for this task:  
https://www.w3schools.com/python/python_strings_slicing.asp - details on string slicing   
https://stackoverflow.com/questions/52408105/masking-part-of-a-string - string slicing examples

# 4. Collatz

Filename: collatz.py (Task04)

Summary: Script to input a positive integer and apply mathematical operations to it until the nuumber equals 1 - AKA the Collatz Conjecture. Upon finishing, the entire list of generated values are printed.

Details: The script first asks for the user to input any positive integer. The number is checked to confirm it is a positive integer or else the user will be asked to enter another number. This number is appended to the list of numbers.   
A while loop is then used to iterate through a number of if statements until the number is equal to 1.
We first check if the number is even using the modulus operator (%) and if so divide it by 2. If not then we assume it is odd and multiple by 3 and add 1. The resulting number is appended to the list of numbers after each calculation.   
The script cycles through the if statements until the while loop is complete (number = 1) and then prints out the full list of numbers formatted using end = " " to seperate the values with a space rather than the default comma.   

Sample Input:
```python
Please enter a positive integer: 34
```
Sample Output:
```
34 17 52 26 13 40 20 10 5 16 8 4 2 1
```

Additional Links referenced for this task:   
https://www.w3schools.com/python/python_conditions.asp - If, elif and else information   
https://www.w3schools.com/python/python_while_loops.asp - while loops explained   
https://realpython.com/python-print/ - Details on how to remove the square brackets in the output by supressing the default newline after a print statement

# 5. weekday

Filename: weekday.py (Task05)

Summary: Script to output what day today is.

Details: the script starts by importing the datetime module and then creating a list of week days (Monday -> Sunday). Using the datetime modue we imported, we can identify a numeric value for today's day. Cross checking this against the list of days where 0 = Monday, 1 = Tuesday etc. we can identify what day it is at the time of running the script. We then print the day of the week based on the day value - if it is between 0 and 4 inclusive then it's a weekeday, or else it must be a weekend day. No input is required to run this script.

Input:
```

```
Sample Output1:
```
Today is a weekday, it's only Wednesday
```

Sample Output2:
```
Today is Saturday so it's the weekend!!!
```

Additional Links referenced for this task:   
https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date - to get the numeric value of today's day

# 6. squareroot

Filename: squareroot.py (Task06)

Summary: Script to calculate the square root of a number using the Newtons method

Details: The purpose of this script is to calculate the square root of a number input by the user using the Newton's method for square roots. This method starts with an initial guess of the square root and uses increasingly better approximations of the root until a final answer that is sufficiently precise is found.   

Input validation is included to ensure a positive float value is entered by the user by checking if the number is greater than 0. using a while loop the script will iterate until a positive value is entered.
We also define a variable for tolerance level which is how accurate we want our result to be. A level of .0001 is deemed appropriate in this case.  

We create a new function, sqrt(num), and once called with the input number included as an arguement, the function tries an initial guess at the answer and compares it against the tolerance level. It then iterates through a while loop, applying the square root formula until a result is found within the tolerance level. This result is then returned to the script for printing with the value formatted with one decimal place using :.1f.

Sample Input:
```
Please enter a positive number:  14.5
```
Sample Output:
```
The square Root of 14.5 is approx. 3.8
```

Additional Links referenced for this task:   
https://www.youtube.com/watch?v=2158QbsunA8 - maths formula for Newtons method   
https://www.youtube.com/watch?v=szQUIRPrAgQ - Newtons method showing use of levels of tolerance and iterations   
https://stackoverflow.com/questions/55888265/time-complexity-for-square-root-using-newtons-method - formula for generating new iterations of the guess   
https://www.sciencedirect.com/topics/mathematics/newton-raphson-method - suggestion for tolerance level to use.


# 7. es

Filename: es.py (Task07)

Summary: Script to count the number of 'e's in a file.

Details: the purpose of this script is to count the number of occurances of the letter e in a file. The filename is not hardcoded into the script but is given as an arguement through the command line and using sys.argv[1] we assign it to the FILENAME variable. (sys.argv[0] would be the actual script name). We import the sys module to enable the use of sys.argv().

In this script we assign the letter to be found in a variable instead of hardcoding it so it can be changed easier if need be. Next step is to open the file in read only mode 'r' using with open (which also handles closing the file correctly after we are finished with it) and read in the contents as a string.   

Finally we count the occurances of the variable in question using count() (i.e. 'e' in this case) and print the result.

Sample Input:
```
python3 es.py readme.md
```
Sample Output:
```
The number of e's in readme.md is 782
```

Assumptions:   
The script will look for an exact match of the letter in question so will not return occurances of upper case letters if looking for lower case letters and vice versa. upper() or lower() could have been used to convert the contents as needed if this was a requirement.   
Also, we do not validate if the filename entered exists or not. If an invalid filename is entered then the script will fail. 

Additional Links referenced for this task:   
#https://www.geeksforgeeks.org/command-line-arguments-in-python/ - details on using command line arguements   
https://www.w3schools.com/python/python_file_open.asp - openng and reading from files   
https://realpython.com/read-write-files-python/ - details on opening and closing files   


# 8. plottask

Filename: plottask.py (Task08)

Summary: Script to plot a histogram and a function on the same plot

Details: The purpose of this script is twofold: Firstly it is designed to plot a histogram of 1000 randomly generated numbers with a mean of 5 and a standard deviation of 2. Secondly it will plot the function h(x) = y cubed in the range of 0 - 10. Both are plotted on the same set of axes.   

The modules numpy and matplotlib are both imported as "np" and "plt" respectively, to use the array handling and plotting functions.   

For the histogram we create variables and assign values to them for the count of numbers to be used along with the mean and standard deviation. We then use these in np.random.normal() to create a list of random, normalised numbers for our histogram.   

Then for the function, we create an array of values for the x value using np.array() giving it a value of 11 which uses the defaults for the function to create the array with values of 0 to 10. Then we create a new variable to store the x cubed value.   

Next, using the features of matplotlib we create lables, legend, title etc. for the plot and finally, using plt.show() we display the plot.

Terminal Command:
```
$ python3 plottask.py
```

Sample User Input:
```

```
Sample Output:
```

```


Additional Links referenced for this task:   
https://www.w3schools.com/python/matplotlib_pie_charts.asp - plotting and legends etc.   
https://www.w3schools.com/python/ref_func_range.asp - using range()   
https://stackoverflow.com/questions/27831923/python-random-number-generator-with-mean-and-standard-deviation - mean and standard deviation   


---

**General Links and Sources**  
https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-python-3 - comments in Python   
https://www.markdownguide.org/cheat-sheet - TOC Formatting ideas   
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github - GitHub README formatting   
https://www.w3schools.com/python - for general help on everything python   
https://realpython.com/python-f-strings/ - f strings   
https://stackoverflow.com/questions/57150426/what-is-printf - other uses and examples of f strings   
https://python-markdown.github.io/extensions/fenced_code_blocks/ - using fenced code blocks to display input and output sections