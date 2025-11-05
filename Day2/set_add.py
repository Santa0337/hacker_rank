n = int(input())
s=set()
for _ in range(n):
    i=input()
    if i not in s:
        s.add(i)
        
 
print(len(s))

#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
