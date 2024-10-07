# reading in the csv as a pandas table

import pandas

FILENAME = "data.csv"
DATADIR = "../datafiles/"

df = pandas.read_csv(DATADIR + FILENAME)
print (df)

