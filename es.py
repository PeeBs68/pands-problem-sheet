# es.py
# Author: Phelim Barry
# Purpose: Write a program that reads in a text file and outputs the number of e's it contains

#Import the sys module, used for command line arguements
import sys

#Get the filename from the command line - argv[1] contains the 1st arguement passed to the script (i.e. filename)
FILENAME = sys.argv[1]

#Define the letter we want to find and count
letter_to_find = "e"

#Initialise a counter
counter=0

#Open the file in read mode
with open(FILENAME) as r:
    #Read in the contents line by line and update the counter with the number of occurances
    for line in r:
        counter = counter+line.count(letter_to_find)

#Print the final counter value
print (f"The number of {letter_to_find}'s in {FILENAME} is {counter}")

