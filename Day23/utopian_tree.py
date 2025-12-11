#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    if n == 0:
        return 1

    doubleCycle = n if n % 2 else n - 1
    treeLength = sum(2** (i+1) for i in range((doubleCycle//2)+1))
    
    return treeLength if n % 2 else treeLength + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
