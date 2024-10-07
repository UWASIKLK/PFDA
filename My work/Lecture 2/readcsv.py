# simpleprogram to read a csv file

import csv

FILENAME= "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            #print (f"{line}\n-------------------")
            pass
        else: # all subsequent rows
            total += int(line[1])
            #print (line)
        linecount += 1
    print (f"average is {total/(linecount-1)}")
