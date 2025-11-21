a=set(map(int,input().split()))
n=int(input())
for _ in range(n):
    b=set(map(int,input().split()))
    if(not(a > b)):
        print(False)
        break
else:
    print(True)

#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
