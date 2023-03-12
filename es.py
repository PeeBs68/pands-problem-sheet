# es.py
# Author: Phelim Barry
# Purpose: Write a program that reads in a text file and outputs the number of e's it contains

# use this link - https://www.w3schools.com/python/python_file_open.asp
# this will also be useful - https://realpython.com/read-write-files-python/

#Import the sys module
import sys

#get the filename from the command line - argv[0] would be the actual py file, argv[1] is the filename
FILENAME = sys.argv[1]

#Note this will be an exact search - i.e. lowercase e only
letter_to_find = "r"
#Open the file in read mode and read in the contents as a string

with open(FILENAME, 'r') as f:
        string1 = f.read()

#count the number of e's (or whatever the variable letter_to_find is set to)
var1 = string1.count(letter_to_find)
print (f"The number of {letter_to_find}'s in {FILENAME} is {var1}")

#https://www.geeksforgeeks.org/command-line-arguments-in-python/ - for the command line arguements