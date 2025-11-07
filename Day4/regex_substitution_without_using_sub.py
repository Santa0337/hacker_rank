import re
pattern = r'(?<= )(&&|\|\|)(?= )'
replace = lambda m : 'and' if m.group() == '&&' else 'or'
print(*(re.sub(pattern,replace,input()) 
for _ in range(int(input()))),sep='\n')

#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
