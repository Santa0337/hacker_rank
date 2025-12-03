import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    d={}
    for i in candles:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d[max(d)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
