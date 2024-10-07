# program to modify header
# Author: Katarina Siklodyova

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader (fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # firt row ie header now
            print (f"{line}\n...................")
        else: # all subsequent rows
            print(line)
        linecount += 1
    