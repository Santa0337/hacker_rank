n = int(input())
set_1 = set(map(int, input().split()))

b = int(input())
set_2 = set(map(int, input().split()))

print(len(set_1 | set_2))


#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
