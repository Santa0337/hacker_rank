#!/bin/python3

import math
import os
import random
import re
import sys

s=str()
l=list()
size=input().split()
n=int(size[0])
m=int(size[1])
for _ in range(n):
    a=input()
    l.append(a)
for j in range(m):
    for i in l:
        s+=i[j]
r=re.sub(r"(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])"," ",s)
print(r)
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
