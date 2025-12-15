#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    position=0
    for i in range(0,len(c)):
        position = (position+k)%len(c) 
        e=e-1
        if c[position] == 1 :
            e=e-2 # 1 for the jump and one for the energy down
        print(e,position,c[position])
        if position == 0:
            break
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
