# es.py
# Author: Phelim Barry
# Purpose: Write a program that reads in a text file and outputs the number of e's it contains

# use this link - https://www.w3schools.com/python/python_file_open.asp
# this will also be useful - https://realpython.com/read-write-files-python/

#Import the sys module
import sys

#get the filename from the command line
FILENAME = sys.argv[1]

#Note this will be an exact search - i.e. lowercase e only
letter_to_find = "r"
with open(FILENAME, 'r') as f:
        string1 = f.read()

#count the number of e's (or whatever the variable letter_to_fine is set to)
num_of_e = string1.count(letter_to_find)
print (f"The number of {letter_to_find}'s in {FILENAME} is {num_of_e}")

#https://www.geeksforgeeks.org/command-line-arguments-in-python/