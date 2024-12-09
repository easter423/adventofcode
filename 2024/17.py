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
IN=IR()
idx=0
flag=True
for c in IN:
    if flag:
        for _ in range(int(c)):
            a.append(idx)
    else:
        for _ in range(int(c)):
            a.append(-1)
        idx+=1
    flag=not flag
l,r=0,len(a)-1
while l<r:
    if a[l]!=-1:
        l+=1
    elif a[r]==-1:
        r-=1
    else:
        a[l]=a[r]
        a[r]=-1
        l+=1
        r-=1
ans=0
for idx,i in enumerate(a):
    if i==-1:
        break
    ans+=idx*i
print(ans)
f.close()