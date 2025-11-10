# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    j=str(input())
    j=j.split(' ')
    if j[0]=='append':
        d.append(j[1])
    elif j[0]=="appendleft":
        d.appendleft(j[1])
    elif j[0]=="popleft":
        d.popleft()
    elif j[0]=="pop":
        d.pop()
print(' '.join(d))

#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
