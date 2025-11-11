# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations
s,n= input().split()
c=sorted(list(permutations(s,int(n))))
for i in c:
    print(''.join(i))

#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
