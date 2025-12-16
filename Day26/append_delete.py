#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    count=0
    for i,j in zip(s,t):
        if i == j:
            count+=1
        else:
            break
    mini=(len(s)-count)+(len(t)-count)
    if len(s)+len(t) <= k or (k >= mini and (k - mini) % 2 == 0):
        return "Yes"
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
