
import math
import os
import random
import re
import sys
#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    # Write your code here
    min_l=[scores[0]]
    max_l=[scores[0]]
    min_c=0
    max_c=0
    for i in range(1,len(scores)):
        if scores[i] > max_l[-1]:
            max_c+=1
            max_l.append(scores[i])
        if scores[i] < min_l[-1]:
            min_c+=1
            min_l.append(scores[i])
    return max_c,min_c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
