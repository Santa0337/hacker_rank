n=int(input())
d={}
for i in range(n):
    k=input()
    if k not in d:
        d[k]=1
    else:
        d[k]+=1

print(len(d))
print(*d.values())

#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
