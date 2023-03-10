# es.py
# Author: Phelim Barry
# Purpose: Write a program that reads in a text file and outputs the number of e's it contains

# Get the file name ...The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up
# Maybe here - https://www.geeksforgeeks.org/command-line-arguments-in-python/
# use this link - https://www.w3schools.com/python/python_file_open.asp
# this will also be useful - https://realpython.com/read-write-files-python/

'''To make that possible sys method was imported. Using the sys.argv[1] variable, it is defined that the filename is second argument when calling a program ( sys.argv[0] is the program we are trying to start ).
References for this part of program go to Python documentation and Geeksforgeeks.org.

With the open( filename,'r' ) function we are opening a file that we called in the command line argument, and making it available just for reading. For counting the lower case letter 'e' the method count() was used, and the argument is a string "e". Reference for the count() method is Programiz.
'''

#Print out the number of e's