# Enter your code here. Read input from STDIN. Print output to STDOUT

# n,s=map(int,input().split())
# sum=0
# for _ in range(n):
#     k=list(map(int,input().split()))
#     k.sort()
#     sum=sum+(k[-1]**2)
# print(sum%s)
K, M = map(int, input().split())
POSSIBLE = {0}
for i in range(K):
    count, *num = list(map(int, input().split())) #1st number in count, and rest in num denoted by *
    vals = {pow(x, 2, M) for x in num} #num will be squared and its MOD M result will be stored in vals
    POSSIBLE = {(a+v)%M for a in POSSIBLE for v in vals} #Every value in vals is added with every value in POSSIBLE and then MOD M on each, finally stored in POSSIBLE
print(max(POSSIBLE))

#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
