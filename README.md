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
| task6.py| Task5: Placeholder for Task6 | [Task06](#6-task5) 

# 1. Helloworld

Filename: helloworld.py (Task01)

Summary: Simple script to output **Hello World** to the terminal window. 

Details: The purpose of this script is to print the string "Hello World!".

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
We assume that the input is indeed 10 characters and no validation on the length is required. We use a simple method of stripping out the last four characters and added 6*"X" to the beginning.

2) The second part of this script is to take in a string of any length and again only printing the last four digits as inputed and replacing the rest with 'X'. We follow the same structure as in part1 above but check the length of the string after it has been inputed to identify how many characters we need to replace (Length-4). We then replace this with the equivalent number of "X" characters and combine with the last 4 to get the result. If 4 or less characters are entered then the code will not seem to do anything - it needs a minimum of 5 characters to work correctly.

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

Details: The script first asks for the user to input any positive integer - note, no validations are performed at this stage so if any other data type is entered the script will fail. This number is appended to the list of numbers.   
A while loop is then used to iterate through a number of if statements until the number is equal to 1.
We first check if the number is even using the modulus operator (%) and if so divide it by 2. If not then we assume it is odd and multiple by 3 and add 1. The resulting number is appended to the list of numbers after each calculation.   
The script cycles through the if statements until the while loop is complete (number = 1) and then prints out the full list of numbers formatted with the asterisk (*) to remove the square brackets.   

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
https://stackoverflow.com/questions/62901226/howto-print-list-without-brackets-and-comma-python - Details on how to remove the square brackets in the output

# 5. weekday

Filename: weekday.py (Task05)

Summary: Placeholder for weekday.py

Details:

Input:
```

```
Sample Output1:
```
Today is a weekday, it's only Wednesday
```
```
Sample Output1:
```
***Need to add once we run on a weekend!
```

Additional Links referenced for this task:   
https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date - to get the numeric value of today's day

# 6. task6

Filename: xxx.py (Task06)

Summary: Placeholder for Task6

Details:




---

**General Links and Sources**  
https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-python-3 - comments in Python   
https://www.markdownguide.org/cheat-sheet - TOC Formatting ideas   
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github - GitHub README formatting   
https://www.w3schools.com/python - for general help on everything python   
https://realpython.com/python-f-strings/ - f strings   
https://stackoverflow.com/questions/57150426/what-is-printf - other uses and examples of f strings   
https://python-markdown.github.io/extensions/fenced_code_blocks/ - using fenced code blocks to display input and output sections