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
f=open("1209.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

a=[]
b=[]
c=[]
IN=IR()
idx=0
flag=True
dist=0
for cc in IN:
    ic=int(cc)
    if flag:
        if ic:
            for _ in range(ic):
                a.append(idx)
            b.append([dist,ic])
    else:
        if ic:
            for _ in range(ic):
                a.append(-1)
            c.append([dist,ic])
        idx+=1
    dist+=ic
    flag=not flag

for db,lnb in b[::-1]:
    for idx,(dc,lnc) in enumerate(c):
        if db<=dc:
            break
        if lnc and lnb<=lnc:
            for i in range(lnb):
                a[dc+i]=a[db+i]
                a[db+i]=-1
            c[idx]=[dc+lnb,lnc-lnb]
            break
ans=0
for idx,i in enumerate(a):
    if i==-1:
        continue
    ans+=idx*i
print(ans)
f.close()