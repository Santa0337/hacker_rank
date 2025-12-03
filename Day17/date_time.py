#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
def timeConversion(s):
    # Write your code here
    time = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
