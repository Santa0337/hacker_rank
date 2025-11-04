# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
for _ in range(q):
    len_l1=int(input())
    a=input().split()
    len_l2=int(input())
    b=input().split()
    if len_l1<len_l2:
        for i in a:
            if i in b:
                continue
            else:
                print(False)
                break
        else:
            print(True)
    else:
        print(False)

#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
