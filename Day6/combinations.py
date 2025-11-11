# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
s,n=input().split()
s=sorted(list(s))
for j in range(1,int(n)+1):
    c=list(combinations(s,int(j)))
    for i in c:
        print(''.join(i))

#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
