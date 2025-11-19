from collections import namedtuple

size = int(input())
fields = input().split()
Student = namedtuple("Student", fields)
total = 0
for _ in range(size):
    row = input().split()
    stu = Student(*row)
    total += int(stu.MARKS)
average = total / size
print(f"{average:.2f}")

#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
