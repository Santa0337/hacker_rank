import numpy as np
n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(n)]
    
print(np.dot(A, B))

#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
