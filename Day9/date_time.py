#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1: str, t2: str) -> str:
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta_seconds = abs(int((dt1 - dt2).total_seconds()))
    return str(delta_seconds)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
#https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
