# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
string = input()
groups = itertools.groupby(string)
results = []
for key, group in groups:
    count = 0
    for item in group:
        count += 1
    results.append((count, int(key)))

print(*results)

#https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
