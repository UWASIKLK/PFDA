#this is code anonymise the sub domains of ip addresses

import re

#regex = "\d{1,3}\.\d{1,3}" #this will find athoer numbers aprat from ips
regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # we make a group at the begginnig to keep

replacementText = "\\1XXX.XX" # note the space at the end to match amove
filename ="access.cvs"
outputFileName = "anomisiedIPs.txt"

with open(filename) as inputFile: 
    with open(outputFileName, 'w') as outputFile:
        for line in  inputFile:
            # for debugging
            # foundText = re.search(regex, line).group()
            # print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)
            