# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

s,n=input().split()
s=sorted(list(s))
c=sorted(list(combinations_with_replacement(s,int(n))))
for i in c:
    print(''.join(i))


#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
