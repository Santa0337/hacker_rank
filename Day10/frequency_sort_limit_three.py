#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    s = input()
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    items = list(d.items())
    items.sort()
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    for ch, freq in items[:3]:
        print(ch, freq)
#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
