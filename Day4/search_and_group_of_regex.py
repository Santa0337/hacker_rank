# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

fount_it = re.search(r'([a-zA-Z0-9])\1+', S)

if fount_it: 
    print(fount_it.group(1)) 
else: 
    print(-1)

#https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
