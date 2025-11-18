import re
n = int(input())
for _ in range(n):
    pattern=input()
    try:
        if re.search(r'(\*|\+|\?){2,}',pattern):
            print(False)
        else:
            re.compile(pattern)
            print(True)
    except re.error:
        print(False)


#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
