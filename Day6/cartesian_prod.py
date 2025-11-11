# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=list(product(a,b))
print(*c)
#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
