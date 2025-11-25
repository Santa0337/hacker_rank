import re 
n=int(input())
for _ in range(n):
    pattern=re.findall(r'^[+-]?\d*\.\d+$',input())
    if pattern:
        print(True)
    else:
        print(False)


#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
