# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    nos = int(input())
    in_list = input().split()
    start = int(in_list[0])
    end = int(in_list[-1])
    if start<end:
        val = end
        in_list.pop(-1)
    else:
        val = start
        in_list.pop(0)
    while len(in_list)>0:
        start = int(in_list[0])
        end = int(in_list[-1])
        if val>=end and end>=start:
            val = end
            in_list.pop(-1)
        elif val>=start and start>=end:
            val = start
            in_list.pop(0)
        else:
            print("No")
            break
    if len(in_list)==0:
        print("Yes")            
#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
