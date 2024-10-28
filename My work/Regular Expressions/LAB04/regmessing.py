#this code will find some text in an access file

import re

#regex = "\[.*\]"
#regex = "^[0-9]+\."
#regex = ":[0-9:]{8}"
#regex ="\w+="
#regex = "^[0-9]+\."
#regex = "\d+$"
regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

filename ="access.cvs"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!=0):
            #print(foundTextList)
            foundText = foundTextList[0]
            print(foundText)
            #if I did not want the [] at the beginning and end
            print(foundText[1:-1])


