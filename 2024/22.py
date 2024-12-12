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

d=defaultdict(lambda: [1]+[-1]*75)

def fun(x, step):
    if step==0:
        return 1
    sx=str(x)
    lx=len(sx)
    if x==0:
        if d[1][step-1]==-1:
            d[1][step-1]=fun(1,step-1)
        d[x][step] = d[1][step-1]
    elif lx&1:
        if d[x*2024][step-1]==-1:
            d[x*2024][step-1]=fun(x*2024,step-1)
        d[x][step] = d[x*2024][step-1]
    else:
        lx//=2
        l,r=int(sx[:lx]),int(sx[lx:])
        if d[l][step-1]==-1:
            d[l][step-1]=fun(l,step-1)
        if d[r][step-1]==-1:
            d[r][step-1]=fun(r,step-1)
        d[x][step] = d[l][step-1]+d[r][step-1]
    return d[x][step]

ans=0
a=LI()
print(a)
for i in a:
    ans+=fun(i,75)
print(ans)

f.close()