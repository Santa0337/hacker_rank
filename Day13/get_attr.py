input()
elm = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    op, l = input().split()
    getattr(elm, op)(set(map(int, input().split())))
print(sum(elm))

#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
