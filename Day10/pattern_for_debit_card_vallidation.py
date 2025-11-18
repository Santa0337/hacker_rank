import re 
n=int(input())
for _ in range(n):
    pattern = re.findall(r'^(?!.*(\d)(-?\1){3})[4-6](\d){3}(-?\d{4}){3}$',input())
    if pattern:
        print("Valid")
    else:
        print("Invalid")

#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
