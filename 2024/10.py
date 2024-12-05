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
from graphlib import TopologicalSorter
input = sys.stdin.readline
f=open("1205.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

x=False
ans=0
order=defaultdict(set)
seq=[]
while True:
    IN=IR()
    if not IN:
        if not x:
            x=True
        else:
            break
        continue
    if not x:
        a,b=map(int,IN.split('|'))
        order[b].add(a)
    else:
        seq.append(list(map(int,IN.split(','))))
for s in seq:
    ts=TopologicalSorter()
    for i in s:
        for j in list(order[i]):
            if j in s:
                ts.add(i,j)
    tss=[*ts.static_order()]
    for i in range(len(s)):
        if s[i]!=tss[i]:
            break
    else:
        continue
    ans+=tss[len(s)//2]
print(ans)
f.close()