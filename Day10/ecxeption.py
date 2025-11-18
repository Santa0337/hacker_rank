n = int(input())
for _ in range(n):
    try:
        a, b = map(int, input().split())
        x = int(a)/int(b)
        print(int(x))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)


#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
