#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    ranks = list(set(ranked)) 
    ranks.sort(reverse=True)
    res = []
    for p in player:
        low, high = 0, len(ranks)
        while low < high:
            mid = (low + high) // 2
            if ranks[mid] > p:
                low = mid + 1
            else:
                high = mid
        res.append(low+1)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
