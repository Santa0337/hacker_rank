n=input()
l=list(map(int,input().split()))
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i,j in dic.items():
    if j==1:
        print(i)

#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
