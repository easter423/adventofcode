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
f=open("1202.in","r")
MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split(','))
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

x=set([])
for i in range(1,1000000):
    x.add(int(str(i)*2))
for i in range(1,10000):
    x.add(int(str(i)*3))
for i in range(1,100):
    x.add(int(str(i)*5))
for i in range(1,100):
    x.add(int(str(i)*7))
for i in range(1,10):
    x.add(int(str(i)*11))
x=sorted(x)

ans=0
while True:
    try:
        IN=LIRS()
        for i in IN:
            s,e=map(int,i.split('-'))
            idx=bisect_left(x,s)
            while idx<len(x) and x[idx]<=e:
                if x[idx]>=s:
                    ans+=x[idx]
                idx+=1
    except:
        break
print(ans)