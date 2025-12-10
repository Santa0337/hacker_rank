#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def formingMagicSquare(s):
    lu_1 = [[8,1,6], [3,5,7], [4,9,2]]
    lu_2 = [[6,1,8], [7,5,3], [2,9,4]]
    lu_3 = [[4,9,2], [3,5,7], [8,1,6]]
    lu_4 = [[2,9,4], [7,5,3], [6,1,8]]
    lu_5 = [[8,3,4], [1,5,9], [6,7,2]]
    lu_6 = [[4,3,8], [9,5,1], [2,7,6]]
    lu_7 = [[6,7,2], [1,5,9], [8,3,4]]
    lu_8 = [[2,7,6], [9,5,1], [4,3,8]]    
    var = [
        lu_1, lu_2, lu_3, lu_4, lu_5, lu_6, lu_7, lu_8
    ]
    diff = []
    for v in var:
        temp = 0
        for v_, s_ in zip(v, s):
            for v__, s__ in zip(v_, s_):
                if v__ != s__:
                    temp += abs(v__ - s__)
        diff.append(temp)
    
    diff = sorted(diff)
    return diff[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
