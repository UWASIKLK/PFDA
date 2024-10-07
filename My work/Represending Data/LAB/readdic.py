# program read csv file as dictionary object
# Author: Katarina Siklodyova

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting = csv.QUOTE_NONNUMERIC)
    
    total = 0
    count = 0
    for line in reader:
         total += (line['age'])
         count += 1
    print(f"Average is {total/(count)}")