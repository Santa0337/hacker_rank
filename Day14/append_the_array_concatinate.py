import numpy
n,m,p = map(int,input().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(list(map(int, input().split())))
for i in range(m):
    arr2.append(list(map(int,input().split())))
arr_1 = numpy.array(arr1)
arr_2 = numpy.array(arr2)
print(numpy.concatenate((arr_1, arr_2), axis = 0))

#https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
