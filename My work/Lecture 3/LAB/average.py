# program to calculate average of age
# Author: Katarina Siklodyova

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

# this will convert string to integer
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader (fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # firt row ie header now
            pass
        else: # all subsequent rows
            total += int(line[1]) 
        linecount += 1
    print(f"average is {total/(linecount-1)}")

#this use te quote parameter to read int he numbers as floats
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader (fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # firt row ie header no
            pass
        else: # all subsequent rows
            total += (line[1]) 
        linecount += 1
    print(f"average is {total/(linecount-1)}")
