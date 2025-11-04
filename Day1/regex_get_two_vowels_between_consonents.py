import re
pattern=re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])',input())
if pattern:    
    print(*pattern, sep='\n')
else:
    print(-1)


#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
