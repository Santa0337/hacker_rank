import numpy

n,m = map(int,input().split(' '))
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
print(numpy.transpose(arr))
arr_flat = numpy.array(arr)
print(arr_flat.flatten())

#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
