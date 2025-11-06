#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    prev_times = []
    total_prev_times = 0
    count = 0
    iteration = 0
    
    for time in responseTimes: 
        iteration += 1		
        if iteration == 1:
            prev_times.append(time)
            total_prev_times += time           
        elif iteration == 2:
            if time > total_prev_times:
                count += 1
            prev_times.append(time)
            total_prev_times += time           
        else:
            if time > total_prev_times / len(prev_times):
                count += 1
            prev_times.append(time)
            total_prev_times += time
    
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)

#https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
