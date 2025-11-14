m=int(input())
a = set(map(int,input().split()))
n = int(input())
b = set(map(int,input().split()))
c=a.difference(b)
d=b.difference(a)
e=set(sorted(c.union(d)))
for i in e:
    print(i)


#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
