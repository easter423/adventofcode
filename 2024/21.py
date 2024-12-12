import sys, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import Fraction
from decimal import *
from heapq import heapify, heappop, heappush, heappushpop
from datetime import datetime
from functools import cache
input = sys.stdin.readline
f=open("1211.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

a=LI()
for step in range(25):
    b=[]
    for i in a:
        si=str(i)
        li=len(si)
        if i==0:
            b.append(1)
        elif li&1:
            b.append(i*2024)
        else:
            li//=2
            b.append(int(si[:li]))
            b.append(int(si[li:]))
    a=b[:]
    print(step,end=' ')
print()
print(len(b))

f.close()