import numpy

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
arr=numpy.array(arr)
arr=numpy.min(arr,axis=1)
print(max(arr))
#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
