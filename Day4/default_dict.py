# # Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
d={}
for i in range(1,n+1):
    w=input()
    if w not in d:
        d[w]=[]
    d[w].append(str(i))

for _ in range(m):
    y=input()
    if y in d:
        print(' '.join(d[y]))
    else:
        print(-1)

# # # Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import defaultdict
# n,m=map(int,input().split())
# d=defaultdict(list)
# for i in range(1,n+1):
#     w=input()
#     d[w].append(str(i))

# for _ in range(m):
#     y=input()
#     if y in d:
#         print(' '.join(d[y]))
#     else:
#         print(-1)


#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
