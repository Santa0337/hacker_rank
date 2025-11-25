import numpy
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A,B))
print(numpy.outer(A,B))

#https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
