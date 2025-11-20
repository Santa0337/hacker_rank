n,m=map(int,input().split())
k=[]
for _ in range(m):
    l=list(map(float,input().split()))
    k.append(l)
t=zip(*k)
for i in t:
    print(sum(i)/len(i))

#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
