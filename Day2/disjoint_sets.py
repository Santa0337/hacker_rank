n, m = list(map(int, input().split()))
ints = [int(i) for i in input().split()]
A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])
h=0
for j in ints:
    if j in A:
        h+=1
    if j in B:
        h-=1
print(h)

#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
