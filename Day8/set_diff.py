n_eng = int(input())
Eng = set(map(int, input().split()))
n_frn = int(input())
Frn = set(map(int, input().split()))

print(len(Eng - Frn))

#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
