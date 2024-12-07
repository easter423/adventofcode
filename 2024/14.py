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
f=open("1207.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

def fun(now,ans,l,idx):
    if len(l)<=idx:
        if now==ans:
            return True
        else:
            return False
    if now*(10**len(str(l[idx])))+l[idx]<=ans:
        if fun(now*(10**len(str(l[idx])))+l[idx],ans,l,idx+1):
            return True
    if now*l[idx]<=ans:
        if fun(now*l[idx],ans,l,idx+1):
            return True
    if now+l[idx]<=ans:
        if fun(now+l[idx],ans,l,idx+1):
            return True
    return False

ans=0
while True:
    IN=IR()
    if not IN:
        break
    x=list(IN.split())
    sm=int(x[0][:-1])
    l=list(map(int,x[1:]))
    if fun(l[0],sm,l,1):
        ans+=sm
print(ans)
f.close()