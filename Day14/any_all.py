n=int(input())
l=list(map(int,input().split()))
print(all(x > 0 for x in l) and any(str(x) == str(x)[::-1] for x in l))


#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
