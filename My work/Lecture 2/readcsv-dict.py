# simpleprogram to read a csv file as a dictionary

import csv
FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting = csv.QUOTE_NONNUMERIC)
    
    total = 0
    for line in reader:
         total += int(line['id'])
         print (line)
   
      