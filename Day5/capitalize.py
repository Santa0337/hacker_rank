#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=[i for i in s.split(' ')]
    k=[]
    for i in l:
        k.append(i.capitalize())
    return ' '.join(k)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
