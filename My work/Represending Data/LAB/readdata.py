# program will read data from csv file
#Author: Katarina Siklodyova

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader (fp, delimiter=",")
    for line in reader:
        print (line)