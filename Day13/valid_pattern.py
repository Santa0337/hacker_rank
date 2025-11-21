import re
n = int(input())
pattern = re.compile(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[A-Za-z0-9]{10}$')
for _ in range(n):
    uid = input()
    if re.match(pattern, uid):
        print("Valid")
    else:
        print("Invalid")


#https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true
