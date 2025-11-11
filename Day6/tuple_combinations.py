from itertools import combinations

N = input()
S = input().split()
K = int(input())
ALL = list(combinations(S, K))
COUNT = sum(1 for UNITS in ALL if 'a' in UNITS)
print(round(COUNT/len(ALL), 4))


#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
