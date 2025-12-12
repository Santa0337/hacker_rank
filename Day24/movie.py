#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#
def is_whole_number(num):
    # Works for int and float
    if isinstance(num, (int, float)):
        return float(num).is_integer()
    return False
    
def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for l in range(i,j+1):
        m=str(l)
        m=m[::-1]
        m=int(m)
        n=(l-m)/k
        if is_whole_number(n):
            count+=1
    return count
    # count = 0
    # for day in range(i, j+1):
    #     if (day-int(str(day)[::-1])) % k == 0:
    #         count += 1
    # return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
