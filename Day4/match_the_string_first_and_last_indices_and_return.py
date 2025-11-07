import re

S = input().strip()
k = input().strip()

pattern = re.compile(rf'(?=({k}))')
matches = list(pattern.finditer(S))

if not matches:
    print((-1, -1))
else:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))


#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
