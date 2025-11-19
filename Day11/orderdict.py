from collections import OrderedDict
import sys
ordDict = OrderedDict()
for line in sys.stdin:
    strippedItem = line.strip()    
    splitItem = strippedItem.rsplit(" ", 1)    
    if not strippedItem.isnumeric(): 
        if splitItem[0] not in ordDict.keys():
            ordDict[splitItem[0]] = int(splitItem[1])
        else:
            ordDict[splitItem[0]] += int(splitItem[1])    
for key in ordDict.keys():
    print(key + " " + str(ordDict.get(key)))

#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
