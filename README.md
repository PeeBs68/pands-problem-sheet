Readme.md for pands-problem-sheet  
Author: Phelim Barry  
Overview: This file provides details of each of the individual task files (python files) for the weekly assignments. It also lists the sources of information (URLs) which were used as references. 

Python v3.10.7   
VS Code: 1.74.3

---
**General Links and Sources**  
https://www.markdownguide.org/cheat-sheet - TOC Formatting ideas
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github - GitHub README formatting   
https://www.w3schools.com/python/python_operators.asp - Python Operators   
https://realpython.com/python-f-strings/ - f strings   
https://stackoverflow.com/questions/57150426/what-is-printf - other uses and examples of f strings

---
**Table of Contents**
| Filename | Short Description | Link |
| --- | ---| ---|
| helloworld.py | Task1: Output **Hello World** to the terminal window. | [Task01](#1-helloworld) 
| bank.py| Task2: Take two inputs in Cents, add them and output the result in Euros | [Task02](#2-bank) 
| accounts.py| Task3: Replace characters in a string with 'X' | [Task03](#3-accounts) 
| collatz.py| Task4: Placeholder for Task4 | [Task04](#4-collatz) 
| task5.py| Task5: Placeholder for Task5 | [Task05](#5-task5) 

# 1. helloworld

Filename: helloworld.py (Task01)

Summary: Simple script to output **Hello World** to the terminal window. 

Details: The purpose of this script is to print the string "Hello World!".

# 2. bank

Filename: bank.py (Task02)

Summary: Script to input two integer values, add them together and output the result

Details: The purpose of this script is to prompt the user to input two values (in cents), add the two values together and output the result (in euros). The script is broken down into three sections.
1) Input - prompt the user to input two values in cents. The inputted values are then displayed back to the user. (Note: No validations are added at this stage  - entering a non INT value will cause the script to fail - we could have used ValueError to get around this.)
2) Calculations - in this section the two values are added together and divided by 100 to give a total in Euros (and Cents). When dividing an INT by an INT Python gives it a type of FLOAT so we need to declare it as type INT.
3) Output - the print command is used to output the result back to the terminal. The output is formatted to ensure that two decimal places are displayed. 

Additional Links referenced for this task:  
Information on handling Decimals taken from the following sources to ensure the output had 2 decimal places   https://www.w3schools.com/python/python_string_formatting.asp  and  https://thepythonguru.com/python-string-formatting/


# 3. accounts

Filename: accounts.py (Task03)

Summary: Read in a 10 character account number and output the number with the last 4 digits showing as input and the others replaced with XXXXXX. Do likewise with a string of any length.

Details: This script is split into two sections. 
1) The first part is to take in a 10 character string as input, replace the first six characters with the character 'X' and output the result. 
We assume that the input is indeed 10 characters and no validation on the length is required. We use a simple method of stripping out the last four characters and added 6*"X" to the beginning.

2) The second part of this script is to take in a string of any length and again only printing the last four digits as inputed and replacing the rest with 'X'. We follow the same structure as in part1 above but check the length of the string after it has been inputed to identify how many characters we need to replace (Length-4). We then replace this with the equivalent number of "X" characters and combine with the last 4 to get the result. If 4 or less characters are entered then the code will not seem to do anything - it needs a minimum of 5 characters to work correctly.

Additional Links referenced for this task:  
Details on string slicing from - https://www.w3schools.com/python/python_strings_slicing.asp and examples here https://stackoverflow.com/questions/52408105/masking-part-of-a-string

# 4. collatz

Filename: xxx.py (Task04)

Summary: Placeholder for Task4

Details:

# 5. task5

Filename: xxx.py (Task05)

Summary: Placeholder for Task5

Details: